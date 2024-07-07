import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8gY&7LzW2q!",
    database="movies"
)

cursor = db.cursor()

# Query 1: Select all fields from the studio table
query1 = "SELECT * FROM studio;"
cursor.execute(query1)
results1 = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")
for result in results1:
    print(f"Studio 1D: {result[0]}")
    print(f"Studio Name: {result[1]}")
print()

# Query 2: Select all fields from the genre table
query2 = "SELECT * FROM genre;"
cursor.execute(query2)
results2 = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --")
for result in results2:
    print(f"Genre ID: {result[0]}")
    print(f"Genre Name: {result[1]}")
print()

# Query 3: Select movie names with a runtime of less than two hours
query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
cursor.execute(query3)
results3 = cursor.fetchall()
print("~- DISPLAYING Short FAIm RECORDS --")
for result in results3:
    print(f"E12m Name: {result[0]}")
    print(f"Runtine: {result[1]}")
print()

# Query 4: Get a list of film names and directors grouped by director
query4 = "SELECT film_director, film_name FROM film ORDER BY film_director;"
cursor.execute(query4)
results4 = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --")
for result in results4:
    print(f"Film Name: {result[1]}")
    print(f"Director: {result[0]}")
print()

# Close the cursor and connection
cursor.close()
db.close()
