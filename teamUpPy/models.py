from exts import db

class Admin(db.Model):
    __tablename__ = 'admin'
    Adminaccount = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True)
    Password = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)

class Project(db.Model):
    __tablename__ = 'project'
    ID = db.Column(db.Integer, primary_key=True)
    SNo = db.Column(db.ForeignKey('student.SNo', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Project = db.Column(db.String(255))
    Award = db.Column(db.String(255))
    Code = db.Column(db.String(255))
    student = db.relationship('Student', primaryjoin='Project.SNo == Student.SNo', backref='projects')

class Student(db.Model):
    __tablename__ = 'student'
    SNo = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True, index=True)
    Avatar = db.Column(db.String(255, 'utf8_general_ci'), index=True)
    SName = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    Grade = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    Group = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    Telephone = db.Column(db.String(255, 'utf8_general_ci'))
    WeChat = db.Column(db.String(255, 'utf8_general_ci'))
    QQ = db.Column(db.String(255, 'utf8_general_ci'))
    MailBox = db.Column(db.String(255, 'utf8_general_ci'))
    Other = db.Column(db.String(255, 'utf8_general_ci'))
    Occupation = db.Column(db.String(255, 'utf8_general_ci'))
    WorkAddress = db.Column(db.String(255, 'utf8_general_ci'))
    Direction = db.Column(db.String(255, 'utf8_general_ci'))

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True, index=True)
    name = db.Column(db.String(255, 'utf8_general_ci'),nullable=False)
    weChatId = db.Column(db.String(255, 'utf8_general_ci'),nullable=False)
    Sno = db.Column(db.String(255, 'utf8_general_ci'),nullable=False)
class Class(db.Model):
    '''
    id（可做邀请码）
    名称
    队伍人数上限
    管理密码
    '''
    __tablename__ = 'class'
    id = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True, index=True)
    name = db.Column(db.String(255, 'utf8_general_ci'),nullable=False)
    limit = db.Column(db.Integer)
    pwd = db.Column(db.String(255, 'utf8_general_ci'),nullable=False)

class Team(db.Model):
    '''
    id
    队长id
    队伍已有人数
    班级_id
    队伍满员标记
    信息 /255
    '''
    __tablename__ = 'team'
    id = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True, index=True)
    cap = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('users.id'))
    # user_id = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('users.id'))
    class_id = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('class.id'))
    full = db.Column(db.Integer)
    msg =  db.Column(db.String(255, 'utf8_general_ci'))


class ClassHasStu(db.Model):
    '''
    id
    班级id
    学生id
    队伍id
    '''
    __tablename__ = 'class_has_stu'
    id = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True, index=True)
    class_id = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('class.id'))
    user_id = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('users.id'))
    team_id = db.Column(db.String(255, 'utf8_general_ci'), db.ForeignKey('team.id'))
