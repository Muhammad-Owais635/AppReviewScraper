
# 📱 App Store & Google Play Review Scraper

A Python-based project to scrape user reviews from **Google Play Store** and **Apple App Store**, enabling large-scale analysis of app feedback and sentiment trends.

---

## 🚀 Features

- 🔍 Scrapes reviews from:
  - Google Play Store
  - Apple App Store
- 📅 Filter by review date (if supported)
- 🌐 Supports multiple apps via app ID
- 💾 Export to CSV/JSON format
- 🧠 Ready for sentiment analysis or NLP pipelines

---

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `google-play-scraper` (or `google-play-scraper-python`)
- `app_store_scraper` (or custom App Store API wrapper)
- `pandas`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/AppReviewScraper.git
cd AppReviewScraper
```

2. **Run the scraper**
```bash
# For Google Play
python scrape_google_play.py

# For Apple App Store
python scrape_app_store.py
```

3. **Output**
Reviews will be saved as `.csv` files in the `output/` directory.

---

## 🖼️ Example

| Review Text | Rating | Date |
|-------------|--------|------|
| Great app!  | 5      | 2024-01-01 |
| Crashes a lot | 2   | 2024-01-05 |

---

## 📁 Project Structure

```
app-review-scraper/
├── scrape_google_play.py
├── scrape_app_store.py
├── utils/
│   └── helpers.py
├── output/
│   └── *.csv
├── requirements.txt
└── README.md
```

---

## 📤 To-Do / Future Improvements

- Sentiment analysis integration (e.g., VADER/TextBlob)
- UI dashboard using Streamlit or Flask

