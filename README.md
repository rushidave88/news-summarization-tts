---
title: News Summarization Tts
emoji: 🏢
colorFrom: pink
colorTo: indigo
sdk: docker
pinned: false
short_description: News Summarization and Text-to-Speech Application
---
This project is a web-based application that extracts key details from news articles related to a given company, performs sentiment analysis, and generates a Hindi Text-to-Speech (TTS) output. The tool allows users to enter a company name and receive a structured sentiment report along with an audio summary.

Features
     News Extraction: Fetches 10 news articles related to the company.
     Sentiment Analysis: Categorizes articles as Positive, Negative, or Neutral.
     Comparative Analysis: Compares sentiment across articles.
     Text-to-Speech (TTS): Converts summarized content into Hindi speech.
     FastAPI Backend: API-based architecture for easy integration.
     Gradio UI: Provides an interactive user interface.
     Deployment: Ready to deploy on Hugging Face Spaces or any cloud provider.

Installation
Step 1: Clone the Repository
    git clone <your-repo-link>
    cd news-summarization-tts
Step 2: Create a Virtual Environment
    python -m venv venv
    venv\Scripts\activate (activate virtyal envirn.)
Step 3: Install Dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
tep 4: Ensure static/ Directory Exists
    mkdir static (for audio)

Running the Application
Step 1: Start the FastAPI Server
    uvicorn api:app --reload (=> http://127.0.0.1:8000 server link)
    Test api in browser => http://127.0.0.1:8000/analyze/
Step 2: Start the Gradio UI
    python app.py (http://127.0.0.1:7860 , Gradio Web interface)

 Folder Structure
news-summarization-tts/
│── api.py               # FastAPI backend
│── app.py               # Gradio frontend
│── news_scraper.py      # Fetches news articles
│── sentiment_analysis.py # Sentiment analysis module
│── comparative_analysis.py # Comparative sentiment analysis
│── tts.py               # Text-to-Speech (Hindi)
│── requirements.txt      # Python dependencies
│── static/               # Stores audio files
│── README.md            # Project documentation

Deployment (Hugging Face Spaces)
    1.Create a Hugging Face Space and select FastAPI as the framework.
    2.Push your repository to Hugging Face:
    git add .
    git commit -m "Deploying to Hugging Face"
    git push origin main

API Used in the Project
    1. FastAPI: Used to create and manage the backend API.
    2. NewsAPI: Fetches news articles related to a company.
    4. gTTS (Google Text-to-Speech): Converts text summaries into Hindi speech.
    5. FastAPI Static Files API: Serves the generated TTS audio file for playback in Gradio.

-------------------------------------------------------------------------
Work Flow
    1. User inputs a company name in the Gradio/Streamlit UI.
    2. The frontend sends a request to the FastAPI backend.
    3. The FastAPI backend fetches news articles using Bing News Search API or NewsAPI.
    4. Each article's content is summarized and sentiment analysis is performed using Hugging Face Transformers.
    5. A comparative sentiment analysis report is generated.
    6. The sentiment report is converted into Hindi speech using gTTS (Google Text-to-Speech).
    7. The generated speech file is stored in the `/static/` directory.
    8. The FastAPI backend serves the structured report and the generated audio file.
    9. The Gradio UI displays the sentiment analysis results and plays the Hindi speech.

Model Details
    News Summarization
        Method Used: The newspaper3k library extracts article content and performs Natural Language Processing (NLP)-based summarization.
     Sentiment Analysis
        Model Used: distilbert/distilbert-base-uncased-finetuned-sst-2-english from Hugging Face Transformers.
        Purpose: Categorizes the sentiment of each news article as Positive, Negative, or Neutral.
    Comparative Sentiment Analysis
        Method Used: The results of sentiment analysis across all articles are aggregated to provide insights on media perception trends.
    Text-to-Speech (TTS)
        Model Used: gTTS (Google Text-to-Speech)
        Purpose: Converts the final sentiment report into Hindi speech and saves it as an MP3 file for playback.

API Usage (Third-Party APIs & Their Purpose)
    
    FastAPI	-- Backend framework to handle API requests.
    API / NewsAPI --	Fetches news articles related to a company.
    Hugging Face Transformers API --	Performs sentiment analysis on news summaries.
    gTTS (Google Text-to-Speech) --	Converts text summaries into Hindi speech.
    FastAPI Static Files API --	Serves the generated TTS audio file for playback in Gradio.


Check out the configuration reference at [Hugging Face Spaces Configuration](https://huggingface.co/docs/hub/spaces-config-reference).
