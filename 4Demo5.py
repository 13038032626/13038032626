import pymssql
#conn=pymssql.connect(server='localhost',database='pxscj1',charset='gbk')
conn=pymssql.connect(server='LAPTOP-RC5R3RTM',user='sa',password='wsl13038',database='pxscj1',charset='cp936')  #gbk的code page是cp936
if conn:
    print('连接成功')

#查询
cursor=conn.cursor()
sql_select='select * from xsb'
cursor.execute(sql_select)
results=cursor.fetchall()
#print(results)    #result 是列表，其中单个元素是由数据库一行所构成的元组（怪不得也叫元组）
for result in results:
    result=list(result)
    for res in range(len(result)):
        if isinstance(result[res],str):   #原本输出，在汉字字符串（汉字char）存在空格
            result[res]=result[res].replace(' ','')
    result=tuple(result)
    print(result)  #输出格式和sql中不同，datetime型
conn.commit()
conn.close()
#插入
cursor=conn.cursor()
sql_insert="insert into xsb values(191318,'马原原',True,datetime,'2001-01-01','通信工程',48,none)" #注意外层两个引号内层才能一个
cursor.execute(sql_insert)
conn.commit()
conn.close()
#更新
cursor=conn.cursor()
sql_update="update xsb set 专业='通信工程' where 学号='131317'"
cursor.execute(sql_update)
conn.commit()
conn.close()

#删除
cursor=conn.cursor()
sql_delete="delete from xsb where 学号='221316'"
cursor.execute(sql_delete)
conn.commit()
conn.close()
