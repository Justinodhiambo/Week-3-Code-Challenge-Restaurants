import sqlite3

class Review:
    def __init__(self, restaurant_id, customer_id, star_rating):
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    def save_to_database(self):
        conn = sqlite3.connect('restaurant_reviews.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (restaurant_id, customer_id, star_rating)
            VALUES (?, ?, ?)
        ''', (self.restaurant_id, self.customer_id, self.star_rating))
        conn.commit()
        conn.close()

