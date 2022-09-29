#GİTHUB REPODAN PROJE ÇEKİNCE YAPILACAK ADIMLAR
1-python -m venv env
2-env/Scripts/activate
3-pip install -r requirements.txt
4-python.exe -m pip install - upgrade pip
5-pip install python-decouple
6-pip freeze > requirements.txt
7-python manage.py migrate
8-python manage.py createsuperuser
9-python manage.py runserver

web scraping nedir araştır. seleniumla yapılıyor...bize kaynaklarını paylaşmayan uygulamalardan da veri çekebiliyoruz bu yöntemle... pythonun da kütüphanesi var beautifulsoup adında..

api ile ilişki kurmak için requests kullandım. önce pip install requests yapıyoruz. sonra import requests...

url den gelen json formatındaki veriyi .json() kullanarak python dictionary formatına çevirebiliriz... pprint i pprint ten import ederek python dictionary formatındaki veriyi daha düzenli okuyabiliriz..

