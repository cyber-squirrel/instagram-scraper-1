# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### [0.4.0] - 2020-11-18

#### Added

- Formatted all .py files to conform to [Black code style](https://github.com/ambv/black)
- Updated all requirements to run Python 3.9
- Updated tests
- Updated Documentation (README and CHANGELOG)
- Added initial github ci

## [Todo]

- 4 tests currently fail possible culprit [June 29 changelog](https://www.instagram.com/developer/):
  - test_get_code_from_id
  - test_get_code_from_code
  - test_get_location_by_id
  - test_get_location_medias_by_id
- Increase test coverage from 31%
- Add more tests see tests/coverage.yml for more information
- Remove non-auth options from from examples and scripts
- Add documentation
