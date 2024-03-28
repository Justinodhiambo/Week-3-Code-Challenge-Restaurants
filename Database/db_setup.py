import sqlite3

def setup_database():
    conn = sqlite3.connect('restaurant_reviews.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY,
            restaurant_id INTEGER,
            customer_id INTEGER,
            star_rating INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
