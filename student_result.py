import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# upload dataset
df=pd.read_csv(r"C:\Users\Flex\OneDrive\Desktop\python\StudentsPerformance.csv")
print(df)

# split
X = df[["math score"]]  # feature
y = df["math score"].apply(lambda x: 1 if x >= 50 else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model training
model = LogisticRegression()
model.fit(X_train, y_train)

# test the model
predictions = model.predict(X_test)
print("Predictions on test set:", predictions)
print("Actual values:          ", y_test.values)


accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Step 8: Predict New Student
new_student = [[45]]  # Math score
new_prediction = model.predict(new_student)
print("Prediction for new student:", "Pass" if new_prediction[0] == 1 else "Fail")