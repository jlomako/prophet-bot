# runs phrophet and gets predictions for occupancy app

library(dplyr)
library(prophet)

df <- vroom::vroom("https://github.com/jlomako/hospital-occupancy-tracker/raw/main/data/hospitals.csv", show_col_types = FALSE)

# create empty df
df0 <- data.frame(matrix(ncol = 5, nrow = 0))
colnames(df0) <- c("name", "Date", "yhat", "yhat_lower", "yhat_upper")
write.csv(df0, file = "data/prophet.csv", row.names = FALSE)

hospitals <- names(df[2:length(df)])

for (i in 1:(length(df)-1)) {
  df_hospital <- df %>% select(ds = Date, y = hospitals[i])
  m <- prophet(df_hospital)
  future <- make_future_dataframe(m, periods = 10, freq = "days")
  forecast <- predict(m, future)
  plot_df <- tail(forecast[c('ds', 'yhat', 'yhat_lower', 'yhat_upper')],10)
  plot_df <- plot_df %>% mutate(name = hospitals[i]) %>% 
    mutate(across(c(yhat, yhat_lower, yhat_upper), round)) %>%
    select(name, Date = ds, yhat, yhat_lower, yhat_upper)
  write.table(plot_df, "data/prophet.csv", append = T, row.names = F, col.names = F, sep = ",")
}
