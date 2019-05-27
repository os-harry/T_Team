from flask import Flask, render_template, request, make_response, send_file ,jsonify
from models import Admin, Student, Project, Users , Team , Class , ClassHasStu
from exts import db
import config, os
from methods import  get_Info, to_Data, to_List, to_Json, new_avatar_name, create_xlsx
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials = True) # 解决跨域问题

app.config.from_object(config)
db.init_app(app)

url = "http://127.0.0.1:5000/"
@app.before_first_request
def init_db():
    print ('>>>>>>>>creating DB...')
    db.create_all()

"http://127.0.0.1:5000/test"
@app.route('/test')
def test():
    # data = to_Data()
    print ('>>>>>in test')
    # print (data)
    return (">>>>>get it!")

@app.route('/classList', methods=['POST','GET'])
def classList():
    # data = to_Data()
    data = 'in classList<<<<'
    print(data)
    print ('>>>>>in classList')
    # print (data)
    classListData = {
        'state': 0,
        'student_info' : 'studentInfo',
        'classes' : 'classes'
    }
    return jsonify(classListData)

@app.route('/')
def index():
    #return render_template('index.html')
    return ("首页")

@app.route('/login', methods=['POST','GET']) # 登录
def login():
    data = to_Data()
    account = data['account']
    password = data['password']

    if account and password:
        admin = Admin.query.filter(Admin.Adminaccount == account, Admin.Password == password).first()
        if admin:
            return ("1")
    return ("0")

@app.route('/by_input', methods = ['POST','GET']) # 按输入查询
def by_input():
    data = to_Data() # 将json转为字典
    input = data['input']
    page = data['page']
    if input and page:
        info = get_Info(input = input) #从数据库获取成员信息
        list = to_List(info, page) #将数据转为列表
        data = to_Json(list) #将列表数据转为json
        return data
    return ("0")


@app.route('/by_name', methods = ['POST']) # 按姓名查询
def by_name():
    data = to_Data()
    sname = data['name']
    page = data['page']
    if sname and page:
        info = get_Info(sname = sname)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_group', methods = ['POST']) # 按组别查询
def by_group():
    data = to_Data()
    group = data['group']
    page = data['page']
    if group and page:
        info = get_Info(group = group)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_grade', methods = ['POST']) # 按年级查询
def by_grade():
    data = to_Data()
    grade = data['grade']
    page = data['page']
    if grade and page:
        info = get_Info(grade = grade)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_name_group', methods=['POST']) # 按姓名、组别查询
def by_name_group():
    data = to_Data()
    sname = data['name']
    group = data['group']
    page = data['page']
    if sname and group and page:
        info = get_Info(sname = sname, group = group)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_name_grade', methods=['POST']) # 按姓名、年级
def by_name_grade():
    data = to_Data()
    sname = data['name']
    grade = data['grade']
    page = data['page']
    if sname and grade and page:
        info = get_Info(sname = sname, grade = grade)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_group_grade', methods=['POST']) # 按组别、年级
def by_group_grade():
    data = to_Data()
    group = data['group']
    grade = data['grade']
    page = data['page']
    if group and grade and page:
        info = get_Info(group = group, grade = grade)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/by_name_group_grade', methods=['POST']) # 按姓名、组别、年级查询
def by_name_group_grade():
    data = to_Data()
    sname = data['name']
    group = data['group']
    grade = data['grade']
    page = data['page']
    if sname and group and grade and page:
        info = get_Info(sname = sname, group = group, grade = grade)
        list = to_List(info, page)
        data = to_Json(list)
        return data
    return ("0")

@app.route('/up/image', methods=['POST']) # 上传头像
def up_image():
    sno = request.form.get('sno')
    # sno = "20182109xxxx"
    avatar = request.files['image_data'] # 上传图片数据名
    if sno and avatar:
        student = Student.query.filter(Student.SNo == sno).first()  # 查找相应成员
        if student:
            basedir = os.path.dirname(__file__) # 运行路径
            avatar_path = os.path.join(basedir, 'static\image', new_avatar_name(avatar.filename)) # 重命名后合成文件在服务器的路径
            avatar_path = avatar_path.replace('\\','/') # 若不换成/ Linux服务器会报错  位置:static/image/*.jpg
            avatar.save(avatar_path) # 保存文件
            avatar_url = url + avatar_path # 合成头像访问路径

            old_url = student.Avatar
            if old_url: # 判断是否存在，若存在删除存储的旧头像
                old_url = old_url.replace(url,'') # 除去路径中的url
                os.remove(old_url)

            student.Avatar = avatar_url # 将链接存储在数据库
            db.session.add(student)
            db.session.commit()
            return ("1")
    return ("0")

@app.route('/add_change/info', methods=['POST']) # 添加或修改成员数据
def add_change_info():
    data = to_Data()
    sno = data['sno']
    avatar = url + "static/image/0.png" # 默认头像
    sname = data['name']
    grade = data['grade']
    group = data['group']
    ID = data['ID']  # 从前端获取得需要修改数据项目的ID列表
    state = data['state'] # 添加或修改
    data_pro = data['project_arr']

    telephone = data['contact']['phone']
    wechat = data['contact']['wx']
    qq = data['contact']['qq']
    mailbox = data['contact']['email']
    other = data['contact']['other']

    occupation = data['graduation']['job']
    workaddress = data['graduation']['address']
    direction = data['graduation']['study']

    if sno and sname and grade and group:
        if state == 0: # 修改
            student = Student.query.filter(Student.SNo == sno).first()
            # student.SNo = sno # 学号作为主键不可更改
            student.SName = sname
            student.Group = group
            student.Grade = grade
            student.Telephone = telephone
            student.WeChat = wechat
            student.QQ = qq
            student.MailBox = mailbox
            student.Other = other
            student.Occupation = occupation
            student.WorkAddress = workaddress
            student.Direction = direction
            db.session.add(student) # 修改成员数据
            db.session.commit() # 提交

            for data in data_pro:
                if data['ID'] == 0:
                    project = data['name']
                    award = data['prize']
                    code = data['code']
                    project = Project(SNo=sno, Project=project, Award=award, Code=code)
                    db.session.add(project)  # 添加项目数据
                    db.session.commit()
            if ID:
                for id in ID:
                    project = Project.query.filter(Project.ID == id).first()
                    if project:
                        for data in data_pro:
                            if data['ID'] == id:
                                project.Project = data['name']
                                project.Award = data['prize']
                                project.Code = data['code']
                                db.session.add(project) # 修改项目数据
                                db.session.commit()
            return ("1")

        elif state == 1: # 增加
            student = Student.query.filter(Student.SNo == sno).first()
            if not student:
                student = Student(SNo=sno, Avatar=avatar, SName=sname, Grade=grade, Group=group, Telephone=telephone, WeChat=wechat,
                                  QQ=qq, MailBox=mailbox, Other=other, Occupation=occupation, WorkAddress=workaddress, Direction=direction)
                db.session.add(student) # 添加成员数据
                db.session.commit() # 提交
                for data in data_pro:
                    project = data['name']
                    award = data['prize']
                    code = data['code']
                    project = Project(SNo=sno, Project=project, Award=award, Code=code)
                    db.session.add(project) # 添加项目数据
                    db.session.commit()
                return ("1")
            return ("0") # 成员已经存在
    return ("-1") # 学号、姓名不能为空

@app.route('/delete/info', methods = ['POST']) # 删除成员
def delete_info():
    data = to_Data()
    sno = data['sno']
    if sno:
        student = Student.query.filter(Student.SNo == sno).first()
        if student:
            old_url = student.Avatar
            if old_url:  # 删除存储在服务器的头像
                old_url = old_url.replace(url, '')  # 除去路径中的url
                os.remove(old_url)
            Student.query.filter(Student.SNo == sno).delete() # 删除
            db.session.commit()
            return ("1")
    return ("0")

@app.route('/delete/pro', methods=['POST']) # 删除项目
def delete_pro():
    data = to_Data()
    ID = data['ID']
    if ID:
        Project.query.filter(Project.ID == ID).delete()
        db.session.commit()
        return ("1")
    return ("0")


if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port = 80) # 若要配置在服务器上
    app.run()