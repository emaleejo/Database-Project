import mysql.connector as mc

# connection to server, and our tester schema
conn = mc.connect(user="admin", password="testpassword", host="softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com", database="tester")

cur = conn.cursor()

cur.execute("SELECT * FROM tester.book;")
result = cur.fetchall()

# Doing this will only grab the first row of table
# result = cur.fetchone()


# each line is saved as an element in a list. So output each on a line
for x in result:
    print(x)