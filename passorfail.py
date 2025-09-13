import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# uploading dataset to a dataframe
data={
    "marks":[10,20,30,40,50,60,70,80,90,100],
    "result":["fail","fail","fail","fail","pass","pass","pass","pass","pass","pass"]
}
df=pd.DataFrame(data)

# split data into input and result
x=df[["marks"]]
y=df["result"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# model training
model = LogisticRegression()
model.fit(x_train, y_train)


# test the model
predictions = model.predict(x_test)
print("Predictions on test set:", predictions)
print("Actual values:          ", y_test.values)


# Step 6: Try new student marks
new_marks = [[4], [2], [75]]
new_predictions = model.predict(new_marks)
print("\nNew Predictions (4, 2, 75):", new_predictions)
