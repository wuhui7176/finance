import mysql.connector

# mysql1.py
config = {
    'host': '47.52.162.85',
    'user': 'root',
    'password': '717615657',
    'port': 3306,
    'database': 'finance',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    # sql_query = 'select id,name from plate ;'
    sql_query = 'insert into plate (name) VALUE(%s)'
    param = ('yangguo')

    s = cursor.execute(sql_query, ['333'])
    cnn.commit()
    # for name, age in cursor:
    #     print (name, age)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()