from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User, Post, Permission, Comment
from .forms import ProfileForm,PostForm,CommentForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Post(body=post_form.body.data,author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', post_form=post_form, posts=posts)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    profile_form = ProfileForm()
    if profile_form.validate_on_submit():
        current_user.about_me = profile_form.about_me.data 
        db.session.add(user)
        db.session.commit()
        flash('Your Profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    profile_form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', profile_form=profile_form)

@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(body=comment_form.body.data,
                          post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published.')
        return redirect(url_for('.index', id=post.id))
    return render_template('comment.html', post=post, comment_form=comment_form)
