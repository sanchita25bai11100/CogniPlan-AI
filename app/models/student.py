"""
Student Intelligence Model
==========================

Maintains an evolving representation of a learner's
knowledge, confidence, retention risk, and study behavior.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class StudentProfile:
    """
    Represents the current learning state of a student.
    """

    student_id: str
    name: str

    # Knowledge state
    mastery: Dict[str, float] = field(default_factory=dict)

    # How confident the student feels about each subject
    confidence: Dict[str, float] = field(default_factory=dict)

    # Probability that previously learned material may be forgotten
    retention_risk: Dict[str, float] = field(default_factory=dict)

    # Learning behavior
    study_streak: int = 0
    completed_sessions: int = 0
    average_accuracy: float = 0.0

    def update_performance(
        self,
        subject: str,
        accuracy: float,
    ) -> None:
        """
        Update the learner model after a study session.

        A weighted update is used so that recent performance
        influences mastery while previous knowledge is retained.
        """

        # Keep accuracy between 0 and 1.
        accuracy = max(0.0, min(1.0, accuracy))

        previous_mastery = self.mastery.get(subject, 0.0)

        # Recent performance has a 30% influence.
        self.mastery[subject] = (
            0.7 * previous_mastery
            + 0.3 * accuracy
        )

        # Confidence follows the latest observed performance.
        self.confidence[subject] = accuracy

        # Lower mastery means greater retention risk.
        self.retention_risk[subject] = (
            1.0 - self.mastery[subject]
        )

        self.completed_sessions += 1

        # Update overall accuracy using a running average.
        self.average_accuracy = (
            (
                self.average_accuracy
                * (self.completed_sessions - 1)
            )
            + accuracy
        ) / self.completed_sessions

    def get_learning_state(
        self,
        subject: str,
    ) -> dict:
        """
        Return the current intelligence state for a subject.
        """

        return {
            "subject": subject,
            "mastery": round(
                self.mastery.get(subject, 0.0),
                3,
            ),
            "confidence": round(
                self.confidence.get(subject, 0.0),
                3,
            ),
            "retention_risk": round(
                self.retention_risk.get(subject, 1.0),
                3,
            ),
        }
