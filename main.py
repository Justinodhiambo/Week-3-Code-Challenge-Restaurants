from models.customer import customer
from models.restaurant import restaurant
from models.review import review
from database.db_setup import setup_database

# Create database tables
setup_database()

# Example usage
if __name__ == "__main__":
    # You can create instances of Customer, Restaurant, and Review classes
    # and interact with the database here for testing purposes

    # Example of creating and saving a customer
    customer1 = Customer("John", "Doe")
    customer1.save_to_database()

    # Example of creating and saving a restaurant
    restaurant1 = Restaurant("The Fancy Place", 5)
    restaurant1.save_to_database()

    # Example of creating and saving a review
    review1 = Review(restaurant_id=1, customer_id=1, star_rating=4)
    review1.save_to_database()
