from google_play_scraper import reviews
import pandas as pd
import time

# App ID of the app on the Play Store
app_id = 'com.careem.acma'

# Extract reviews with no limit
def get_reviews(app_id):
    all_reviews = []
    continuation_token = None  # Initialize the continuation token for pagination
    while True:
        # Fetch reviews, passing in the continuation_token if it's not the first page
        result, continuation_token = reviews(
            app_id,
            count=100,  # Fetching more reviews per request for efficiency
            country='pk',
            continuation_token=continuation_token
        )

        # If no more reviews are available, break the loop
        if not result:
            print("No more reviews available.")
            break

        # Add the fetched reviews to the list
        all_reviews.extend(result)
        # Debugging: show how many reviews are fetched so far
        print(f"Fetched {len(all_reviews)} reviews so far...")

        # If the continuation_token is None, it means no more pages are available
        if not continuation_token:
            print("Reached the end of available reviews.")
            break

        # Optional: To avoid hitting rate limits, add a small delay between requests
        time.sleep(1)

    # Convert the reviews to a DataFrame for easy manipulation
    df_reviews = pd.DataFrame(all_reviews)

    # Extract country (if available)
    #df_reviews['country'] = df_reviews['userName'].apply(lambda x: x.split()[-1] if isinstance(x, str) else 'Unknown')
    # Ensure 'content' column has no None values
    df_reviews['content'] = df_reviews['content'].fillna('')  # Replace None with empty string

    # Detect language: Urdu ('ur') and English ('en')
    df_reviews['language'] = df_reviews['content'].apply(
        lambda x: 'ur' if any("\u0600" <= c <= "\u06FF" for c in x) else 'en'
    )

    # Keep only reviews in Urdu and English
    filtered_reviews = df_reviews[df_reviews['language'].isin(['en', 'ur'])]

    return filtered_reviews

# Fetch reviews
reviews_df = get_reviews(app_id)

# Show the first few reviews
print(reviews_df[['content', 'language']].head())

# Optionally, save reviews to a CSV file with UTF-8 encoding to preserve Urdu text
reviews_df.to_csv('careem_reviews.csv', index=False, encoding='utf-8')

print("Reviews saved to careem_reviews.csv")
