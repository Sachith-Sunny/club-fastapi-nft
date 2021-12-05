This project aims at creating a fantasy club for players. A user registers and creates players for his team or club.
Then these players could be exchanged among the users in the platform.


Setup

set a virtual environment first

python3 -m venv .venv
source .venv/bin/activate

install the dependencies in the requirements file by 

pip install -r requirements.txt


to start server using uvicorn
cd app
uvicorn main:app --reload