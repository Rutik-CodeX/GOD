from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    __tablename__ = 'employee'
    EMPID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    EName = db.Column(db.String(255))
    DOJRS = db.Column(db.String(255))
    DOJSIPL = db.Column(db.String(255))
    Profile = db.Column(db.String(255))
    Status = db.Column(db.String(50))
    SIPLLevel = db.Column(db.String(50))
    RSALevel = db.Column(db.String(50))
    EEMail = db.Column(db.String(255))
    IEMail = db.Column(db.String(255))
    Landline = db.Column(db.String(20))
    Mobile = db.Column(db.String(20))
    Ext = db.Column(db.String(10))
    Secretary = db.Column(db.String(255))
    SecretaryID = db.Column(db.String(255))
    SystemID = db.Column(db.String(255))
    Password = db.Column(db.String(255), nullable=False)
    Team = db.Column(db.String(255))
    LineManager = db.Column(db.String(255))
    LineManagerID = db.Column(db.String(255))

    def get_id(self):
        return self.EMPID

class TimesheetEntry(db.Model):
    __tablename__ = 'timesheet_entries'
    Uniq_ID = db.Column(db.String(50), primary_key=True)
    EName = db.Column(db.String(255), nullable=False)
    EmpID = db.Column(db.String(10), nullable=False)
    Team = db.Column(db.String(255), nullable=False)
    LineManager = db.Column(db.String(255), nullable=False)
    DateofEntry = db.Column(db.Date, nullable=False)
    StartTime = db.Column(db.String(255))
    EndTime = db.Column(db.String(255))
    Hours = db.Column(db.Float)
    Minutes = db.Column(db.Float)
    billable_time = db.Column(db.Float)
    nonbillable_admin_time = db.Column(db.Float)
    nonbillable_training_time = db.Column(db.Float)
    unavailable_time = db.Column(db.Float)
    total_time = db.Column(db.Float)
    AllocationType = db.Column(db.String(50))
    Category1 = db.Column(db.String(50))
    Category2 = db.Column(db.String(50))
    Category3 = db.Column(db.String(50))
    Category4 = db.Column(db.String(50))
    Category5 = db.Column(db.String(50))
    Category6 = db.Column(db.String(50))
    ProjectCode = db.Column(db.String(10), nullable=False)
    Comment = db.Column(db.String(255))
    Status = db.Column(db.String(20))
    SubmitDate = db.Column(db.Date, default=datetime.utcnow)
    LastUploadDate = db.Column(db.Date, onupdate=datetime.utcnow)
    LastUpdatedBy = db.Column(db.String(50))

    def __repr__(self):
        return f'<TimesheetEntry {self.Uniq_ID}>'
