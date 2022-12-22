import pandas as pd
from prophet import Prophet

# read in data
url = "https://github.com/jlomako/hospital-occupancy-tracker/raw/main/data/hospitals.csv"
df = pd.read_csv(url)

# read in holidays for quebec
holidays = pd.read_csv("data/quebec.csv")

# create empty df
df0 = pd.DataFrame(columns = ['name', 'Date', 'yhat', 'yhat_lower', 'yhat_upper'])

# get hospital names from columns
hospitals = df.columns[1:len(df.columns)]

# loop through hospitals
for hospital in hospitals:
  # select columns date and hospital
  df_hospital = df[['Date', hospital]]

  # rename columns to be processed in prophet
  df_hospital.columns = ['ds', 'y']

  # include holidays fit the model
  m = Prophet(holidays=holidays)
  m.fit(df_hospital)

  # create future df (10 days)
  future = m.make_future_dataframe(periods=10, freq='d')
  forecast = m.predict(future)

  # add last ten entries to plot_df
  plot_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10)

  # add hospital name
  plot_df = plot_df.assign(name=hospital)

  # rename column ds to Date
  plot_df.rename(columns={'ds': 'Date'}, inplace=True)

  # transform columns with yhats to integers
  plot_df.iloc[:, 1:4] = plot_df.iloc[:, 1:4].round().astype(int)

  # sort columns
  plot_df = plot_df.reindex(columns=["name", "Date", "yhat", "yhat_lower", "yhat_upper"])

  # append data to dataframe
  df0 = df0.append(plot_df)

# write dataframe with calculations to file
df0.to_csv("data/prophet.csv", header=True, index=False)
