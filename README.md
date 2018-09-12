# DryAzPi
Raspberry Pi controlled Dehydrator with Azure

Monitor a home dehydrator using an IoT device (Raspberry Pi) with a temperature sensor and sync data to Azure Storage.

# Development
## Dependencies
[Pyenv](https://github.com/pyenv/pyenv) is used to manage the runtime and packages for this project. It can be installed by following [these instructions](https://github.com/pyenv/pyenv#installation).

To restore dependencies listed in _Pipfile_ (will create a virtual environment if one does not exist):
```bash
$ pipenv install
```

To run a Raspberry Pi simulator that generates a JSON payload every second:
```bash
$ pipenv run python src/main.py
```
