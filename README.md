# What is this?

Personally I find it really difficult to change my profile pictures / login icon while using gdm.

I couldn't find any clear guides or tools with this feature so im making my own!
Hope someone finds it useful :D

---

# Easy Setup
One command installer! Just copy and paste.
```
git clone https://github.com/OmletCat/GDMpfpChanger.git
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Easy run
```
source env/bin/activate
python main.py
```

Alternatively you can run the program with the `start.bash` script

Note: You may need to install tkinter on your machine for the application to work, please refer to instructions below

# Manual Install
1. ensure you have the following dependancies
- python
- python tkinter

## python tkinter

### Arch
```
$ sudo pacman -S tk
```

### Ubuntu
```
$ sudo apt-get install python3-tk
```

2. Python dependancies

In the folder where your project is create a python virtual environment
and run the following:
```
pip install -r requirements.txt
```


3. Run the program

```
$ python main.py
```

or

```
sh start.bash
```

# Usage

1. Select an image with the gui (I've only tested pngs)
2. Check the image is correct by using the "Show image" button, should open in either an image viewer or a webbrowser
3. Click "Get Command"
4. Command should automatically be copied to clipboard, otherwise copy it manually
5. run command in terminal
