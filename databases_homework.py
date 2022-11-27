import sqlite3
from sqlite3 import Error
import os
import json

database = os.path.join(os.getcwd(), "film_data.db")
conn = sqlite3.connect(database)
curs_ = conn.cursor()

select_films_starting_with_b = """SELECT title
                  FROM film_data
                  WHERE title LIKE "B%"
                """

with conn:
    curs_.execute(select_films_starting_with_b)

result = curs_.fetchall()
print(result)

select_longest_film = """SELECT length
                        FROM film_data
                        ORDER BY length desc
                        """

with conn:
    curs_.execute(select_longest_film)

result = curs_.fetchone()
print(result)

selecting_all = """SELECT *
                    FROM film_data
                """

with conn:
    curs_.execute(selecting_all)

result = curs_.fetchall()

with open("film.json", "w") as json_file:
    json.dump(result, json_file)

selecting_films = """SELECT *
                        FROM film_data
                        where release_year > 2010 and 3 <= rate <= 5
                    """

with conn:
    curs_.execute(selecting_films)

result_for_new_table = curs_.fetchall()

print(result_for_new_table)

database = os.path.join(os.getcwd(), "filtered_films.db")
conn = sqlite3.connect(database)
curs = conn.cursor()

new_filtered_films_table = """ CREATE TABLE IF NOT EXISTS filtered_films (
                                                id integer PRIMARY KEY,
                                                film_id integer,
                                                title text,
                                                description text,
                                                release_year text,
                                                rate integer,
                                                length integer,
                                                special_features text
                                            ); """

with conn:
    curs.execute(new_filtered_films_table)

insert_query = """INSERT INTO filtered_films (film_id, title, description, release_year, length, rate, special_features)
                    VALUES(?, ?, ?, ?, ?, ?, ?);
                """

with conn:
    curs.executemany(insert_query, result_for_new_table)

result = curs_.fetchall()
print(result)


