import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8gY&7LzW2q!',
    database='BacchusWinery'
)

cursor = connection.cursor()

# Supplier Supply Summary Report Query
supplier_supply_query = """
SELECT Supplier.SupplierID, Supplier.SupplierName, Supply.SupplyType, SUM(Supply.Quantity) AS TotalQuantity
FROM Supplier
JOIN Supply ON Supplier.SupplierID = Supply.SupplierID
GROUP BY Supplier.SupplierID, Supplier.SupplierName, Supply.SupplyType
ORDER BY Supplier.SupplierID;
"""

cursor.execute(supplier_supply_query)
rows = cursor.fetchall()
headers = [i[0] for i in cursor.description]

# Display the result
print("\nSupplier Supply Summary Report\n")
print(" | ".join(headers))
print("-" * (len(headers) * 15))

for row in rows:
    print(" | ".join(str(cell) for cell in row))

# Close the connection
cursor.close()
connection.close()
