from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.course import Course

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def my_profile():
    return render_template('profile.html', user=current_user)

@profile.route('/enroll/<int:course_id>')
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    if course not in current_user.enrolled_courses:
        current_user.enrolled_courses.append(course)
        db.session.commit()
        flash(f'"{course.title}" курсына тіркелдіңіз!', 'success')
    return redirect(url_for('main.courses'))

@profile.route('/unenroll/<int:course_id>')
@login_required
def unenroll(course_id):
    course = Course.query.get_or_404(course_id)
    if course in current_user.enrolled_courses:
        current_user.enrolled_courses.remove(course)
        db.session.commit()
        flash('Курстан шықтыңыз.', 'info')
    return redirect(url_for('profile.my_profile'))

# Профильді өңдеу (UPDATE)
@profile.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if not name or len(name) < 2:
            flash('Аты-жөні кемінде 2 әріп болуы керек!', 'error')
            return redirect(url_for('profile.edit_profile'))
        current_user.name = name
        db.session.commit()
        flash('Профиль жаңартылды!', 'success')
        return redirect(url_for('profile.my_profile'))
    return render_template('edit_profile.html', user=current_user)

# Аккаунтты өшіру (DELETE)
@profile.route('/profile/delete', methods=['POST'])
@login_required
def delete_account():
    user = current_user
    logout_user()
    db.session.delete(user)
    db.session.commit()
    flash('Аккаунт өшірілді.', 'info')
    return redirect(url_for('main.index'))