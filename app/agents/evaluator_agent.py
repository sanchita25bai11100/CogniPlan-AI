"""
Performance Evaluation Agent
============================

Analyzes the outcome of a learning session and converts
the results into measurable learning signals.
"""


class EvaluatorAgent:
    """
    Evaluates a student's study-session performance.

    The agent considers:
    - accuracy
    - confidence
    - time efficiency

    It then recommends the next learning action.
    """

    def evaluate_session(
        self,
        questions_attempted: int,
        correct_answers: int,
        confidence: float,
        time_spent_minutes: int,
    ) -> dict:
        """
        Evaluate one completed study session.
        """

        if questions_attempted <= 0:
            raise ValueError(
                "questions_attempted must be greater than zero"
            )

        if correct_answers < 0:
            raise ValueError(
                "correct_answers cannot be negative"
            )

        if correct_answers > questions_attempted:
            raise ValueError(
                "correct_answers cannot exceed questions_attempted"
            )

        if time_spent_minutes < 0:
            raise ValueError(
                "time_spent_minutes cannot be negative"
            )

        # Calculate accuracy.
        accuracy = (
            correct_answers / questions_attempted
        )

        # Calculate learning efficiency.
        efficiency = (
            correct_answers / time_spent_minutes
            if time_spent_minutes > 0
            else 0
        )

        # Keep confidence within the valid range.
        confidence = max(
            0.0,
            min(1.0, confidence)
        )

        return {
            "accuracy": round(accuracy, 3),
            "confidence": round(confidence, 3),
            "efficiency": round(efficiency, 3),
            "recommendation": self._generate_recommendation(
                accuracy
            ),
        }

    @staticmethod
    def _generate_recommendation(
        accuracy: float,
    ) -> str:
        """
        Convert performance into a learning recommendation.
        """

        if accuracy < 0.50:
            return "REVISIT"

        if accuracy < 0.75:
            return "PRACTICE"

        if accuracy < 0.90:
            return "STRENGTHEN"

        return "ADVANCE"
