# Redis as high-performance ML cache for text prediction
The intent of this project is to demonstrate how Redis can be used as a high-performance database engine for machine learning text generation tasks.

## Project requirements
Software used throughout this project:
- **Redis**: High-performance database management system
- Docker
- Jupyter Notebook
- Python
- Pandas

## System setup

### Ubuntu
- Intall python3 with the following commands
`sudo apt-get update`
`sudo apt-get install python3 python3-pip`
and update the default python alternative:
`sudo update-alternatives --install /usr/bin/python python /usr/bin/python33 1`
You can then confirm that Python was installed by looking at the python version `python --version` should give `Python 3.xxx`
- Install Jupyter notebook with the following command:
`pip install jupyterlab`

## Project setup
- Clone the repository
- Using docker, start the redis server stack with the following command: 
`docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest`
- Install python dependencies using pip 
`pip install -r requirements.txt`

