📘 FactCheck AI Agent
A memory-enabled AI fact-checking assistant built using Chainlit and Gemini 2.0 API. This agent evaluates user-submitted claims by searching live internet sources, determines their truthfulness, and returns a verdict with cited, reputable references.

🚀 Features
✅ Built with Chainlit for a smooth chat interface

🔍 Uses Gemini API to perform real-time web-based fact-checking

🧠 Supports session memory (remembers previous user inputs)

📄 Returns verdicts like: True, False, Likely True, Likely False, or Unverified

📚 Provides 2+ reliable source citations (e.g., BBC, WHO, Reuters, etc.)

🛡️ Designed to be neutral, professional, and evidence-based

🛠️ Tech Stack
Python 3.10+

Chainlit

Gemini API (via OpenAI-compatible endpoint)

dotenv for API key management

📦 Installation
bash
Copy
Edit
git clone https://github.com/your-username/factcheck-ai-agent.git
cd factcheck-ai-agent
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # for Linux/macOS
.\.venv\Scripts\activate   # for Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your .env file:

env
Copy
Edit
GEMINI_API_KEY=your_actual_api_key_here
▶️ Run the App
bash
Copy
Edit
chainlit run main.py
Then open http://localhost:8000 in your browser.

🧠 How It Works
User sends a claim (e.g., "NASA confirmed alien life in 2025.")

Agent searches the internet using Gemini

It classifies the claim based on real, credible sources

Verdict and reasoning are returned with URLs

Memory lets it track context from earlier inputs

🧪 Example Usage
User:

Is turmeric effective against COVID-19?

Agent:

❌ Likely False
Based on WHO and CDC data, there is no scientific evidence that turmeric alone can prevent or cure COVID-19.
Sources:

https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19-mythbusters

https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html

