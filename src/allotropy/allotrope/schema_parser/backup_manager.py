from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from itertools import zip_longest
from pathlib import Path
import shutil

PathType = Path | str


def _files_equal(path1: PathType, path2: PathType) -> bool:
    with open(str(path1)) as file1, open(str(path2)) as file2:
        for line1, line2 in zip_longest(file1, file2, fillvalue=""):
            if line1 != line2 and not line1.startswith("#   timestamp:"):
                return False
    return True


def _get_backup_path(path: PathType) -> Path:
    _path = Path(path)
    return Path(_path.parent, f".{_path.stem}.bak{_path.suffix}")


def is_file_changed(path: PathType) -> bool:
    backup_path = _get_backup_path(path)
    if backup_path.exists():
        return not _files_equal(path, backup_path)
    return True


def _backup_file(path: PathType) -> None:
    if Path(path).exists():
        shutil.copyfile(path, str(_get_backup_path(path)))


def restore_backup(path: PathType) -> None:
    backup_path = _get_backup_path(path)
    if backup_path.exists():
        backup_path.rename(path)


def _remove_backup(path: PathType) -> None:
    _get_backup_path(path).unlink(missing_ok=True)


def is_backup_file(path: PathType) -> bool:
    return ".bak" in Path(path).suffixes


@contextmanager
def backup(
    paths: Sequence[PathType] | PathType, *, restore: bool | None = False
) -> Iterator[None]:
    paths_ = paths if isinstance(paths, list) else [paths]
    for path in paths_:
        _backup_file(path)
    try:
        yield
    except Exception:
        for path in paths_:
            restore_backup(path)
        raise

    if restore:
        for path in paths_:
            restore_backup(path)
    else:
        for path in paths_:
            _remove_backup(path)
