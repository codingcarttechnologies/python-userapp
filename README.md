# python-userapp
A simple users app CRUD

To run this app on linux distribution of Ubuntu OS:
1) clone the app

2)Create a virtual environment using command :
virualenv name_of_environment

3)Activate the environment:
source name/bin/activate

4)Install the dependencies:
sudo pip install -r requirements.txt

5)Make databasse migrations:
  (i)sudo python manage.py makemigrations


  (ii)sudo python manage.py migrate

6)run the app:
sudo python manage.py runserver
