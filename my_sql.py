import pymysql
from config import *

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=name,
    cursorclass=pymysql.cursors.DictCursor
)
# with connection.cursor() as cur:
#     cur.execute("DROP TABLE `users`")

with connection.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS `users` ("
                "`id` INT AUTO_INCREMENT," 
                "`surname` VARCHAR(15)," 
                "`money` INT DEFAULT 0,"
                "PRIMARY KEY(id)"
                ")"
                )

with connection.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS `garage` ("
                "`id` INT AUTO_INCREMENT,"
                "`data_stopped` DATE,"
                "`liters` INT DEFAULT 0,"
                "`id_driver` INT,"
                "PRIMARY KEY(id)"
                ")"
                )

# with connection.cursor() as cur:
#     cur.executemany("INSERT INTO `garage` (data_stopped, liters, id_driver) VALUES" \
#                 "(%s, %s, %s)", (list_garage))
#     connection.commit()

# with connection.cursor() as cur:
#     cur.executemany("UPDATE `users` SET `money` = %s WHERE `id` = %s", (update_users))
#     connection.commit()

# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM `users`")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
# with connection.cursor() as cur:
#     cur.execute('INSERT INTO `users`(name, age) VALUES (%s, %s)', ("Mike", 23))

# with connection.cursor() as cur:
#     cur.executemany('INSERT INTO `week` (days, temp) VALUES (%s, %s)', (my_week))
#     connection.commit()

# Данные таблицы
# with connection.cursor() as cur:
#     cur.execute('SELECT * FROM `week`')
#     row = cur.fetchall()
#     with open('Данные табл.txt', 'a', encoding='utf-8') as f:
#         for i in row:
#             f.write(str(i) + '\n')