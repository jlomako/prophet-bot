# prophet-bot
github action that runs prophet in R and gets predictions for <a href="https://jlomako.shinyapps.io/occupancy_app/">occupancy app</a>.
Holiday effects for quebec where added manually as prophet function <code>add_country_holidays</code> is not supported in R 4.2. (since holiday package was removed from CRAN?)
