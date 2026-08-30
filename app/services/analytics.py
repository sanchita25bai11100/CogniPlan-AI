"""
Learning Analytics Engine
=========================

Transforms raw learning activity into meaningful
student intelligence signals.

The analytics engine tracks:

- mastery
- consistency
- accuracy
- learning efficiency
- retention risk
- readiness
"""

from statistics import mean


class LearningAnalytics:
    """
    Calculates high-level learning metrics from
    a student's historical study sessions.
    """

    @staticmethod
    def calculate_accuracy(
        correct_answers: int,
        questions_attempted: int,
    ) -> float:
        """
        Calculate normalized accuracy.
        """

        if questions_attempted <= 0:
            return 0.0

        accuracy = (
            correct_answers / questions_attempted
        )

        return round(
            max(0.0, min(1.0, accuracy)),
            3,
        )

    @staticmethod
    def calculate_learning_efficiency(
        correct_answers: int,
        time_spent_minutes: int,
    ) -> float:
        """
        Estimate learning efficiency as correct
        responses per minute.
        """

        if time_spent_minutes <= 0:
            return 0.0

        return round(
            correct_answers / time_spent_minutes,
            3,
        )

    @staticmethod
    def calculate_consistency(
        session_accuracies: list[float],
    ) -> float:
        """
        Measure consistency across recent sessions.

        A score closer to 1 means performance is
        relatively stable.
        """

        if not session_accuracies:
            return 0.0

        normalized = [
            max(0.0, min(1.0, value))
            for value in session_accuracies
        ]

        average = mean(normalized)

        variance = mean(
            [
                (value - average) ** 2
                for value in normalized
            ]
        )

        consistency = 1.0 - min(
            variance * 4,
            1.0,
        )

        return round(
            consistency,
            3,
        )

    @staticmethod
    def calculate_readiness(
        mastery: float,
        confidence: float,
        consistency: float,
        retention_risk: float,
    ) -> float:
        """
        Calculate an overall readiness score.

        Higher readiness indicates that a learner
        is more prepared to progress.
        """

        readiness = (
            mastery * 0.40
            + confidence * 0.20
            + consistency * 0.20
            + (1.0 - retention_risk) * 0.20
        )

        return round(
            max(0.0, min(1.0, readiness)),
            3,
        )

    def generate_insights(
        self,
        mastery: float,
        confidence: float,
        retention_risk: float,
        session_accuracies: list[float],
    ) -> dict:
        """
        Generate a compact intelligence report
        for the learner and planning agents.
        """

        consistency = self.calculate_consistency(
            session_accuracies
        )

        readiness = self.calculate_readiness(
            mastery=mastery,
            confidence=confidence,
            consistency=consistency,
            retention_risk=retention_risk,
        )

        if readiness >= 0.80:
            status = "READY_TO_ADVANCE"
        elif readiness >= 0.60:
            status = "STRENGTHEN"
        elif readiness >= 0.40:
            status = "PRACTICE"
        else:
            status = "REVISIT"

        return {
            "mastery": round(mastery, 3),
            "confidence": round(confidence, 3),
            "retention_risk": round(
                retention_risk,
                3,
            ),
            "consistency": consistency,
            "readiness": readiness,
            "recommended_action": status,
        }
