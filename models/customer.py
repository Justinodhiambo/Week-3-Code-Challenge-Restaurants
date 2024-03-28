import sqlite3

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save_to_database(self):
        conn = sqlite3.connect('restaurant_reviews.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        ''', (self.first_name, self.last_name))
        conn.commit()
        conn.close()

