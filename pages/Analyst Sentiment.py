import streamlit as st
from google_play_scraper import Sort, reviews
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
import io

st.set_page_config(
    page_title="Sentiment Analyst",
    page_icon="images/analis.png",
)

# Function to scrape reviews
def scrape_reviews(app_id, num_reviews):
    result, _ = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.MOST_RELEVANT,
        count=num_reviews,
        filter_score_with=None
    )
    return result

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    return text

# Function for sentiment analysis
def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        text = preprocess_text(review['content'])
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        sentiments.append(sentiment)
    return sentiments

# Function for sentiment labeling
def label_sentiments(sentiments):
    labels = ['Negative' if s < 0 else 'Positive' if s > 0 else 'Neutral' for s in sentiments]
    return labels

# Function to create sentiment distribution visualization
def plot_sentiment_distribution(sentiments):
    plt.figure(figsize=(10, 6))
    plt.hist(sentiments, bins=20, edgecolor='k', alpha=0.7)
    plt.title('Sentiment Distribution of Reviews')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt)

# Function to create sentiment proportion pie chart
def plot_sentiment_pie_chart(labels):
    sentiment_counts = pd.Series(labels).value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Proportion of Review Sentiments')
    st.pyplot(plt)

# Function to create sentiment count bar chart
def plot_sentiment_bar_chart(labels):
    sentiment_counts = pd.Series(labels).value_counts()
    plt.figure(figsize=(10, 6))
    sentiment_counts.plot(kind='bar', color=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Count of Review Sentiments')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.grid(True)
    st.pyplot(plt)

# Function to display evaluation metrics
def show_evaluation_report(true_labels, pred_labels):
    st.subheader('Model Evaluation')
    st.write('Accuracy:', accuracy_score(true_labels, pred_labels))
    st.text(classification_report(true_labels, pred_labels))

# Function to download CSV file
def create_csv_download_link(df):
    csv = df.to_csv(index=False)
    buf = io.BytesIO()
    buf.write(csv.encode())
    buf.seek(0)
    return buf

# Streamlit App
st.title('App Review Sentiment Analysis App on Play Store')

app_id = st.text_input('Enter Play Store App ID:', 'Example: com.grabtaxi.passenger')
num_reviews = st.number_input('Number of Reviews to Retrieve:', min_value=1, value=1500, step=1)

if st.button('Scrape and Analyze'):
    if app_id:  # Ensure app_id is not empty
        with st.spinner('Scraping and analyzing reviews...'):
            reviews_data = scrape_reviews(app_id, num_reviews)
            sentiments = analyze_sentiment(reviews_data)
            labels = label_sentiments(sentiments)
            
            # Save data to DataFrame and CSV
            df = pd.DataFrame({
                'Review': [review['content'] for review in reviews_data],
                'Sentiment': labels
            })
            
            # Provide download link for CSV file
            csv_buffer = create_csv_download_link(df)
            st.download_button(
                label="Download Review Data",
                data=csv_buffer,
                file_name='review_play_store.csv',
                mime='text/csv'
            )
            
            # Display data summary
            st.write(f'Total reviews retrieved: {len(reviews_data)}')
            st.write(f'Average sentiment: {sum(sentiments) / len(sentiments):.2f}')
            
            # Plot sentiment distribution
            plot_sentiment_distribution(sentiments)
            
            # Plot sentiment proportion
            plot_sentiment_pie_chart(labels)
            
            # Plot sentiment count
            plot_sentiment_bar_chart(labels)
            
            # Model evaluation
            st.subheader('Model Evaluation')
            
            # Split data into train and test
            X_train, X_test, y_train, y_test = train_test_split(df['Review'], df['Sentiment'], test_size=0.2, random_state=42)
            
            # Vectorization and Model Training
            vectorizer = CountVectorizer()
            X_train_vec = vectorizer.fit_transform(X_train)
            X_test_vec = vectorizer.transform(X_test)
            
            model = MultinomialNB()
            model.fit(X_train_vec, y_train)
            y_pred = model.predict(X_test_vec)
            
            # Show evaluation report
            show_evaluation_report(y_test, y_pred)
    else:
        st.error('The application ID cannot be empty!')
