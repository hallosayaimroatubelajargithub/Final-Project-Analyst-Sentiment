# Final Project Analyst Sentiment [FGA Digitalent 2024]
![gambar](https://github.com/user-attachments/assets/3199b40b-7694-452a-9d84-b75ccb647e2f)


This project is a sentiment analysis application designed to provide insights into user reviews on the Google Play Store. The app categorizes reviews into **<span style="color:#00FF00;">positive</span>**, **<span style="color:#FF0000;">negative</span>**, and **<span style="color:#808080;">neutral</span>** sentiments and visualizes the distribution to help users understand public perception of an app.

## Key Features
`1.` <b>Scraping Reviews:</b> Automatically scrape reviews from the Google Play Store based on the app's ID.\
`2.` <b>Sentiment Analysis:</b> Analyze the sentiment of each review using natural language processing techniques.\
`3.` <b>Data Visualization:</b> Visualize sentiment distribution using various charts like histograms, pie charts, and bar charts.\
`4.` <b>Model Evaluation:</b> Evaluate the accuracy of the sentiment analysis model and display detailed performance metrics.

## Project Structure
```bash
├── Home.py                # The main homepage of the application
├── Analyst_Sentiment.py   # The core module for sentiment analysis and visualization
├── Profile.py             # Profile page of the project creator
├── images/                # Directory containing images used in the app
└── requirements.txt       # List of dependencies for the project
```

## How to Install
```bash
# Step 1 -> Clone repository
git clone [https://github.com/hallosayaimroatubelajargithub/Final-Project-Analyst-Sentiment.git]

# Step 2 -> Navigate to project directory
cd Final-Project-Analyst-Sentiment

# Step 3 -> Install dependencies
pip install -r requirements.txt

# Last step -> Run the application
streamlit run Home.py
```

## Application Usage
```vbnet
1. Enter the Play Store App ID in the text box on the Analyst Sentiment page.
2. Specify the number of reviews you want to retrieve.
3. Click the "Scrape and Analyze" button to retrieve and analyze the reviews.
4. Explore the visualizations and download the analyzed data as a CSV file.
```

## Online Access
<b>Link:</b> https://final-project-analyst-sentiment-250602.streamlit.app/

## Full Version on Medium
<b>Link:</b>

## MIT License
Copyright (c) 2024 Imroatu Solicah
