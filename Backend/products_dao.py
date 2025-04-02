import mysql.connector
cnx = mysql.connector.connect(user = 'root', password='7291945251',
                              host = '127.0.0.1',
                              database = 'grocery_store')
# cnx.close()

cursor = cnx.cursor()

query = "SELECT * FROM grocery_store.products"

cursor.execute(query)

for () in cursor:
    pass
cnx.close()