"""
CogniPlan AI API
================

FastAPI application exposing the adaptive learning engine.

Core workflow:

Student Data
     ↓
Planner Agent
     ↓
Study Session
     ↓
Evaluator Agent
     ↓
Adaptation Agent
     ↓
Next Learning Strategy
"""

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.agents.orchestrator import CogniPlanOrchestrator


# ---------------------------------------------------------
# Application
# ---------------------------------------------------------

app = FastAPI(
    title="CogniPlan AI",
    description=(
        "Adaptive Agentic Learning System powered by "
        "student intelligence, performance evaluation, "
        "and closed-loop schedule adaptation."
    ),
    version="2.0.0",
)


# ---------------------------------------------------------
# Agent System
# ---------------------------------------------------------

orchestrator = CogniPlanOrchestrator()


# ---------------------------------------------------------
# Request Models
# ---------------------------------------------------------


class PlanningRequest(BaseModel):
    """
    Input required to generate a personalized study plan.
    """

    tasks: list[dict]


class SessionRequest(BaseModel):
    """
    Study-session performance submitted after learning.
    """

    questions_attempted: int = Field(
        gt=0,
        description="Number of questions attempted.",
    )

    correct_answers: int = Field(
        ge=0,
        description="Number of correctly answered questions.",
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Student confidence from 0 to 1.",
    )

    time_spent_minutes: int = Field(
        ge=0,
        description="Time spent during the session.",
    )

    retention_risk: float = Field(
        ge=0.0,
        le=1.0,
        description="Estimated retention risk from 0 to 1.",
    )

    current_duration: int = Field(
        gt=0,
        description="Current study-session duration.",
    )


# ---------------------------------------------------------
# Basic Routes
# ---------------------------------------------------------


@app.get("/")
def root():
    """
    System landing endpoint.
    """

    return {
        "system": "CogniPlan AI",
        "version": "2.0.0",
        "status": "online",
        "architecture": "adaptive-agentic",
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.get("/health")
def health():
    """
    Health-check endpoint.
    """

    return {
        "status": "healthy",
        "service": "cogniplan-api",
    }


@app.get("/api/v1/system")
def system_info():
    """
    Return information about the agent architecture.
    """

    return {
        "name": "CogniPlan AI",
        "version": "2.0.0",
        "architecture": "adaptive-agentic",
        "agents": [
            "PlannerAgent",
            "EvaluatorAgent",
            "AdaptationAgent",
        ],
        "learning_loop": [
            "PLAN",
            "STUDY",
            "EVALUATE",
            "ADAPT",
            "REPLAN",
        ],
    }


# ---------------------------------------------------------
# Planning API
# ---------------------------------------------------------


@app.post("/api/v1/planner/plan")
def generate_plan(request: PlanningRequest):
    """
    Generate a prioritized learning plan.
    """

    plan = orchestrator.create_plan(
        request.tasks
    )

    return {
        "status": "success",
        "plan": plan,
    }


# ---------------------------------------------------------
# Evaluation + Adaptation API
# ---------------------------------------------------------


@app.post("/api/v1/sessions/evaluate")
def evaluate_session(request: SessionRequest):
    """
    Evaluate a completed study session and determine
    how the next session should be adapted.
    """

    result = orchestrator.process_session(
        questions_attempted=request.questions_attempted,
        correct_answers=request.correct_answers,
        confidence=request.confidence,
        time_spent_minutes=request.time_spent_minutes,
        retention_risk=request.retention_risk,
        current_duration=request.current_duration,
    )

    return {
        "status": "success",
        "result": result,
    }
