import sqlite3, sys, os


# 数据库连接
def opendb():
    conn = sqlite3.connect("mydb.db")
    cur = conn.execute(
        "CREATE TABLE IF NOT EXISTS tongxunlu(userid integer primary key ,username varchar(128),password varchar(128),address varchar(125),telnum varchar(128))")
    return cur, conn


# 查询全部信息
def showalldb():
    print("----------------处理后数据-------------")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("SELECT * FROM tongxunlu")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h),
        print()
    cur.close()


# 输入信息

def intoinfo():
    usernum = input("请输入学号")
    username1 = input("请输入姓名")
    password1 = input("请输入密码")
    address1 = input("请输入地址:")
    telnum1 = input("请输入联系方式：")
    return usernum, username1, password1, address1, telnum1


# 添加信息到数据库
def addinfo():
    welcome = "==============欢迎新同学=============="
    print(welcome)
    person = intoinfo()
    hel = opendb()
    hel[1].execute("INSERT INTO tongxunlu(userid,username,password,address,telnum) VALUES(?,?,?,?,?)",
                   (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print("==================数据添加完成！==========")
    showalldb()
    hel[1].close()


# 删除数据库内容
def deldb():
    print("==============删除同学============")
    hel = opendb()
    delchoice = input("请输入想要删除的学号")
    if isinstance(int(delchoice),int):
        hel[1].execute("DELETE FROM tongxunlu WHERE userid = " + delchoice)
        hel[1].commit()
        print("================数据删除完成========")
        showalldb()
        hel[1].close()
    else:
        print("请输入学号！")
        deldb()


# 修改数据库内容
def alter():
    print("=========修改同学========")
    changechoice = input("请输入想要修改学生的学号")
    if isinstance(int(changechoice),int):
        hel = opendb()
        person = intoinfo()
        #hel[1].execute("insert into tongxunlu(usernum,username,passworld,address,telnum) values({0},'{1}','{2}','{3}','{4}') where usernum= {5}".format(person[0],person[1],person[2],person[3],person[4],changechoice))
        hel[1].execute("UPDATE tongxunlu SET userid=?,username=?,password=?,address=?,telnum=? WHERE userid=" + changechoice,(person[0], person[1], person[2], person[3], person[4]))
        hel[1].commit()
        showalldb()
        hel[1].close()
    else:
        print("请正确输入学号！")
        alter()


# 查询数据
def searchdb():
    print("==========查询数据库========")
    choice = input("请输入查询的学号：")
    if isinstance(int(choice),int):
        hel = opendb()
        cur = hel[1].cursor()
        cur.execute("SELECT * FROM tongxunlu WHERE userid=" + choice)
        hel[1].commit()
        print("----------查询结果如下----------")
        for row in cur:
            print("学号：{}，  姓名：{},   密码：{},   地址：{},   联系方式：{}".format(row[0],row[1],row[2],row[3],row[4]))
            #print(row[0], row[1], row[2], row[3], row[4])
        cur.close()
        hel[1].close()
    else:
        print("请输入正确学号!")
        searchdb()

#是否继续进行操作的判断
#option = [1]
def cont():
    choice = input("选择是否要继续进行操作。(y or n)")
    if choice == 'y' or choice == "Y":
        pass
    elif choice == "n" or choice == "N":
        print("Goodbye!")
        sys.exit()
    else:
        print("您的输入有误，请输入‘y’或者‘n’！（不区分大小写）")
        cont()


# 程序
if __name__ == "__main__":
    while True:
        print("=================欢迎使用通讯录=================")
        choiceshow = """
        请选择您的进一步选择：
        （添加）往数据库添加数据
        （删除）删除数据库中的数据
        （修改）修改数据库中的数据
        （查询）查询数据库中的数据
        （退出）退出数据库操作
        选择你要进行的操作：
        """
        choice = input(choiceshow)
        if choice == "添加":
            addinfo()
            cont()
        elif choice == "删除":
            deldb()
            cont()
        elif choice == "修改":
            alter()
            cont()
        elif choice == "查询":
            searchdb()
            cont()
        elif choice == "退出":
            print("Goodbye!")
            sys.exit()
        else:
            print("输入的操作有误，重新输入！")
            os.system("python class.py")