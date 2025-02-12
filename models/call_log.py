from app.utils.database import db

class CallLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caller_number = db.Column(db.String(20), nullable=False)
    call_time = db.Column(db.DateTime, nullable=False, default=db.func.now())
    transcript = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
