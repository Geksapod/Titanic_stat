import pandas as pd
import matplotlib.pyplot as plt


titanic = pd.read_csv("titanic.csv")
titanic.columns = ["No", "Name", "Class", "Age", "Sex", "Survived", "SexCode"]

# print(titanic.head(), titanic.tail())

survived = (titanic.loc[titanic["Survived"] == 1])

# print(survived.loc[titanic["Age"] == (survived["Age"]).min()])
# print(survived.loc[titanic["Age"] == (survived["Age"]).max()])
# print(survived.describe())

survived_women = titanic[(titanic["Survived"] == 1) & (titanic["Class"] == "1st") & (titanic["Sex"] == "female")]

print(survived_women.loc[survived_women["Age"] == (survived_women["Age"]).min()])
print(survived_women.loc[survived_women["Age"] == (survived_women["Age"]).max()])
print((survived_women["Survived"]).count())


histogram = (titanic["Age"]).hist()
histogram_sur = (survived["Age"]).hist()
histogram.set_title("Age of all passengers and survived")
histogram.set_xlabel("Age")
histogram.set_ylabel("Number of survived")

labels = ["All", "Survived"]
plt.legend(labels)

plt.show()
