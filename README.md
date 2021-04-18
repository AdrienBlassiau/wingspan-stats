# wingspan-stats
A tool for Wingspan enthusiasts. It plot your games scores with a lot of useful informations.

## TODO
- add log for better debug and a debug mode to activate it
- add more option on ini file (and more features, graph type, etc)

## Help ! How to use this wingspan-stats ?
Open to ```data/HELP.md``` for more information about how to use the tool.

## If you want to install the project locally on your machine

If you want to work on this project on your machine, your only need to install
the python3 dependency.

A. Install the python3 dependencies:
```
$ python3 -m pip install -r requirements.txt
```

B. Then, run the program with:
```
$ python3 main.py
```

## If you want to build the project

If you want to build the project, you will need a version of python3-dev and a version of pyinstaller.
Then a simple call to build.py script will build create an executable of the project on dist folder.

A. Install python3-dev :
```
$ sudo apt-get install python3-dev
```

B. Install pyinstaller :
```
$ python3 -m install pyinstaller
```

C. Then you can run the build with this command :
```
$ python3 build.py
```