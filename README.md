# Redis as high-performance ML cache for text prediction
The intent of this project is to demonstrate how Redis can be used as a high-performance database engine for machine learning text generation tasks.

## Project overview
The primary objective of this research project is to demonstrate the practical application of Redis within a real-world machine learning pipeline focused on natural language processing. Specifically, we aim to utilize Redis as a high-performance, in-memory database to support the classification of toxic comments found on the internet. The overarching idea is to leverage Redis as the backbone database to store the training, testing, and validation datasets required for training a deep learning model for text classification. The model will be designed to categorize text into five distinct categories, namely toxic, obscene, threat, and identity hate. By harnessing Redis's capabilities, we seek to showcase its potential as a reliable and efficient in-memory database solution within the context of machine learning-driven natural language processing tasks in a distributed computing environment where the model can be re-trained on new sets of data on the fly minimizing further tweaks and manual configurations by end users and engineers.

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
`sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1`
  - You can then confirm that Python was installed by looking at the python version `python --version` should give `Python 3.xxx`
- Install Jupyter notebook with the following command:
`pip install jupyterlab`
- Install docker: https://docs.docker.com/engine/install/ubuntu/
- Reset your shell to take the new `$PATH` into account.

## Project setup
- Clone the repository

### Setting up the database
- Install python dependencies using pip `pip install -r requirements.txt`
- Download training data using the `sh ./get_data.sh` script; this will download the data files for the ML modles into the `data/` folder.
- Start docker service `sudo service docker start`
- Start the docker database using the `sh ./start_redis.sh`

### Setting up the Jupyter environment
- Run `jupyter-lab` from the project repository, navigate to the `notebook-dataprep.ipynb` file.
- Read through the Notebook and execute every cell, two new files should be created after in the `data/test_cleaned.csv` and `data/train_cleaned.csv`.
- Fill the database with training and testing data using `python fill_db.py`.
- Start executing cells within the Jupyter notebook.