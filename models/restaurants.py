import sqlite3

class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_to_database(self):
        conn = sqlite3.connect('restaurant_reviews.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO restaurants (name, price)
            VALUES (?, ?)
        ''', (self.name, self.price))
        conn.commit()
        conn.close()

    # Implement other methods as per the requirements
