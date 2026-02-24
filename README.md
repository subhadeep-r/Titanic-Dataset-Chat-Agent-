# Titanic Dataset Chat Agent

A simple chatbot that can answer naturallanguage questions about the
Titanic dataset and return both text replies and useful visualizations
It’s built with:

* **Backend** – Python / FastAPI with a small agent that inspects the
  `seaborn` Titanic dataset.
* **Agent logic** – contained in `backend/agent.py`; parses questions,
  computes statistics, and generates plots.
* **Frontend** – a Streamlit app (`frontend/streamlit_app.py`) that sends
  user questions to the API and displays answers and images.

## Quick start

```powershell
# clone the repo
git clone https://github.com/subhadeep-r/Titanic-Dataset-Chat-Agent.git
cd Titanic-Dataset-Chat-Agent

# create & activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# install dependencies
pip install --upgrade pip
pip install -r [requirements.txt](http://_vscodecontentref_/0)

# start the API (runs on http://localhost:8000)
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# in a second terminal, start the Streamlit frontend
.venv\Scripts\python -m streamlit run [streamlit_app.py](http://_vscodecontentref_/1) --server.port 8501