# Screen Time Analysis is the task of analyzing and creating a report on which application and websites are used by the user for how much time. Apple devices have one of the best ways of creating a screen time report.
import pandas as pd
import plotly.express as px

data = pd.read_csv("Screentime-App-Details.csv")

# required_columns = {"Notifications", "Usage"}
# if not required_columns.issubset(data.columns):
#     raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

'''print(data.head())
print(data.isnull().sum())
print(data.describe())
figure = px.bar(data_frame=data, x="Date", y="Usage", color="App", title='Usage Poltly Library to show Graph')
figure = px.bar(data_frame=data, x="Date", y="Notifications", color="App", title='Analysis of Graph Output as Notificaations along with Date')
figure = px.bar(data_frame=data, x="Date", y="Times opened", color="App", title='Usage Number of Time the App Opened at that Date')'''
figure = px.scatter(data_frame=data, x = "Notifications", y="Usage", size="Notifications", trendline="ols", title="Relationship Between Number of notifications and amount of usage")
figure.show()