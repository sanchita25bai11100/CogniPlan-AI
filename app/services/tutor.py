"""
CogniPlan AI Tutor
==================

A personalized learning assistant that combines
retrieved study material with the learner's current
performance state.

The tutor supports:
- concept explanations
- revision guidance
- practice generation
- personalized feedback
"""

from app.services.knowledge_engine import KnowledgeEngine


class AITutor:
    """
    Personalized tutoring engine.

    The tutor uses the learner's knowledge base and
    learning state to generate focused study guidance.
    """

    def __init__(self, knowledge_engine: KnowledgeEngine):
        self.knowledge_engine = knowledge_engine

    def explain(
        self,
        question: str,
        mastery: float = 0.5,
        confidence: float = 0.5,
    ) -> dict:
        """
        Generate a personalized explanation using
        retrieved learning material.
        """

        context = self.knowledge_engine.build_context(
            query=question,
            top_k=3,
        )

        if mastery < 0.40:
            learning_level = "beginner"
        elif mastery < 0.70:
            learning_level = "developing"
        else:
            learning_level = "advanced"

        return {
            "question": question,
            "learning_level": learning_level,
            "mastery": round(mastery, 3),
            "confidence": round(confidence, 3),
            "retrieved_context": context,
            "instruction": self._build_instruction(
                question=question,
                learning_level=learning_level,
                context=context,
            ),
        }

    @staticmethod
    def _build_instruction(
        question: str,
        learning_level: str,
        context: str,
    ) -> str:
        """
        Build a grounded tutoring instruction.

        This prompt can later be passed directly to
        an LLM provider without changing the rest
        of the architecture.
        """

        return f"""
You are CogniPlan, an adaptive AI tutor.

Student level: {learning_level}

Student question:
{question}

Relevant study material:
{context}

Teaching instructions:
1. Explain the concept at the student's current level.
2. Use the provided study material as the primary context.
3. Break difficult ideas into simple steps.
4. Give one practical example.
5. End with a short question to test understanding.

Do not introduce unsupported facts when the supplied
study material is sufficient to answer the question.
""".strip()
