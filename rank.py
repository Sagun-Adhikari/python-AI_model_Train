# this program tells you rank of student just assuming each studnet gets unique marks in fifference of 10
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# uploading data
data={
    "marks":[10,20,30,40,50,60,70,80,90,100],
"ranks":[10,9,8,7,6,5,4,3,2,1]
}
df=pd.DataFrame(data)

# split data into input and result
x=df[["marks"]]
y=df["ranks"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

# model training
model=LogisticRegression()
model.fit(x_train,y_train)

# test the model
predictions=model.predict(x_test)
print("Predictions on test set:",predictions)

# test new student marks
newmarks=[[70],[20],[90]]
newprediction=model.predict(newmarks)
print("\nNew Predictions (70, 20, 90):",newprediction)
