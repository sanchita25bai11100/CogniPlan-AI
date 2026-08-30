"""
CogniPlan Agent Orchestrator
============================

Coordinates CogniPlan's specialized agents into a
continuous adaptive learning loop.

Learning lifecycle:

PLAN
  ↓
STUDY
  ↓
EVALUATE
  ↓
ADAPT
  ↓
REPLAN
"""


from .planner_agent import PlannerAgent
from .evaluator_agent import EvaluatorAgent
from .adaptation_agent import AdaptationAgent


class CogniPlanOrchestrator:
    """
    Central coordinator for the CogniPlan agent system.

    Each agent has a specialized responsibility:

    PlannerAgent
        Decides what the learner should study.

    EvaluatorAgent
        Measures the outcome of a study session.

    AdaptationAgent
        Changes future learning strategy based
        on the evaluation.
    """

    def __init__(self):
        self.planner = PlannerAgent()
        self.evaluator = EvaluatorAgent()
        self.adaptation = AdaptationAgent()

    def create_plan(
        self,
        tasks: list[dict],
    ) -> list[dict]:
        """
        Generate a prioritized learning plan.
        """

        return self.planner.rank_tasks(tasks)

    def process_session(
        self,
        questions_attempted: int,
        correct_answers: int,
        confidence: float,
        time_spent_minutes: int,
        retention_risk: float,
        current_duration: int,
    ) -> dict:
        """
        Process a completed study session.

        The result flows through:

        Evaluation → Adaptation → Replanning
        """

        # -----------------------------------------
        # Stage 1: Evaluate the study session
        # -----------------------------------------

        evaluation = self.evaluator.evaluate_session(
            questions_attempted=questions_attempted,
            correct_answers=correct_answers,
            confidence=confidence,
            time_spent_minutes=time_spent_minutes,
        )

        # -----------------------------------------
        # Stage 2: Adapt the future strategy
        # -----------------------------------------

        adaptation = self.adaptation.adapt(
            accuracy=evaluation["accuracy"],
            retention_risk=retention_risk,
            current_duration=current_duration,
        )

        # -----------------------------------------
        # Stage 3: Prepare for the next planning cycle
        # -----------------------------------------

        return {
            "evaluation": evaluation,
            "adaptation": adaptation,
            "loop_status": "ready_for_replanning",
        }
