
import MySQLdb

db = MySQLdb.connect("tigerhacks.cmch6rgigsis.us-east-2.rds.amazonaws.com", "ku", "rockchalk", "Jayhacks")

cursor = db.cursor()

source = "nytimes"
headline = "Blood Donation Lines for Las Vegas Shooting Victims Stretch for Blocks"
url = "https://www.nytimes.com/2017/10/02/us/donate-blood-las-vegas.html"

query = "INSERT INTO HEADLINES(SOURCE, HEADLINE, URL) VALUES ('" + source + "', '" + headline + "', '" + url + "')"

try:
	cursor.execute(query)

	db.commit()
except:
	db.rollback()

db.close()
