from models import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(50))
    description = db.Column(db.Text)
    lessons = db.relationship('Lesson', backref='course', lazy=True)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    youtube_url = db.Column(db.String(300))
    material_url = db.Column(db.String(300))
    order = db.Column(db.Integer, default=1)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))