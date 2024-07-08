import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8gY&7LzW2q!",
    database="movies"
)

cursor = db.cursor()

def show_films(cursor, title):
    query = """
    SELECT 
        film_name AS Name, 
        film_director AS Director, 
        genre_name AS Genre, 
        studio_name AS Studio 
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    print(f"-- {title} --")
    for row in results:
        print(f"Film Name: {row[0]}")
        print(f"Director: {row[1]}")
        print(f"Genre: {row[2]}")
        print(f"Studio: {row[3]}")
        print()

show_films(cursor, "DISPLAYING FILMS")

insert_query = """
INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES ('Inception', '2010', 148, 'Christopher Nolan', 
(SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),
(SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));
"""
cursor.execute(insert_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

update_query = """
UPDATE film
SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
WHERE film_name = 'Alien';
"""
cursor.execute(update_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

delete_query = """
DELETE FROM film
WHERE film_name = 'Gladiator';
"""
cursor.execute(delete_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor.close()
db.close()
