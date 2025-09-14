# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 2. Load dataset (change path if needed)
data = pd.read_csv(r"C:\Users\Flex\OneDrive\Desktop\python\titanic\train.csv")

# 3. Select features + target
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
df = data[features + ["Survived"]]

# 4. Handle missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# 5. Convert categorical variables to numbers
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

# 6. Split into features (X) and target (y)
X = df.drop("Survived", axis=1)
y = df["Survived"]

# 7. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. Train Logistic Regression model
model = LogisticRegression(max_iter=500)  # increased max_iter to avoid convergence warnings
model.fit(X_train, y_train)

# 9. Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 10. (Optional) Check first 10 predictions
print("First 10 Predictions:", y_pred[:10])
print("First 10 Actual:", y_test.values[:10])
