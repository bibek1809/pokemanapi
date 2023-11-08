# pokemanapi
1. After Installation of required enviroment the system can be run using through reuirement.txt
:
python3 -m venv venv
source venv/bin/activate
pip3 install  -r requirement.txt

2. Setup postgresql 
setup using this link : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04
After that step 
	1. sudo -u postgres psql
	2. postgres=# create database mydb;
	3.postgres=# create user myuser with encrypted password 'mypass';
	4.postgres=# grant all privileges on database mydb to myuser;
	
3. setup .env file

4. run uvicorn main:app --reload in bash
5. The Api that are avaliable can be fetch through <url>/docs
6. All pokemons details can be fetched through <url>/api/v1/pokemons
7. Pokemon By params types can be fetched through <url>/api/v1/pokemons?params=<params>
8. Pokemon By name can be fetched through <url>/api/v1/pokemons?name=<name> 
9. Pokemon By name and by params can be fetched through <url>/api/v1/pokemons?name=<name>&params=<params>
