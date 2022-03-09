from flask import Flask, request, render_template, flash, redirect
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptionAgency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "OOooOOOoOOOoo000"

connect_db(app)

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)


"new pet form"
@app.route('//new-pet', methods=['GET', 'POST'])
def new_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        "Get all form values"
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        avalible = form.avalible.data
        "Create new pet and add to db"
        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes,avalible=avalible)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        "If form isnt valid, return to the page"
        return render_template('new-pet.html', form=form)


"View a pets details"

@app.route('/view/<int:user_id>')
def view_pet(user_id):
    pet = Pet.query.get_or_404(user_id)
    return render_template('view-pet.html',pet=pet)


"edit Pet"
@app.route('/edit/<int:user_id>', methods=["GET", "POST"])
def edit_pet(user_id):
    pet = Pet.query.get_or_404(user_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        "Get all form values"
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.avalible = form.avalible.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit-pet.html',pet=pet, form=form)




