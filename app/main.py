"""
CogniPlan AI
============
Adaptive Agentic Learning System

Main application entry point.
"""

from datetime import datetime

from fastapi import FastAPI


app = FastAPI(
    title="CogniPlan AI",
    description=(
        "An adaptive, agentic AI learning system that "
        "personalizes study plans using learner performance, "
        "knowledge gaps, retention signals, and learning behavior."
    ),
    version="2.0.0",
)


@app.get("/")
def root():
    """Return basic system information."""
    return {
        "system": "CogniPlan AI",
        "version": "2.0.0",
        "status": "online",
        "architecture": "agentic",
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.get("/health")
def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "cogniplan-api",
    }


@app.get("/api/v1/system")
def system_info():
    """Return information about the CogniPlan architecture."""
    return {
        "name": "CogniPlan AI",
        "version": "2.0.0",
        "architecture": "adaptive-agentic",
        "components": [
            "Student Intelligence Engine",
            "Adaptive Planning Agent",
            "Performance Evaluation Agent",
            "Schedule Adaptation Agent",
            "Learning Analytics Engine",
        ],
    }
