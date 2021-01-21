import pymysql
database=pymysql.connect(host='localhost', user='root', password='', db='foodplaza', port=3308)
c=database.cursor()
