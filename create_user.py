import pymysql
from werkzeug.security import generate_password_hash

# Replace these with your own database details
# connection = pymysql.connect(
#     host='localhost',
#     user='your_mysql_username',         # change this!
#     password='your_mysql_password',     # change this!
#     database='shose_website_1'
# )

connection = pymysql.connect(
    host='localhost',
    user='root',                  # or the username you use for MySQL Workbench
    password='Gayatri@25',      # the password you use to sign in to MySQL
    database='shose_website_1'
)



username = 'testuser'
email = 'test@example.com'
raw_password = 'testpass'
password_hash = generate_password_hash(raw_password)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, password_hash))
    connection.commit()
    print("Test user created successfully!")
finally:
    connection.close()
