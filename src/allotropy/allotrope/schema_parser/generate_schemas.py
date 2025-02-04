import os
from pathlib import Path
import re
import subprocess  # noqa: S404, RUF100

from autoflake import fix_file  # type: ignore[import-untyped]
from datamodel_code_generator import (
    DataModelType,
    generate,
    InputFileType,
    PythonVersion,
)

from allotropy.allotrope.schema_parser.backup_manager import (
    backup,
    is_backup_file,
    is_file_changed,
    restore_backup,
)
from allotropy.allotrope.schema_parser.model_class_editor import modify_file
from allotropy.allotrope.schema_parser.schema_cleaner import SchemaCleaner
from allotropy.allotrope.schema_parser.update_units import update_unit_files

SCHEMA_DIR_PATH = "src/allotropy/allotrope/schemas"
SHARED_SCHEMAS_PATH = os.path.join(SCHEMA_DIR_PATH, "shared", "definitions")
UNITS_SCHEMAS_PATH = os.path.join(SHARED_SCHEMAS_PATH, "units.json")
CUSTOM_SCHEMAS_PATH = os.path.join(SHARED_SCHEMAS_PATH, "custom.json")
MODEL_DIR_PATH = "src/allotropy/allotrope/models"
SHARED_MODELS_PATH = os.path.join(MODEL_DIR_PATH, "shared", "definitions")
UNITS_MODELS_PATH = os.path.join(SHARED_MODELS_PATH, "units.py")
CUSTOM_MODELS_PATH = os.path.join(SHARED_MODELS_PATH, "custom.py")
GENERATED_SHARED_PATHS = [
    UNITS_SCHEMAS_PATH,
    UNITS_MODELS_PATH,
    CUSTOM_SCHEMAS_PATH,
    CUSTOM_MODELS_PATH,
]


def lint_file(model_path: str) -> None:
    # The first run of ruff changes typing annotations and causes unused imports. We catch failure
    # due to unused imports.
    try:
        subprocess.check_call(
            f"ruff {model_path} --fix",
            shell=True,  # noqa: S602
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        pass
    # The call to autoflake.fix_file removes unused imports.
    fix_file(
        model_path,
        {
            "in_place": True,
            "remove_unused_variables": True,
            "write_to_stdout": False,
            "ignore_init_module_imports": False,
            "expand_star_imports": False,
            "remove_all_unused_imports": True,
            "remove_duplicate_keys": True,
            "remove_rhs_for_unused_variables": False,
            "ignore_pass_statements": False,
            "ignore_pass_after_docstring": False,
            "check": False,
            "check_diff": False,
        },
    )
    # The second call to ruff checks for additional rules.
    subprocess.check_call(
        f"ruff {model_path} --fix", shell=True, stdout=subprocess.DEVNULL  # noqa: S602
    )
    subprocess.check_call(
        f"black {model_path}", shell=True, stderr=subprocess.DEVNULL  # noqa: S602
    )


def _get_schema_and_model_paths(
    root_dir: Path, rel_schema_path: Path
) -> tuple[Path, Path]:
    schema_path = Path(root_dir, SCHEMA_DIR_PATH, rel_schema_path)
    model_file = re.sub(
        "/|-", "_", f"{rel_schema_path.parent}_{rel_schema_path.stem}.py"
    ).lower()
    model_path = Path(root_dir, MODEL_DIR_PATH, model_file)
    return schema_path, model_path


def _generate_schema(model_path: Path, schema_path: Path) -> None:
    # Generate models
    generate(
        input_=schema_path,
        output=model_path,
        output_model_type=DataModelType.DataclassesDataclass,
        input_file_type=InputFileType.JsonSchema,
        # Specify base_class as empty when using dataclass
        base_class="",
        target_python_version=PythonVersion.PY_310,
        use_union_operator=True,
    )
    # Import classes from shared files, remove unused classes, format.
    modify_file(str(model_path), str(schema_path))
    lint_file(str(model_path))


def _should_generate_schema(schema_path: str, schema_regex: str | None = None) -> bool:
    # Skip files in the shared directory
    if schema_path.startswith("shared"):
        return False
    if is_backup_file(schema_path):
        return False
    if schema_regex:
        return bool(re.match(schema_regex, str(schema_path)))
    return True


def generate_schemas(
    root_dir: Path,
    *,
    dry_run: bool | None = False,
    schema_regex: str | None = None,
) -> list[str]:
    """Generate schemas from JSON schema files.

    :root_dir: The root directory of the project.
    :dry_run: If true, does not save changes to any models, but still returns the list of models that would change.
    :schema_regex: If set, filters schemas to generate using regex.
    :return: A list of model files that were changed.
    """

    unit_to_iri: dict[str, str] = {}
    with backup(GENERATED_SHARED_PATHS, restore=dry_run):
        os.chdir(os.path.join(root_dir, SCHEMA_DIR_PATH))
        schema_paths = list(Path(".").rglob("*.json"))
        os.chdir(os.path.join(root_dir))
        models_changed = []
        for rel_schema_path in schema_paths:
            if not _should_generate_schema(str(rel_schema_path), schema_regex):
                continue

            print(f"Generating models for schema: {rel_schema_path}...")  # noqa: T201
            schema_path, model_path = _get_schema_and_model_paths(
                root_dir, rel_schema_path
            )

            with backup(model_path, restore=dry_run), backup(schema_path, restore=True):
                schema_cleaner = SchemaCleaner()
                schema_cleaner.clean_file(str(schema_path))
                unit_to_iri |= schema_cleaner.get_referenced_units()
                _generate_schema(model_path, schema_path)

                if is_file_changed(model_path):
                    models_changed.append(model_path.stem)
                else:
                    restore_backup(model_path)

        update_unit_files(unit_to_iri)
        for path in [UNITS_MODELS_PATH, CUSTOM_MODELS_PATH]:
            lint_file(path)

    return models_changed
