# Titanic Dataset Chat Agent

A clean, minimal chatbot that answers natural-language questions about the
Titanic dataset and returns both text answers and helpful visualizations.

Key components
- **Backend** — FastAPI app in `backend/main.py` exposing a single `/ask`
  endpoint.
- **Agent** — `backend/agent.py` contains `TitanicAgent`, a small
  rule-based analyzer that computes statistics and produces PNG plots
  (returned as base64 strings).
- **Frontend** — Streamlit app at `frontend/streamlit_app.py` that sends
  questions to the backend and displays text + images.

Why this project
- Demonstrates data analysis (`pandas`, `seaborn`), plotting
  (`matplotlib`), a lightweight API (`FastAPI` + `uvicorn`), and an
  interactive UI (`Streamlit`).
- Easy to extend with an LLM or retrieval layer later (e.g. using
  LangChain).

Quick start (local)

1. Clone the repo and change into it:

```powershell
git clone https://github.com/subhadeep-r/Titanic-Dataset-Chat-Agent.git
cd Titanic-Dataset-Chat-Agent
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

4. Start the backend API (port 8000):

```powershell
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

5. In another terminal start the frontend (Streamlit, port 8501):

```powershell
.venv\Scripts\python -m streamlit run frontend/streamlit_app.py --server.port 8501
```

6. Open `http://localhost:8501` in your browser and ask questions such
   as:

   - What percentage of passengers were male on the Titanic?
   - Show me a histogram of passenger ages
   - What was the average ticket fare?
   - How many passengers embarked from each port?

Interacting with the API directly

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What percentage of passengers were male?"}'
```

Project layout

```
backend/
  agent.py
  main.py
frontend/
  streamlit_app.py
requirements.txt
README.md
```

Testing and CI
- Unit tests live in `tests/` and a GitHub Actions workflow runs `pytest`
  on push/PR (see `.github/workflows/ci.yml`).

Notes on deployment

Frontend on Streamlit Cloud
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. In the deployment settings, set the environment variable:
   - `BACKEND_URL=https://your-backend-url.com` (e.g., from Render or Azure)
4. Click Deploy. The frontend will use this backend URL automatically.

Backend on Render or Azure
1. Deploy `backend/main.py` as a web service:
   - Set the startup command to: `python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000`
   - Or use the provided `Dockerfile` if available.
2. Get the public URL of your deployed API (e.g., `https://titanic-api-xyz.onrender.com`).
3. In Streamlit Cloud settings, set `BACKEND_URL` to that URL.
4. Optionally, set `ALLOWED_ORIGINS` on the backend to restrict CORS to your Streamlit Cloud domain for security.

License
- Consider adding an MIT license if you plan to share this publicly.

If you want, I can add a demo GIF, CI badges, a Dockerfile, or more
polished tests next.
