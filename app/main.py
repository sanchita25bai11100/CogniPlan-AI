"""
CogniPlan AI
============

Adaptive Agentic Learning System.

CogniPlan continuously evaluates student performance
and adapts future learning recommendations.

Core loop:

PLAN → STUDY → EVALUATE → ADAPT → REPLAN
"""

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.agents.orchestrator import CogniPlanOrchestrator
from app.services.analytics import LearningAnalytics
from app.services.knowledge_engine import KnowledgeEngine
from app.services.tutor import AITutor


# =========================================================
# Application
# =========================================================

app = FastAPI(
    title="CogniPlan AI",
    description=(
        "Adaptive Agentic Learning System that personalizes "
        "learning using performance signals, knowledge gaps, "
        "retention risk, and continuous feedback."
    ),
    version="2.0.0",
)


# =========================================================
# Core Intelligence Components
# =========================================================

orchestrator = CogniPlanOrchestrator()

analytics = LearningAnalytics()

knowledge_engine = KnowledgeEngine()

tutor = AITutor(
    knowledge_engine=knowledge_engine
)


# =========================================================
# Request Models
# =========================================================


class PlanningRequest(BaseModel):
    """
    Request for generating a prioritized study plan.
    """

    tasks: list[dict]


class SessionRequest(BaseModel):
    """
    Performance data from a completed study session.
    """

    questions_attempted: int = Field(gt=0)

    correct_answers: int = Field(ge=0)

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    time_spent_minutes: int = Field(
        ge=0,
    )

    retention_risk: float = Field(
        ge=0.0,
        le=1.0,
    )

    current_duration: int = Field(gt=0)


class TutorRequest(BaseModel):
    """
    Request for personalized tutoring.
    """

    question: str

    mastery: float = Field(
        ge=0.0,
        le=1.0,
        default=0.5,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        default=0.5,
    )


# =========================================================
# System Routes
# =========================================================


@app.get("/")
def root():
    """
    Return basic system information.
    """

    return {
        "system": "CogniPlan AI",
        "version": "2.0.0",
        "status": "online",
        "architecture": "adaptive-agentic",
        "learning_loop": (
            "PLAN → STUDY → EVALUATE → ADAPT → REPLAN"
        ),
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.get("/health")
def health():
    """
    Service health check.
    """

    return {
        "status": "healthy",
        "service": "cogniplan-api",
    }


@app.get("/api/v1/system")
def system_info():
    """
    Describe the system architecture.
    """

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
            "Personal Knowledge Engine",
            "AI Tutor",
        ],
        "learning_loop": [
            "PLAN",
            "STUDY",
            "EVALUATE",
            "ADAPT",
            "REPLAN",
        ],
    }


# =========================================================
# Planning
# =========================================================


@app.post("/api/v1/planner/plan")
def generate_plan(
    request: PlanningRequest,
):
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


# =========================================================
# Session Evaluation
# =========================================================


@app.post("/api/v1/sessions/evaluate")
def evaluate_session(
    request: SessionRequest,
):
    """
    Evaluate a study session and adapt the next strategy.
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


# =========================================================
# Learning Analytics
# =========================================================


@app.post("/api/v1/analytics/insights")
def learning_insights(
    mastery: float = 0.5,
    confidence: float = 0.5,
    retention_risk: float = 0.5,
    session_accuracies: list[float] | None = None,
):
    """
    Generate a learner intelligence report.
    """

    if session_accuracies is None:
        session_accuracies = []

    insights = analytics.generate_insights(
        mastery=mastery,
        confidence=confidence,
        retention_risk=retention_risk,
        session_accuracies=session_accuracies,
    )

    return {
        "status": "success",
        "insights": insights,
    }


# =========================================================
# AI Tutor
# =========================================================


@app.post("/api/v1/tutor/explain")
def explain_concept(
    request: TutorRequest,
):
    """
    Generate a personalized, knowledge-grounded
    tutoring instruction.
    """

    result = tutor.explain(
        question=request.question,
        mastery=request.mastery,
        confidence=request.confidence,
    )
# =========================================================
# End-to-End Demo
# =========================================================


@app.get("/api/v1/demo")
def run_demo():
    """
    Run a complete CogniPlan learning cycle using
    representative learner data.

    This endpoint demonstrates how the system combines
    evaluation, analytics, and adaptation.
    """

    questions_attempted = 20
    correct_answers = 13
    confidence = 0.62
    time_spent_minutes = 30
    retention_risk = 0.48
    current_duration = 45

    # -----------------------------------------------------
    # Evaluate the session
    # -----------------------------------------------------

    evaluation = orchestrator.process_session(
        questions_attempted=questions_attempted,
        correct_answers=correct_answers,
        confidence=confidence,
        time_spent_minutes=time_spent_minutes,
        retention_risk=retention_risk,
        current_duration=current_duration,
    )

    # -----------------------------------------------------
    # Generate learning analytics
    # -----------------------------------------------------

    analytics_report = analytics.generate_insights(
        mastery=0.65,
        confidence=confidence,
        retention_risk=retention_risk,
        session_accuracies=[
            0.55,
            0.60,
            0.65,
            0.70,
        ],
    )

    # -----------------------------------------------------
    # Return unified learning intelligence
    # -----------------------------------------------------

    return {
        "demo": "CogniPlan Adaptive Learning Cycle",
        "student_session": {
            "questions_attempted": questions_attempted,
            "correct_answers": correct_answers,
            "confidence": confidence,
            "time_spent_minutes": time_spent_minutes,
        },
        "evaluation": evaluation,
        "analytics": analytics_report,
        "next_action": evaluation[
            "adaptation"
        ]["action"],
        "learning_loop": [
            "PLAN",
            "STUDY",
            "EVALUATE",
            "ADAPT",
            "REPLAN",
        ],
    }
    return {
        "status": "success",
        "tutor_response": result,
    }
