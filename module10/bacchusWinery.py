import mysql.connector  # Import the mysql.connector module to connect to the MySQL database

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',  # Database host
    user='root',  # Database username
    password='8gY&7LzW2q!',  # Database password
    database='BacchusWinery'  # Database name
)

cursor = connection.cursor()  # Create a cursor object to interact with the database

# Function to display table data
def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")  # Execute SQL query to select all data from the table
    rows = cursor.fetchall()  # Fetch all the rows from the executed query
    headers = [i[0] for i in cursor.description]  # Get the column headers from the cursor description

    # Print table name
    print(f"\n{table_name} Table")

    # Print headers
    print(" | ".join(headers))

    # Print separator line
    print("-" * (len(" | ".join(headers))))

    # Print rows
    for row in rows:
        print(" | ".join(str(col) for col in row))

# List of tables to display
tables = ['Wine', 'Supplier', 'Supply', 'Distributor', 'Orders', 'OrderDetails', 'Employee']

# Loop through each table and display its data
for table in tables:
    display_table(table)

# Close the cursor and the connection to the database
cursor.close()  # Close the cursor
connection.close()  # Close the connection
