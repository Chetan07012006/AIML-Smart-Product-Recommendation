import random
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st


# Helper functions to generate random data
def random_date(start, end):
    """Generate a random datetime between start and end."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def random_categories():
    categories = ['Electronics', 'Books', 'Clothing', 'Beauty', 'Home', 'Toys']
    return random.sample(categories, k=random.randint(1, 3))


def random_products():
    product_categories = ['Electronics', 'Books', 'Clothing', 'Beauty', 'Home', 'Toys']
    return {
        'product_id': random.randint(1000, 9999),
        'product_name': f"Product {random.randint(1, 100)}",
        'category': random.choice(product_categories),
        'price': round(random.uniform(10, 1000), 2),
        'rating': round(random.uniform(1, 5), 1),
        'popularity_score': random.randint(1, 100)
    }


# Main function to generate datasets based on user input
def generate_dataset():
    # Streamlit UI elements for user input
    st.title('Smart product Recommendation')

    num_users = st.number_input("Enter the number of users:", min_value=1, max_value=1000, value=10)
    num_products = st.number_input("Enter the number of products:", min_value=1, max_value=1000, value=20)

    start_date = st.date_input("Enter the start date for interactions:", value=datetime(2023, 1, 1))
    end_date = st.date_input("Enter the end date for interactions:", value=datetime(2023, 12, 31))

    # User dataset
    users = []
    for i in range(num_users):
        users.append({
            'user_id': i + 1,
            'age': random.randint(18, 65),
            'gender': random.choice(['Male', 'Female']),
            'location': random.choice(['Delhi', 'Mumbai', 'Chennai', 'Hyderabad', 'Kerala']),
            'preferred_categories': random_categories(),
            'purchase_history': []
        })

    # Product dataset
    products = [random_products() for _ in range(num_products)]

    # Interactions dataset
    interactions = []
    interaction_types = ['view', 'add_to_cart', 'purchase']

    # Generate user-product interactions
    for user in users:
        num_interactions = random.randint(5, 15)
        for _ in range(num_interactions):
            product = random.choice(products)
            interaction_type = random.choice(interaction_types)
            interaction_timestamp = random_date(start_date, end_date)

            # Add to interactions dataset
            interactions.append({
                'user_id': user['user_id'],
                'product_id': product['product_id'],
                'interaction_type': interaction_type,
                'interaction_timestamp': interaction_timestamp
            })

            # Simulate purchase history if the interaction was a purchase
            if interaction_type == 'purchase':
                user['purchase_history'].append({
                    'product_id': product['product_id'],
                    'purchase_timestamp': interaction_timestamp
                })

    # Convert to DataFrames
    users_df = pd.DataFrame(users)
    products_df = pd.DataFrame(products)
    interactions_df = pd.DataFrame(interactions)

    # Display a sample of the created datasets
    st.subheader("Users DataFrame:")
    st.write(users_df.head())

    st.subheader("Products DataFrame:")
    st.write(products_df.head())

    st.subheader("Interactions DataFrame:")
    st.write(interactions_df.head())

    # Optional: Save to CSV (streamlit will download the files)
    if st.button('Save Datasets to CSV'):
        users_df.to_csv('users.csv', index=False)
        products_df.to_csv('products.csv', index=False)
        interactions_df.to_csv('interactions.csv', index=False)
        st.success("Datasets have been saved as CSV files.")


# Run the Streamlit app
if __name__ == '__main__':
    generate_dataset()