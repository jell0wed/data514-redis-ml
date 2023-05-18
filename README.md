# Redis as high-performance ML cache for text prediction
The intent of this project is to demonstrate how Redis can be used as a high-performance database engine for machine learning text generation tasks.

## Project requirements
Software used throughout this project:
- **Redis**: High-performance database management system
- Jupyter Notebook
- Python
- Pandas

## System setup

### Windows
- You must first install [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-windows/) for Windows.
To do so, you must have Windows Subsystem for Linux enabled (details on how to enable the feature in [here](https://learn.microsoft.com/en-us/windows/wsl/install)).
Once WSL is installed, follow [these instructions](https://redis.io/docs/getting-started/installation/install-redis-on-windows/) to install Redis on your local operating system.\
Issue `sudo service redis-server start` to start up the Redis database.
- Install [python2-minimal](https://linux.how2shout.com/how-to-install-python-2-7-on-ubuntu-20-04-lts/) on the WSL operating system.
You can simply issue the following commands: 
`sudo apt-add-repository universe`
`sudo apt-get update`
`sudo apt-get install python2-minimal`
and update the default python alternative:
`sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1`
You can then confirm that Python was installed by looking at the python version `python --version` should give `Python 2.7.18`
- Install `pip` for your Python version: 
`curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py`
`sudo python get-pip.py`
- Install Jupyter notebook with the following command:
`pip install jupyterlab`

## Project setup
- Clone the repository
- Install python dependencies using pip 
`pip install -r requirements.txt`