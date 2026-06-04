from routes import app
from models import db
from models.course import Course, Lesson

with app.app_context():
    db.create_all()
    math = Course(title='Математика — ҰБТ дайындық', subject='math',
                  description='ҰБТ-ға арналған математика курсы. Алгебра, геометрия, логарифм.')
    inf = Course(title='Информатика — ҰБТ дайындық', subject='informatics',
                 description='ҰБТ-ға арналған информатика курсы. Алгоритм, Python, сандар жүйесі.')
    db.session.add_all([math, inf])
    db.session.commit()

    lessons = [
        Lesson(title='1-сабақ: Алгебра', youtube_url='https://youtube.com/watch?v=example1', course_id=math.id, order=1),
        Lesson(title='2-сабақ: Геометрия', youtube_url='https://youtube.com/watch?v=example2', course_id=math.id, order=2),
        Lesson(title='1-сабақ: Алгоритм', youtube_url='https://youtube.com/watch?v=example3', course_id=inf.id, order=1),
        Lesson(title='2-сабақ: Python', youtube_url='https://youtube.com/watch?v=example4', course_id=inf.id, order=2),
    ]
    db.session.add_all(lessons)
    db.session.commit()
    print("Деректер қосылды!")
