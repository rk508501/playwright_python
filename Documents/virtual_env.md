# How to Initialize a Python Virtual Environment

Follow these steps to create and activate a virtual environment for your Python project:

## 1. Open Terminal in Project Folder

```sh
cd C:\Users\itsga\OneDrive\Documents\Playwright_Python
```

## 2. Create a Virtual Environment

```sh
python -m venv venv
```

This creates a folder named `venv` containing your virtual environment.

## 3. Activate the Virtual Environment (Windows)

```sh
.\venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal prompt.

## 4. Verify Activation (Optional)

```sh
python --version
```

You are now ready to install packages and run Python scripts in