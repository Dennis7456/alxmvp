from turtle import position
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from hirehub import db
from hirehub.models import JobPost
from hirehub.jobposts.forms import JobPostForm

job_posts = Blueprint('job_posts', __name__)

@job_posts.route("/my_job_posts")
def my_job_posts():
    job_posts = JobPost.query.filter(user_id=current_user.owner)
    return render_template('job_posts.html', job_posts=job_posts)

@job_posts.route("/job_post/new", methods=['GET', 'POST'])
@login_required
def new_job_post():
    if current_user.role != 'recruiter':
        abort(401)
    form = JobPostForm()
    if form.validate_on_submit():
        job_post = JobPost(company_name=form.company_name.data, desired_major=form.desired_major.data, job_title=form.job_title.data, job_desc=form.job_desc.data, more_info_name=form.more_info_name.data, email=form.email.data, position=form.position.data)
        db.session.add(job_post)
        db.session.commit()
        flash('Your post has been created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_job_post.html', title='New Job Post', form=form, legend='New Job Post')



@job_posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@job_posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = JobPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@job_posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
