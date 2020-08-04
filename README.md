
<img src="https://raw.githubusercontent.com/Eoin-McMahon/raycast/master/raycast_image.png" alt="banner" style="width:100%;">

# raycast
Python raycasting demo using p5py

This is a port based off of the javascript implementation shown here: https://www.youtube.com/watch?v=TOEi6T2mtHo&t=1708s
This should be more performant however, i noticed there were a number of duplicate heavy calculations being made in the video which have been fixed here.


Requirements:
* Python 3 or above
* p5py
* Glfw: most linux distros have it but if not install it using this link: https://p5.readthedocs.io/en/latest/install.html#installing-p5

Installation:
* make sure you are using pip for python 3
* run the following command:
```bash
# installs the requirements for the program
pip install -r requirements.txt --user
```

Run the code:
```bash
# use the mouse as input
python3 main.py
```
```bash
# auto move the source particle
python3 main.py --auto
```

```bash
# set number of rays to 180, the smaller the number, the more performant
python3 main.py --rays 180
```