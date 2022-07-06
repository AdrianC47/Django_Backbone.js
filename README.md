# Django_Backbone.js

Se plantea una arquitectura simple de los dos frameworks
Version python 3.9.7
IDE Pycharm
PostgreSQL
python -m pip install django
python.exe -m pip install psycopg2
pip install django-tastypie


Creamos un nuevo proyecto junto con un entorno virtual
instalamos lo siguiente
python -m pip install django
python -m pip install django-tastypie   
python.exe -m pip install --upgrade pip
se crea una carpeta personas_django al nivel del entorno
y en esa carpeta hacemos lo siguiente
django-admin startproject sap (ojo que nuestro proyecto es nuestro source root)
Dentro del sap crearemos las diferentes app
python manage.py startapp webapp (se configura los diferentes url y views) 
se configura  en settings la base de datos
python -m pip install psycopg2


#Ver las migraciones pendientes:
python manage.py showmigrations

#Aplicar las migraciones pendientes
python manage.py migrate

#buscamos las migraciones por hacer 
python manage.py makemigrations

#ver el sql a ejecutar
python manage.py sqlmigrate personas 0001


#crear la tabla y ver cómo se creó (prefijo)
python manage.py migrate