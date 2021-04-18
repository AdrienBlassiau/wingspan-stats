# wingspan-stats
*A tool for Wingspan enthusiasts. It plots your games scores with a lot of useful informations.*

## Presentation
The tool is made to be really *user-friendly*. How does it work ? 
- **First**, write all your score on a **scores.csv** file,
- **Then**, create a beautiful resume of all you games by running the script ! It looks like this :

![Alt text](img/example.png?raw=true "Title")

## Q&A for package users

### How to write your score ?
Its really simple ! Open the scores.csv (inside the input folder) in your favorite csv editor (EXCEL, LibreOffice Calc, ...) and then write all
your score. It works like this : 
- **index** : is the index of the game,
- **player_name** : is the name of the player involve in the current game,
- **birds** : is the number of birds points of the current player involve in the current game,
- **bonus_cards** : is the number of bonus cards points of the current player involve in the current game,
- **end_of_round_goals** : is the number of end of round goals points of the current player involve in the current game,
- **eggs** : is the number of eggs points of the current player involve in the current game,
- **food_on_cards** : is the number of food on cards points of the current player involve in the current game,
- **tucked_cards** : is the number of tucked cards points of the current player involve in the current game,
- **nectars** : is the number of nectars points of the current player involve in the current game,
- **game_type** : is the type of the game (put 0 or 1 here, this feature is not used for the moment ....).

An example with three games with player A, B and C is given on player.csv file inside the archive.

### How to run the script that draw my results ?
Easy. Double click on wingspan-stats.exe (or wingspan-stats if you are on linux) ... and enjoy your performance. 

### Can I customize the graph ?
Yes you can ;) It's inside the wingspan.stats.ini file. For the moment, you can : 
- **change the language** (english and french supported),
- **change the color** of the bars (in hexadecimal format).

This feature will evolve in the future !

## Q&A for programmer users

### I want to work on this project, how can I do ?

You can clone the repository of the project, which is located at this address :  https://github.com/AdrienBlassiau/wingspan-stats.

#### If you want to install the project locally on your machine

If you want to work on this project on your machine, your only need to install the python3 dependency.

A. Install the python3 dependencies:
```
$ python3 -m pip install -r requirements.txt
```

B. Then, run the program with:
```
$ python3 main.py
```

#### If you want to build the project

If you want to create a build of the project, you will need a version of python3-dev and a version of pyinstaller.
Then a simple call to build.py script will create an executable of the project on the dist folder.

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

## Any suggestion, any issue ?
You can send an email to *adblassiau@gmail.com* or create a new issue on github ;)

I will do my best to help you !