import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8gY&7LzW2q!',
    database='BacchusWinery'
)

cursor = connection.cursor()

# Order Details Report Query
order_details_query = """
SELECT Orders.OrderID, Orders.OrderDate, Distributor.DistributorName, Wine.WineName, OrderDetails.Quantity
FROM Orders
JOIN Distributor ON Orders.DistributorID = Distributor.DistributorID
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
JOIN Wine ON OrderDetails.WineID = Wine.WineID
ORDER BY Orders.OrderID, OrderDetails.OrderDetailsID;
"""

cursor.execute(order_details_query)
rows = cursor.fetchall()
headers = [i[0] for i in cursor.description]

# Display the result
print("\nOrder Details Report\n")
print(" | ".join(headers))
print("-" * (len(headers) * 15))

for row in rows:
    print(" | ".join(str(cell) for cell in row))

# Close the connection
cursor.close()
connection.close()
