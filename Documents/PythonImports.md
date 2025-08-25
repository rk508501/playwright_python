# Python Imports and Module Execution

## Imports and Exports in Python

- **Importing** allows you to use code from other modules or packages.
- Use `import module` or `from module import object` to access functions, classes, or variables.
- Python searches for modules in directories listed in `sys.path`.
- Packages are directories containing an `__init__.py` file (can be empty).

**Example:**
```python
from helpers.Greetings import Greetings
```
This imports the `Greetings` class from `helpers/Greetings.py`.

## Exporting

- Any function, class, or variable defined in a module is "exported" and can be imported elsewhere.
- You can control what is exported using the `__all__` list in a module.

## Running Modules with `-m`

- The `-m` flag lets you run a module or package as a script.
- It sets up the import paths so relative imports work correctly.

**Example:**
```sh
python -m tests.TestGreetings
```
This runs `TestGreetings.py` inside the `tests` package.

**Significance:**
- Ensures your code runs with the correct package context.
- Avoids manual path manipulation (like editing `sys.path`).
- Makes relative imports work as expected.

## Best Practices

- Structure your project as a package.
- Use `python -m` to run scripts inside packages.
- Avoid modifying `sys.path` in your code unless necessary.
