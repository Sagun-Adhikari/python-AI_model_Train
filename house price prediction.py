import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression     
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df=pd.read_csv(r"C:\Users\Flex\OneDrive\Desktop\python\house-prices-advanced-regression-techniques\train.csv")

# split
feature=features = ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath"]
x=df[features]  # feature
y=df["SalePrice"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# model training
model=LogisticRegression()
model.fit(x_train, y_train)

# test the model
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# new data for prediction
new_house = pd.DataFrame({
    "OverallQual": [7],
    "GrLivArea": [2000],
    "GarageCars": [2],
    "TotalBsmtSF": [1000],
    "FullBath": [2]
})

predicted_price = model.predict(new_house)
print(f"Predicted Sale Price for the new house: ${predicted_price[0]:.2f}")