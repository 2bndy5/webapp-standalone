# webapp

[![Documentation Status](https://readthedocs.org/projects/vve-webapp/badge/?version=latest)](https://vve-webapp.readthedocs.io/en/latest/?badge=latest)

Flask webapp for interacting and remotely controlling the MASCCOT robot via WiFi.


# How to Contribute
check out our [contributing guidelines](https://github.com/DVC-Viking-Robotics/about-us/blob/master/Contributing%20Guidelines.rst)

# How to add or change the documentation
check out our guide on [contributing documentation](https://github.com/DVC-Viking-Robotics/about-us/blob/master/Contributing%20Documentation.rst)

## Setup instructions
# Clone the repository navigate to its root folder
```bash
git clone https://github.com/2bndy5/webapp-standalone.git
cd webapp-standalone
```
# Prepare the virtual environment
```bash
pip install virtualenv
python -m venv env
```
# Activate the virtual environment
For Windows
```bash
env\\Scripts\\activate.bat
```
For Linux
```bash
source env/bin/activate
```
# Install Dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```
On the Raspberry Pi, you'll need to install the `picamera` module via `apt`:
```bash
sudo apt-get install python3-picamera
```
## Running the server
```bash
python -m webapp.app
```
