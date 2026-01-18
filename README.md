# Fact-Checking Web App

## Overview
This project is a **Fact-Checking Web Application** that automatically verifies factual claims in documents before publication.  
The app ingests a PDF, extracts verifiable claims, checks them against **live web data**, and flags each claim as **Verified**, **Inaccurate**, or **False** with supporting sources.

The system is designed to detect **intentional misinformation, myths, and outdated statistics**, exactly as described in the assignment evaluation criteria.

---

## Key Features
- 📄 Upload and process PDF documents
- 🔍 Extract factual, checkable claims (numbers, dates, prices, statistics)
- 🌐 Verify claims using real-time web search
- 🚩 Classify claims as Verified, Inaccurate, or False
- 📚 Provide corrected real-time values with sources
- ☁️ Deployed and accessible via Streamlit Cloud

---

## Tech Stack
- **UI:** Streamlit  
- **Backend:** Python  
- **LLM:** Google Gemini (`google-genai`)  
- **Web Search:** Tavily API  
- **PDF Parsing:** PyPDF2  
- **Deployment:** Streamlit Cloud  

---

## How It Works

### 1. PDF Ingestion
Users upload a PDF through the Streamlit interface. Text is extracted using PyPDF2.

### 2. Claim Extraction
The app uses an LLM-based prompt to extract **only factual, verifiable claims**, such as:
- Prices and financial figures  
- Dates and timelines  
- Percentages and statistics  
- Quantifiable technical facts  

Editorial, descriptive, or opinion-based statements are ignored.

### 3. Claim Verification
Each extracted claim is verified using:
- **Live web search (Tavily)** to fetch real-time evidence  
- **Gemini LLM reasoning** to compare the claim against current data  

Each claim is classified as:
- **Verified** – Matches reliable, current data  
- **Inaccurate** – Partially correct but contains wrong or outdated values  
- **False** – Unsupported, incorrect, or contradicted by real-time evidence  

When applicable, the app provides **corrected real-time information** along with **source citations**.

### 4. Results Display
For every claim, the app displays:
- The extracted claim  
- Classification result  
- Correction (if needed)  
- Sources used for verification  

---

## Deployment

The application is deployed on **Streamlit Cloud** and is publicly accessible.

**Live App URL:**  
(https://fact-checking-web-app-e3vazufc4gfwr6qrigpctl.streamlit.app/)

API keys are securely managed using **Streamlit Secrets (TOML format)** and are not stored in the repository.

---
## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/vanshrajput1/fact-checking-web-app.git
cd fact-checking-web-app
```
2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set API keys

Set the following keys either as environment variables or in .streamlit/secrets.toml:
```bash
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
TAVILY_API_KEY = "YOUR_TAVILY_API_KEY"
```
5. Run the application
```bash
streamlit run app.py
```
The app will be available at:
```bash
http://localhost:8501
```




