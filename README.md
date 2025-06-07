# What is this?

Personally I find it really difficult to change my profile pictures while using gdm.

I couldn't find any clear guides or tools with this feature so im making my own! :D

---

# Easy Setup
One command installer
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

# How to change gdm Profile
Either use the tool provided or follow these instructions

---

# To Do

- [x] select image
- [x] move image
- [x] have script identify username
- [ ] pop up for errors and done

- [ ] make things more clear

- [ ] package and put on aur?
- [ ] easy set of instructions like one set of commands in a ``` ``` so you just copy and paste it once into the terminal and it works
