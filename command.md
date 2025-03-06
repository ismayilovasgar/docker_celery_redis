pip freeze > requirements.txt 
chmod +x ./entyrpoint.sh  
http://0.0.0.0:8000  
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh


tp1.delay()

from celery import group
from newapp.tasks import *


<!-- Group -->
task_group = group(tp1.s(),tp2.s(),tp3.s(),tp4.s())
task_group.apply_async() 

result =  group(tp1.s(),tp2.s(),tp3.s(),tp4.s())()
print(result.get()) # => [ "tp1","tp2","tp3","tp4" ]
<!--  -->

<!-- Chain -->
task_chain = chain( tp1.s(),tp3.s(),tp2.s())