import MySQLdb

db = MySQLdb.connect("tigerhacks.cmch6rgigsis.us-east-2.rds.amazonaws.com", "ku", "rockchalk", "Jayhacks")

cursor = db.cursor()

SelectQuery = "SELECT * FROM HEADLINES"

print("Executing Query")
cursor.execute(SelectQuery)


print("Formatting results")
results = cursor.fetchall()

print("Result Size: ", str(len(results)), "\n\n")

for row in results:
	source = row[0]
	headline = row[1]
	url = row[2]
	print("Source: ",source, "\nHeadline: ",headline,"\nURL: ",url, "\n\n")

