<h2 align="center">
  <br>
 <img src="./assets/banner.png?v=1" alt="banner" style="width:100%;">
  <br>
  <br>
</h2>
  
# 💡 Raycast


* A python raycasting demo using p5py
* This is a port based off of the javascript implementation shown here: https://www.youtube.com/watch?v=TOEi6T2mtHo&t=1708s
* This should be (it isn't because unlike p5js, its not built ontop of the skia engine) more performant however than the video, I noticed there were a number of duplicate heavy calculations being made in the video which have been fixed here.

### 🔧 Demo
<p align="center">
<img src="./assets/demo.gif" alt="demo" style="width:100%;">
</p>

### 📓 Requirements:
##### system
* Python 3
* Glfw: install it using this link: https://p5.readthedocs.io/en/latest/install.html#installing-p5
##### pip
* absl-py
* p5py

### 📦 Installation:
* make sure you are using pip for python 3
* run the following command:
```bash
# installs the requirements for the program
pip install -r requirements.txt --user
```

### ✨ Examples:
```bash
# use the mouse as input
python3 main.py
```
```bash
# automatically move the source particle
python3 main.py --auto
```

```bash
# set number of rays to 36, the smaller the number, the more performant
python3 main.py --rays 36
```
