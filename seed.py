from flask import session
from models import db, connect_db, Pet
from app import app

db.drop_all()
db.create_all()

hamster_url = 'https://forum.playhive.com/uploads/default/original/3X/2/8/287d5799f3709607be5561a7bdf6af3314df5a7f.png'
mars_url = 'https://cdn.discordapp.com/attachments/951202672722214976/951203946259693588/B58EAC05-2916-419F-8F4C-CA510BA1CEA9.jpg'
funko_url='https://cdn.discordapp.com/attachments/951202672722214976/951202746210590740/7E28CF00-3212-4F20-881E-D06B7E117DB6.jpg'
xxxdog_url='https://community.custom-cursor.com/uploads/default/original/3X/4/8/481a9720d41284112e77ca2c216d88e347bf1afb.jpeg'
gus_url = 'https://cdn.discordapp.com/attachments/951202672722214976/951204203886415882/IMG_7620.jpg'

mars = Pet(name='Mars', species='cat',photo_url=mars_url, age=4, notes='Annoying')
gus = Pet(name='Gus', species='cat',photo_url=gus_url, age=1, notes='fluffy')

penny = Pet(name='Penny', species='dog', age=6, notes='dumb and fluffy')
xxxdog = Pet(name='XXXDOG', species='dog',photo_url=xxxdog_url, age=41, notes='old, annoying, and smelly', avalible=False)
hammy = Pet(name='Hammy', species='hamster',photo_url=hamster_url , age=1, notes='Funky', avalible=True)
funko = Pet(name='Funko', species='cat',photo_url=funko_url , age=999, notes='Funky', avalible=True)







db.session.add(mars)
db.session.add(gus)
db.session.add(xxxdog)
db.session.add(hammy)
db.session.add(funko)





db.session.commit()
