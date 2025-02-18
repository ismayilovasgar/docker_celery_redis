pip freeze > requirements.txt 
chmod +x ./entyrpoint.sh  
http://0.0.0.0:8000  
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh
