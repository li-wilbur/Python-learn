import sqlite3,sys


# 数据库连接
def opendb():
    conn = sqlite3.connect("mydb.db")
    cur = conn.execute(
        "create table if not exists tongxunlu(usernum integer primary key ,username varchar(128),passworld varchar(128),address varchar(125),telnum varchar(128))")
    return cur, conn


# 查询全部信息
"""def showalldb():
    print("----------------处理后数据-------------")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxunlu")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h),
        print()
    cur.close()"""


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
    hel[1].execute("insert into tongxunlu(usernum,username,passworld,address,telnum) values(?,?,?,?,?)",
                   (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print("==================数据添加完成！==========")
    showalldb()
    hel[1].close()


# 删除数据库内容
def deldb():
    print("==============删除同学============")
    hel = opendb()
    delchoice = input("请输入想要删除的学号或者名字")
    if isinstance(delchoice, int):
        hel[1].execute("delete from tongxunlu where usernum = " + delchoice)
    else:
        hel[1].execute("delete from tongxunlu where username = " + delchoice)

    hel[1].commit()
    print("================数据删除完成========")
    showalldb()
    hel[1].close()


# 修改数据库内容
def alter():
    print("=========修改同学========")
    changechoice = input("请输入想要修改学生的学号")
    hel = opendb()
    person = intoinfo()
    hel[1].execute(
        "update tonxunlu set usernum=?,username=?,passworld=?,address=?,telnum=?, where usernum=" + changechoice,
        (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    showalldb()
    hel[1].close()


# 查询数据
def searchdb():
    print("==========查询数据库========")
    choice = input("请输入查询的学号：")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxunlu where usernum=" + choice)
    hel[1].commit()
    print("----------查询结果如下----------")
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    hel[1].close()


#是否继续进行操作的判断
def cont():
    choice = input("选择是否要进行操作。(y or n)")
    if choice == 'y':
        return 1
    else:
        sys.exit()


# 程序
if __name__ == "__main__":
    #while cont() == 1:
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
