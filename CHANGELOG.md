# Changelog

All notable changes to this packages will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Script to create graph visualization of calculated data documents from asm json files
- Details of parser requirements to docs
- Add Agilent Gen5 Image Adapter

### Fixed

### Changed
- Upgraded allotropy python requirement to python 10
- Updated ASM model class typing to use or union
- Implement default value for sample role names in AppBio Quantstudio

### Deprecated

### Removed

### Security

## [0.1.30] - 2024-05-10

### Added

- Global definition of calculated data documents representation
- Update bioplex to use _get_date_time
- Add structure for Methodical Mind

### Fixed
- Remove duplicated ct sd and ct se calculated data documents in Quantstudio Design and Analysis adapter
- Remove duplicated quantity mean calculated data documents from AppBio Quantstudio adapter

### Changed
- Update multianalyte model minimum_assay_bead_count to be of type "number" insetead of "unitless"
- Update luminex and biorad bioplex to use updated multianalyte model
- Remove inner calculated data documents from AppBio Quantstudio
- Use global definition of calculated data documents in AppBio Quantstudio and Quantstudio Design and Analysis adapters

### Deprecated

### Removed

### Security

## [0.1.29] - 2024-04-30

### Added

- Add Vendor display names
- Added liquid-chromatograpy 2023/09 schema

### Fixed

### Changed

- Improved schema model generation script to handle more complicated schemas

### Deprecated

### Removed

- Remove assert in validate_contents

### Security


## [0.1.28] - 2024-04-29

### Added

- Add AppBio Quantstudio Design and Analysis adapter
- Add software version to Chemometec Nucleoview
- Biorad Bioplex adapter
- Utils for parsing xml
- Rename the Biorad Bioplex to "Biorad Bioplex Manager"
- Add a utility to remove non-required None values from a dataclass
- Add Beckman PharmSpec adapter

### Fixed

- Re-added encoding inference to Beckman VI Cell Blu adapter
- Corrected concentration unit in Lunatic to conform to unit as reported within the source file
- Corrected Luminex xPonent adapter to output one multi analyte profiling document per well.
- Remove duplicated calculated data documents of delta ct se in AppBio Quantstudio

### Changed

- Use new plate reader schema in gen5 adapter

### Deprecated

### Removed

### Security

## [0.1.27] - 2024-04-10

### Added

- Added allotropy.testing library, exposing test utils for validating ASM outside of allotropy

### Changed

- Exclude tests from sdist

## [0.1.26] - 2024-04-08

### Fixed

- Reverted "add encoding inference to Beckman Vi Cell Blu adapter" - it is causing unexpected behavior in other environments

## [0.1.25] - 2024-04-05

### Fixed

- Add encoding inference to Beckman Vi Cell Blu adapter
- Fix Luminex Xponent adapter to account for the correct instrument file formatting

## [0.1.24] - 2024-04-03

### Added

- Add optical imaging to plate reader schema
- Add Revvity Kaleido adapter

### Fixed

- Change lightfield with brightfield in transmitted light setting enum of plate reader schema
- Fix missing case for concentration column without A260 prefix in Unchained Labs Lunatic

## [0.1.23] - 2024-03-12

### Added

- Add Qiacuity dPCR adapter

### Changed

- Added ability to specify encoding in top-level functions. Not passing an encoding defaults to UTF-8. To auto-detect encoding with chardet, pass in CHARDET_ENCODING
- Loosen requirement for jsonschema package to increase package compatibility

## [0.1.22] - 2024-03-07

### Fixed

- Fixed Softmax Pro handling of partially filled plates

### Changed

- Moved VendorType to to_allotrope

## [0.1.21] - 2024-03-05

### Fixed

- Add missing ct mean calculated data documents to relative std curve experiments in AppBio Quantstudio

### Changed

- Infer size of plate to read all data available in Moldev Softmax

## [0.1.20] - 2024-02-23

### Fixed

- Remove duplicated delta ct mean calculated data documents in AppBio Quantstudio
- Fix problem in NanoDrop Eight parser where data source IDs were being used that did not refer to any existing measurement ID

### Changed

- Allow n/a absorbance values in Unchained Labs Lunatic Parser

## [0.1.19] - 2024-02-19

### Fixed

- Fix try_float_or_none bug with evaluating 0 as NaN

## [0.1.18] - 2024-02-19

### Added

- Add try_float_or_nan util and fix bug with evaluating 0 as NaN
- Singleton UUID generator, allowing tests to generate stable ids

### Fixed

- Cast sample identifier to string when saving it in SoftmaxPro parser
- Handle style bug in xlsx files produced by VI-Cell XR instrument

## [0.1.17] - 2024-02-15

### Added

- Automatic validation of generated model in to_allotrope methods with error messages

### Fixed

- Handle invalid values in SoftmaxPro well measurements, filling with "NaN"

## [0.1.16] - 2024-02-08

### Fixed

- Fix mixup of Plate ID and Plate Position in Unchained Labs Lunatic Parser

## [0.1.15] - 2024-02-02

### Added

- pandas_utils module wraps pandas functions to throw AllotropeConversionError

### Fixed

- Total cells column no longer required for vi-cell XR
- Ignore invalid first row when present for vi-cell XR files
- Capture concentration on Nanodrop Eight files that do not have NA Type column
- Removed hardcoding of date parsing around Gen5 plate numbers

### Changed

- Corrections to the spectrophotometry/BENCHLING/2023/12 schema to account for feedback from Allotrope Modeling Working Group
- Replace null with N/A in Moldev Softmax Pro

## [0.1.14] - 2024-01-31

### Added

- Add Luminex xPONENT Adapter

### Fixed

- Ignore calculated data documents entry in output of Moldev Softmax Pro when there are no calculated data documents
- Check for raw data indicator in plate header for Moldev Softmax Pro

## [0.1.13] - 2024-01-19

### Added

- Add parser for ChemoMetic NucleoView
- Add parser for Nanodrop Eight
- Add calculated data documents to Unchained Labs Lunatic adapter
- Add calculated data documents to Moldev Softmax Pro
- Add multi-analyte-profiling BENCHLING/2024/01 schema
- Add non-numeric options for tQuantityValue value property
- Add support for non-numeric values to ChemoMetic NucleoView
- Add context manager to handle backups to schema generation script
- Add --regex argument to schema generation script

### Fixed

- Perkin Elmer Envision: calculated data name now captures string to the left - rather than right - of the ‘=’ in the Formula cell

### Changed

- Simplify Moldev Softmax Pro parsing with dataclasses
- Update plate reader schema in Moldev Softmax Pro
- Standardized on UNITLESS constant ("(unitless)") for unitless values. Changed Perkin Elmer Envision, which formerly used "unitless"
- Increase test coverage of calculated data documents on Perkin Elmer Envision

## [0.1.12] - 2023-12-12

### Added

- Calculated data documents to PerkinElmer EnVision
- Add Unchained Labs Lunatic adapter

### Fixed

- Fix per-well calculated documents in AppBio QuantStudio

### Changed

- Refactor builders as create methods in AppBio QuantStudio

## [0.1.11] - 2023-12-04

### Added

- Add parser structure documentation

### Changed

- Refactor Agilent Gen5 with explicit dataclasses structure
- Update Benchman Vi-cell Blu adapter to use the new cell-counting BENCHLING/2023/11 schema
- Update Benchman Vi-cell XR adapter to use the new cell-counting BENCHLING/2023/11 schema
- Set mypy's disallow_any_generics to True. Ideally, new files should not suppress these warnings
- Refactor way to extract and validate information from pandas series in AppBio QuantStudio
- Simplify CSV lines reader
- Update PerkinElmer EnVision adapter to use the new plate-reader BENCHLING/2023/09 schema
- Standaradize and clarify exception messages

## [0.1.10] - 2023-11-14

### Added

- Add data system document to plate reader schema

### Changed

- Redefine reporter dye setting for genotyping experiments in AppBio QuantStudio
- Refactor Moldev Softmax Pro with explicit dataclasses structure
- Inline VendorParser.parse_timestamp (was only used by VendorParser.get_date_time)
- Change TimeStampParser.parse() to raise for invalid input

## [0.1.9] - 2023-11-03

### Added

- Add missing example outputs for AppBio Quantstudio tests
- Add cell-counting REC/2023/09 schema, with additions to support existing use cases

### Fixed

- Update plate-reader schema to be compatible with current supported adapters and change REC -> BENCHLING

## [0.1.8] - 2023-10-30

### Added

- Allow lines reader to accept or infer encoding

### Fixed

- Use fuzzy=True for timestamp parsing to handle non-standard cases (e.g. mixing 24h time and AM/PM)

## [0.1.7] - 2023-10-26

### Added

- Governance document
- Added plate-reader REC/2023/09 schema (not in use by parsers yet)

### Fixed

### Changed

- Relax TimestampParser to use tzinfo for typing
- Change the cell counter schema name to match with the one published by Allotrope (cell counting)
- Update README, CONTRIBUTING, and pyproject.toml
- Rename to PerkinElmerEnvisionParser and RocheCedexBiohtParser for consistency
- Add additional plate reader testing data for the plate reader parser
- Change generic Exceptions to AllotropyErrors

## [0.1.6] - 2023-10-16

### Added

- Test for broken calculated document structure in AppBio QuantStudio

### Fixed

- Fix bug in result caching in AppBio Quantstudio

### Changed

- Allow block type to have plate well count in any position for AppBio QuantStudio
- Replace datetime.timezone with ZoneInfo in TimestampParser
- Implement CsvReader as child of LinesReader

## [0.1.5] - 2023-10-04

### Added

- Parser for AppBio Absoute Q dPCR exports

### Fixed

- Redefine calculated data documents references as required in AppBio QuantStudio parser
- Update dPCR schema "experiement type" enum to have correct values

### Changed

- Make "flourescence intensity threshold setting" optional in the dPCR schema
- Changed the "calculated datum" property on the calculated data documents to allow different units

## [0.1.4] - 2023-10-03

### Fixed

- Remove duplication of calculated documents related to quantity measurements in AppBio QuantStudio
- Rename "qPRC detection chemistry" to "PRC detection chemistry" in PCR schemas
- Add missing @dataclass annotation to TQuantityValueNumberPerMicroliter

## [0.1.3] - 2023-10-03

### Fixed

- Redefine the way calculated documents are structured for relative standard curve in AppBio QuantStudio
- Fixed some issues in dPCR schema and corresponding model updates
- Accept comma as thousand indicator in all sections of AppBio Quantstudio

## [0.1.2] - 2023-09-27

### Added

- Allotrope Simple Model schema for Digital PCR (dPCR) documents
- Calculated documents for the AppBio Quantstudio parser
- Genotyping data structure test for AppBio Quantstudio parser

### Fixed

- Typing ignore tags removed from the construction of AppBio Quantstudio structure
- Ignore unexpected sections in AppBio Quantstudio input file
- Accept comma as thousand indicator in AppBio Quantstudio results section

## [0.1.1] - 2023-09-22

### Changed

- Loosened requirement for jsonschema package to make allotropy compatible with datamodel-code-generator

## [0.1.0] - 2023-09-18

### Added

- Initial commit, includes support for:
  - Agilent Gen5
  - Applied Bio QuantStudio
  - Beckman Vi-Cell BLU
  - Beckman Vi-Cell XR
  - MolDev SoftMax Pro
  - NovaBio Flex2
  - PerkinElmer Envision
  - Roche Cedex BioHT
