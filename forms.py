from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class ReviewPredictorForm(FlaskForm):
    review = StringField('Review')
    predict = SubmitField('PREDICT')