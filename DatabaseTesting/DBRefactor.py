import MySQLdb

db = MySQLdb.connect("tigerhacks.cmch6rgigsis.us-east-2.rds.amazonaws.com", "ku", "rockchalk", "Jayhacks")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS HEADLINES")

sql = "CREATE TABLE HEADLINES(SOURCE VARCHAR(50) NOT NULL, HEADLINE VARCHAR(200), URL VARCHAR(100) NOT NULL)"

cursor.execute(sql)

db.close()