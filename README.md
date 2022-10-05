# prophet-bot
Github action that reads data from my repository: hospital-occupancy-tracker, then runs prophet in R and gets predictions for <a href="https://jlomako.shinyapps.io/occupancy_app/">occupancy app</a>.
Holiday effects for quebec where added manually as prophet function <code>add_country_holidays</code> is not supported in R 4.2. (holiday package was removed from CRAN). I made this bot because prophet package slowed down <a href="https://jlomako.shinyapps.io/occupancy_app/">occupancy app</a> in shiny
