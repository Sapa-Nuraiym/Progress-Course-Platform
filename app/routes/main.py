from flask import Blueprint, render_template
from flask_login import login_required
from models.course import Course

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/courses')
@login_required
def courses():
    math_courses = Course.query.filter_by(subject='math').all()
    inf_courses = Course.query.filter_by(subject='informatics').all()
    return render_template('courses.html', math_courses=math_courses, inf_courses=inf_courses)

@main.route('/course/<int:course_id>')
@login_required
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course_detail.html', course=course)

@main.route('/help')
def help():
    return render_template('help.html')
