import sys
import base64
from pathlib import Path

# Ensure project root is on sys.path so tests can import `backend` package
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.agent import TitanicAgent


def test_percentage_male():
    agent = TitanicAgent()
    res = agent.ask("What percentage of passengers were male on the Titanic?")
    assert "answer" in res
    assert "%" in res["answer"]


def test_average_fare():
    agent = TitanicAgent()
    res = agent.ask("What was the average ticket fare?")
    assert "answer" in res
    assert "Average" in res["answer"] or "Mean" in res["answer"]


def test_embarked_counts_and_image():
    agent = TitanicAgent()
    res = agent.ask("How many passengers embarked from each port?")
    assert "answer" in res
    assert ":" in res["answer"]
    assert "image" in res
    assert res["image"] is None or isinstance(res["image"], str)


def test_age_histogram_returns_image():
    agent = TitanicAgent()
    res = agent.ask("Show me a histogram of passenger ages")
    assert "image" in res
    assert res["image"] is not None
    # ensure it's valid base64 that decodes
    decoded = base64.b64decode(res["image"])
    assert len(decoded) > 0
