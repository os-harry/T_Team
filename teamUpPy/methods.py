from flask import request
import json, re, datetime, random, os
from models import Student, Project
from werkzeug.utils import secure_filename
import xlwt # 向excel表格写数据的库

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
def get_Info(sname = None, group = None, grade = None, input = None):
    info = None
    if sname:
        sname = re.sub(' ', "", sname) # 除去空格
        sname = re.sub('\d+', "", sname) # 提取姓名

    if sname and group and grade:
        info = Student.query.filter(Student.SName == sname, Student.Group == group, Student.Grade == grade).all()
        if not info: # 模糊查询
            sname = "%" + sname + "%" # 模糊条件
            info = Student.query.filter(Student.SName.like(sname)).all()
    elif sname and group:
        info = Student.query.filter(Student.SName == sname, Student.Group == group).all()
        if not info: # 模糊查询
            sname = "%" + sname + "%" # 模糊条件
            info = Student.query.filter(Student.SName.like(sname)).all()
    elif sname and grade:
        info = Student.query.filter(Student.SName == sname, Student.Grade == grade).all()
        if not info: # 模糊查询
            sname = "%" + sname + "%" # 模糊条件
            info = Student.query.filter(Student.SName.like(sname)).all()
    elif group and grade:
        info = Student.query.filter(Student.Group == group, Student.Grade == grade).all()
    elif sname:
        info = Student.query.filter(Student.SName == sname).all()
        if not info: # 模糊查询
            sname = "%" + sname + "%" # 模糊条件
            info = Student.query.filter(Student.SName.like(sname)).all()
    elif group:
        info = Student.query.filter(Student.Group == group).all()
    elif grade:
        info = Student.query.filter(Student.Grade == grade).all()

    elif input:
        input = re.sub(' ', "", input) # 除去空格
        # 输入条件为学号查询
        input_sno = re.sub('\D', "", input) # 提取数字
        if len(input_sno) > 6:
            info = Student.query.filter(Student.SNo == input_sno).all()
            if not info:
                input_sno = "%" + input_sno + "%"
                info = Student.query.filter(Student.SNo.like(input_sno)).all()

        if not info:
            # 为姓名查询
            input_name = re.sub('\d+',"",input) # 提取姓名
            if len(input_name) >= 1: # 存在
                info = Student.query.filter(Student.SName == input_name).all()
                if not info: # 模糊查询
                    input_name = "%" + input_name + "%"
                    info = Student.query.filter(Student.SName.like(input_name)).all()

        if not info:
            # 为组别
            input_group = re.sub('\d+', "", input)  # 提取组别
            if len(input_group) >= 1:  # 存在
                info = Student.query.filter(Student.Group == input_group).all()
                if not info: # 模糊查询
                    input_group = "%" + input_group +"%"
                    info = Student.query.filter(Student.Group.like(input_group)).all()

        if not info:
            # 为年级查询
            input_grade = re.sub('\D',"",input) # 提取年级
            if 4 >= len(input_grade) >= 2:# 存在
                info = Student.query.filter(Student.Grade == input_grade).all()
                if not info:
                    input_grade = "%" + input_grade + "%"
                    info = Student.query.filter(Student.Grade.like(input_grade)).all()
        if not info:
            info = []
    return info

def to_Data():
    data = request.get_data()  # 获取前端数据
    print(request.get_data(),'1')
    data = str(data, 'utf-8')  # 转utf-8
    print(request.get_data(), '2')
    data = json.loads(data)  # json转字典
    print(request.get_data(), '3')
    print(request.get_data())
    # data = json.loads(request.get_data().decode("utf-8"))
    if data:
        return data
    else:
        return {}

def to_Json(list = None):
    if list:
        data = json.dumps(list, ensure_ascii = False)
    else:
        data = "0"
    return data

def to_List(info, page): # page为页数
    list = []
    limit = 10 # 限制返回数据条数
    index = len(info)  # 行索引
    for row in range(index):
        dic_stu = {
            'sno': info[row].SNo,
            'image_url':info[row].Avatar,
            'name': info[row].SName,
            'grade': info[row].Grade,
            'group': info[row].Group,
            'contact':{
                'phone': info[row].Telephone,
                'wx': info[row].WeChat,
                'qq': info[row].QQ,
                'email': info[row].MailBox,
                'other': info[row].Other
            },
            'graduation':{
                'job': info[row].Occupation,
                'address': info[row].WorkAddress,
                'study': info[row].Direction
            },
        }

        list_pro = []
        pro_info = Project.query.filter(Project.SNo == info[row].SNo).all()
        for row_ in range(len(pro_info)):
            dic_pro = {
                'ID':pro_info[row_].ID,
                'name': pro_info[row_].Project,
                'prize': pro_info[row_].Award,
                'code': pro_info[row_].Code
            }
            list_pro.append(dic_pro)
        dic_stu['project_arr'] = list_pro

        list.append(dic_stu) # 合并

    total = limit * page

    list = list[total-limit:total] # 索引，位置
    return list

def new_avatar_name(avatar_name):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    rand_num = random.randint(10,99) # 随机10到99
    name = secure_filename(avatar_name)
    ext = name.rsplit('.', 1)[1]  # 扩展名
    avatar_name = str(now_time) + str(rand_num) + '.' + ext # 合成
    return avatar_name

def create_xlsx(info):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('新思路成员信息一览表', cell_overwrite_ok = True)

    alignment = xlwt.Alignment()  # 对齐格式
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  #

    font = xlwt.Font() # 字体
    font.bold = True # 设置黑体

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 27 # 浅色

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN # THIN:实线  NO_LINE:无  DASHED:虚线
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    borders_ = xlwt.Borders()
    borders_.bottom = xlwt.Borders.THIN

    tall = xlwt.easyxf('font:height 700;')
    worksheet.row(0).set_style(tall)
    tall = xlwt.easyxf('font:height 360;')
    worksheet.row(1).set_style(tall)
    tall = xlwt.easyxf('font:height 360;')
    worksheet.row(2).set_style(tall)

    worksheet.col(0).width = 256*13 # 学号
    worksheet.col(4).width = 256*12 # 电话
    worksheet.col(5).width = 256*12 # 微信
    worksheet.col(6).width = 256*12 # QQ
    worksheet.col(7).width = 256*18 # 邮箱
    worksheet.col(10).width = 256*15 # 地址
    worksheet.col(11).width = 256*27 # 方向
    worksheet.col(13).width = 256*25
    worksheet.col(14).width = 256*25
    worksheet.col(15).width = 256*25
    worksheet.col(16).width = 256*25
    worksheet.col(17).width = 256*25

    style0 = xlwt.XFStyle()
    style0.alignment = alignment
    style0.font = font
    style0.pattern = pattern
    style0.borders = borders
    worksheet.write_merge(0, 0, 0, 17, 'New-Thread成员信息一览表', style0)

    style1 = xlwt.XFStyle()
    style1.alignment = alignment
    style1.font = font
    style1.borders = borders
    worksheet.write_merge(1, 1, 0, 3, '个人信息', style1)
    worksheet.write_merge(1, 1, 4, 8, '联系方式', style1)
    worksheet.write_merge(1, 1, 9, 11, '毕业去向(工作/研究生/留学生)', style1)
    worksheet.write_merge(1, 1, 12, 17, '参与项目', style1)

    style2 = xlwt.XFStyle()
    style2.alignment = alignment
    style2.borders = borders
    a = ['学号','姓名','年级','组别','电话','微信','QQ','邮箱','其它','职业','地址(工作单位)','研究方向(岗位/研究生技术方向)','-','项目1','项目2','项目3','项目4','项目5']
    for i in range(18):
        worksheet.write(2, i, a[i], style2)

    style3 = xlwt.XFStyle()
    style3.alignment = alignment
    style3.borders = borders
    if info:
        i = 3 # 控制行
        pi = 3
        for row in range(len(info)):
            stu_info = [info[row].SNo, info[row].SName, info[row].Grade, info[row].Group, info[row].Telephone, info[row].WeChat, info[row].QQ,
                    info[row].MailBox, info[row].Other, info[row].Occupation, info[row].WorkAddress, info[row].Direction]
            j = 0 # 控制信息列
            pj = 13 # 工程列
            for content in stu_info:
                worksheet.write_merge(i, i+2, j, j, content, style3) # 合并单元格参数(从0开始): 1-3行，0-0列，内容，格式
                j = j+1
                if j == 12:
                    break

            style4 = xlwt.XFStyle()
            style4.borders = borders_
            worksheet.write(i, 12, '项目名称')
            worksheet.write(i+1, 12, '获奖情况')
            worksheet.write(i+2, 12, '源码', style4)

            project = Project.query.filter(Project.SNo == info[row].SNo).all()
            for row in range(len(project)):
                pro_info = [project[row].Project, project[row].Award, project[row].Code]
                for content in pro_info:
                    worksheet.write(pi, pj, content, style3)
                    pi = pi+1 # 加行
                pj = pj + 1 # 加列
                pi = pi - 3 # 还是一个学生，所以回到这一次的初始行

            i = i + 3 # 隔行输出
            pi = pi + 3 # 下一初始行

        basedir = os.path.dirname(__file__)  # 运行路径
        excel_path = os.path.join(basedir, 'static', '成员信息一览表.xls')  # 重命名后合成文件在服务器的路径
        excel_path = excel_path.replace('\\', '/')  # 若不换成/ Linux服务器会报错  位置:static/*.xls
        workbook.save(excel_path)  # 写入

        return excel_path
