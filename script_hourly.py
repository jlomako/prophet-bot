import pandas as pd
from prophet import Prophet

# read in data
url = "https://github.com/jlomako/hospital-occupancy-tracker/raw/main/tables/occupancy.csv"
df = pd.read_csv(url)

# get column names and rename
col_names = ["Date", "Centre Hospitalier de l'Université de Montréal", "Centre Hospitalier de St. Mary",
             "CHU Sainte-Justine", "Hôpital de Lachine", "Hôpital de Lasalle",  "Hôpital de Verdun",
             "Hôpital Douglas", "Hôpital Maisonneuve-Rosemont", "Hôpital du Sacré-Cœur de Montréal",
             "Hôpital en Santé Mentale Albert-Prévost", "Hôpital Fleury", "Hôpital Général de Montréal",
             "Hôpital Général du Lakeshore", "Hôpital Général Juif", "Hôpital Jean-Talon", "Hôpital Notre-Dame",
             "Hôpital Royal Victoria", "Hôpital Santa Cabrini", "Institut de Cardiologie de Montréal",
             "Institut Universitaire en Santé Mentale de Montréal", "Hôpital de Montréal pour Enfants", "Total Montréal"]
# Rename columns
df.columns = col_names

# get holidays for QC
holidays = pd.read_csv("https://github.com/jlomako/prophet-bot/raw/main/data/quebec.csv")

# create empty df
df0 = pd.DataFrame(columns = ["name", "Date", "yhat", "yhat_lower", "yhat_upper"])

# get hospital names from columns
hospitals = df.columns[1:len(df.columns)]

# loop through hospitals
for hospital in hospitals:
  # select columns date and hospital
  df_hospital = df[['Date', hospital]]

  # rename columns to be processed in prophet
  df_hospital.columns = ['ds', 'y']

  # include holidays to fit the model
  m = Prophet(holidays=holidays)
  m.fit(df_hospital)

  # create future df (80 hours)
  future = m.make_future_dataframe(periods=90, freq='h')
  forecast = m.predict(future)

  # add last entries to plot_df
  plot_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(80)

  # add hospital name
  plot_df = plot_df.assign(name=hospital)

  # rename column ds to Date
  plot_df.rename(columns={'ds': 'Date'}, inplace=True)

  # transform columns with yhats to integers
  plot_df.iloc[:, 1:4] = plot_df.iloc[:, 1:4].round().astype(int).values

  # reindex
  plot_df = plot_df.reindex(columns=["name", "Date", "yhat", "yhat_lower", "yhat_upper"])

  # append data to dataframe OBS! .append replaced by pd.concat
  df0 = pd.concat([df0, plot_df])

# write dataframe with calculations to file
df0.to_csv("data/prophet_hourly.csv", header=True, index=False)
