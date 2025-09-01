# src/models/train_model.py

import pickle
from sklearn.tree import DecisionTreeClassifier

# Dummy dataset (features = answers to 5 questions)
# Each answer is encoded: Yes=1, No=0
X = [
    [1, 1, 0, 0, 1],  # loves coding + data → Data Scientist
    [1, 1, 0, 0, 0],  # logical + coding → Software Engineer
    [0, 0, 1, 0, 0],  # creative → Designer
    [0, 0, 0, 1, 0],  # likes helping → Teacher
    [1, 0, 0, 0, 1],  # logical + data → Analyst
    [0, 1, 0, 0, 1],  # coding + data → AI Engineer
]

# Target labels (careers)
y = [
    "Data Scientist",
    "Software Engineer",
    "Designer",
    "Teacher",
    "Analyst",
    "AI Engineer"
]

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("career_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as career_model.pkl")
