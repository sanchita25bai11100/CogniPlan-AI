"""
Adaptive Planning Agent
=======================

Determines what a learner should study next by combining
knowledge gaps, retention risk, exam urgency, and difficulty.
"""

from dataclasses import dataclass


@dataclass
class LearningTask:
    """
    Represents a single learning task.
    """

    subject: str
    topic: str
    difficulty: float
    exam_urgency: float
    estimated_minutes: int


class PlannerAgent:
    """
    Adaptive planning engine.

    The planner does not simply create a timetable.
    It prioritizes learning tasks based on the learner's
    current cognitive state.
    """

    def calculate_priority(
        self,
        mastery: float,
        retention_risk: float,
        exam_urgency: float,
        difficulty: float,
    ) -> float:
        """
        Calculate the priority of a learning task.

        Higher priority means the task should be studied sooner.
        """

        # A low mastery value represents a large knowledge gap.
        knowledge_gap = 1.0 - mastery

        priority = (
            knowledge_gap * 0.35
            + retention_risk * 0.25
            + exam_urgency * 0.25
            + difficulty * 0.15
        )

        return round(priority, 3)

    def rank_tasks(
        self,
        tasks: list[dict],
    ) -> list[dict]:
        """
        Rank learning tasks from highest to lowest priority.
        """

        for task in tasks:

            task["priority"] = self.calculate_priority(
                mastery=task.get("mastery", 0.0),
                retention_risk=task.get(
                    "retention_risk",
                    0.5,
                ),
                exam_urgency=task.get(
                    "exam_urgency",
                    0.5,
                ),
                difficulty=task.get(
                    "difficulty",
                    0.5,
                ),
            )

        return sorted(
            tasks,
            key=lambda task: task["priority"],
            reverse=True,
        )
