import pickle
from src.model.questions import QUESTIONS  # your questions.py

# Load the trained decision tree model
with open("src/model/career_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_career(user_answers: list) -> str:
    """
    user_answers: list of integers corresponding to choices for each question
    Returns: predicted career path as string
    """
    if len(user_answers) != len(QUESTIONS):
        return f"Error: Expected {len(QUESTIONS)} answers, got {len(user_answers)}"

    # Decision tree expects 2D array
    prediction = model.predict([user_answers])
    return prediction[0]

# Example usage
if __name__ == "__main__":
    # Sample answers for testing (replace with actual user input)
    sample_answers = [1, 0, 2, 1]  # Each number corresponds to the selected option index
    career = predict_career(sample_answers)
    print(f"Predicted Career Path: {career}")
