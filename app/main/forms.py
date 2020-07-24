from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ProfileForm(FlaskForm):
    about_me = TextAreaField('About me', validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = StringField('', validators=[Required()])
    submit = SubmitField('Submit')