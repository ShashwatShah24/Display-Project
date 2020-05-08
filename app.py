# -*- coding: utf-8 -*-
# app.py
import datetime
from flask import Flask, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.mysql import TIME
from wtforms import Form, FieldList, FormField, IntegerField, StringField, \
        SubmitField
import sqlite3  

class StepForm(Form):
    """Subform.

    CSRF is disabled for this subform (using `Form` as parent class) because
    it is never used by itself.
    """
    Phase = StringField('Phase')
    AssignedDev = StringField('AssignedDev')

class MainForm(FlaskForm):
    """Parent form."""
    step01 = FieldList(
        FormField(StepForm),
        min_entries=1,
        max_entries=50
    )


# Create models
db = SQLAlchemy()


class Step01(db.Model):
    """Stores Feedback."""
    __tablename__ = 'Feedback'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    Lead = db.Column(db.String(100))
    Assigned_By = db.Column(db.String(100))
    Assigned_Date = db.Column(db.String(100))
    Devloper = db.Column(db.String(100)) 
    Description = db.Column(db.String(500))
    Submittiontime = db.Column(db.String(100))

def __init__(self, name):
   self.name = name


class Feedback01(db.Model):
    """Stores step01 of a step02."""
    __tablename__ = 'Steps_Table'

    id = db.Column(db.Integer, primary_key=True)
    Feedback_id = db.Column(db.Integer, db.ForeignKey('Feedback.id'))

    Phase = db.Column(db.String(100))
    AssignedDev = db.Column(db.String(100))

    # Relationship
    step02 = db.relationship(
        'Step01',
        backref=db.backref('step01', lazy='dynamic', collection_class=list)
    )



# Initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sosecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///q12.db'
db.init_app(app)
db.create_all(app=app)


@app.route('/', methods=['GET', 'POST'])
def index():
    now = datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M:%S")
    form = MainForm()
    MSG=""
    if form.validate_on_submit():
        # Create step02
        new_step02 = Step01(name=request.form.get("name"),Lead=request.form.get("Lead"),Assigned_By=request.form.get("Assigned_By"),Assigned_Date=request.form.get("Assigned_Date"),Devloper=request.form.get("Devloper"),Description=request.form.get("Description"),Submittiontime=now)

        db.session.add(new_step02)

        for feedback01 in form.step01.data:
            new_feedback01 = Feedback01(**feedback01)

            # Add to step02
            new_step02.step01.append(new_feedback01)

        #print(request.form)

        db.session.commit()
        MSG=" Thank you"
    Feedback = Step01.query
    print(Feedback)
    return render_template(
        'index.html',
        form=form,
        Feedback=Feedback,MSG=MSG
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8011,threaded=True)  
