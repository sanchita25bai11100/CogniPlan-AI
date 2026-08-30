from app.agents.planner_agent import PlannerAgent
from app.agents.evaluator_agent import EvaluatorAgent
from app.agents.adaptation_agent import AdaptationAgent


def test_planner_prioritizes_weak_topics():
    planner = PlannerAgent()

    tasks = [
        {
            "subject": "AI",
            "topic": "Neural Networks",
            "mastery": 0.30,
            "retention_risk": 0.70,
            "exam_urgency": 0.90,
            "difficulty": 0.80,
        },
        {
            "subject": "Java",
            "topic": "Classes",
            "mastery": 0.90,
            "retention_risk": 0.10,
            "exam_urgency": 0.30,
            "difficulty": 0.40,
        },
    ]

    ranked = planner.rank_tasks(tasks)

    assert ranked[0]["topic"] == "Neural Networks"
    assert ranked[0]["priority"] > ranked[1]["priority"]


def test_evaluator_calculates_accuracy():
    evaluator = EvaluatorAgent()

    result = evaluator.evaluate_session(
        questions_attempted=20,
        correct_answers=15,
        confidence=0.7,
        time_spent_minutes=30,
    )

    assert result["accuracy"] == 0.75
    assert result["recommendation"] == "STRENGTHEN"


def test_adaptation_increases_revision_for_low_accuracy():
    adaptation = AdaptationAgent()

    result = adaptation.adapt(
        accuracy=0.30,
        retention_risk=0.70,
        current_duration=45,
    )

    assert result["action"] == "increase_revision"
    assert result["strategy"] == "focused_revision"
    assert result["next_duration"] == 60
