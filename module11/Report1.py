import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8gY&7LzW2q!',
    database='BacchusWinery'
)

cursor = connection.cursor()

# Wine Inventory and Price Report Query
wine_inventory_query = """
SELECT Wine.WineID, Wine.WineName, Wine.Type, Wine.Price, IFNULL(SUM(OrderDetails.Quantity), 0) AS TotalSold
FROM Wine
LEFT JOIN OrderDetails ON Wine.WineID = OrderDetails.WineID
GROUP BY Wine.WineID, Wine.WineName, Wine.Type, Wine.Price
ORDER BY Wine.WineID;
"""

cursor.execute(wine_inventory_query)
rows = cursor.fetchall()
headers = [i[0] for i in cursor.description]

# Display the result
print("\nWine Inventory and Price Report\n")
print(" | ".join(headers))
print("-" * (len(headers) * 15))

for row in rows:
    print(" | ".join(str(cell) for cell in row))

# Close the connection
cursor.close()
connection.close()
