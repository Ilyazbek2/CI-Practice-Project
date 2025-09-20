# CI-Practice-Project

This is a small project for practicing **Python testing** and **CI/CD basics**.

## Features
- Function `head_file(path, n=100)`:
  - Returns first bytes of file
  - Detects text vs binary
  - Returns status code (200 or 404)

## Tests
- Implemented with `unittest`
- Cases:
  - Empty file
  - Missing file
  - Binary file
  - Text file
  - Invalid input type

## Run tests

```bash
pytest -v
