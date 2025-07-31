# Undertale Save State Manager
This is a WIP project that aims to create a comprehensive (gui) save state manager for Undertale.
## Project state
As this is a WIP project and early in its development there may certainly be bugs and other issues.

**No gui exists yet.** Currently this repo contains the backend modules for
- reading Undertale files (e.g. `file0`, `undertale.ini`) and 
- managing multiple saves(e.g. saving, loading and timetravel). Yes, you can load a past save and split of a branch.
## Installation
You can install the package via pip using the following command:
```shell
pip install git+https://github.com/RedBugGamer/undertaleSSM.git
```
## Usage
Currently you can use this mostly as a library for reading undertale files. I might include some example code and/or docs in the future. In the meantime you can have a look at the `undertaleSSM.fileInterface.undertaleReader` module. You can load a directory using the following example.
```python
from undertaleSSM.fileInterface.undertaleReader import undertaleDir

directory = undertaleDir.UndertaleDir("/path/to/a/directory/containing/undertale/files/")

print(directory.file0.room)
print(directory.file0.inventory)
print(directory.iniFile.general_time)

```

I don't recommend using the `undertaleSSM.fileInterface` module at the moment, as no documentation exists and it likely has bugs.

**I am not responsible for lost data!**
