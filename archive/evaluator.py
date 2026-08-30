This file evaluates the user’s answers by comparing them with the correct answer. It uses simple keyword matching to calculate a score, simulating basic natural language processing.
# evaluator.py

def evaluate_answer(student_answer, model_answer):
    stop_words = {"is", "a", "the", "and", "of", "to", "in"}

    student_words = set(student_answer.lower().split()) - stop_words
    model_words = set(model_answer.lower().split()) - stop_words

    matched = student_words.intersection(model_words)

    if len(model_words) == 0:
        return 0

    score = (len(matched) / len(model_words)) * 10

    return round(score, 2)
