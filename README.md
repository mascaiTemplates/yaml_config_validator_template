# YAML config validator

### Aim - create reusable model to validate .yaml configfile and convert it to python object

# How to apply to your project
1. Copy `src/base_model.py` to your project
2. Inherit your model from `YamlModel` (see `src/example_model.py` for example)


# How to install
```
python -m venv venv
pip install -r requirements.txt
```

# How to run tests
```
pip install -r requirements_test.txt

pytest
```