# prophet-bot
* Github action that reads data from hospital-occupancy-tracker repository, then runs prophet in R and gets predictions for <a href="https://jlomako.shinyapps.io/occupancy_app/">occupancy app</a>.
* Holiday effects for Quebec were added manually as prophet function <code>add_country_holidays</code> is not supported in R 4.2. (holiday package was removed from CRAN). 
* made this bot because prophet package slowed down <a href="https://jlomako.shinyapps.io/occupancy_app/">occupancy app</a> in shiny.
* deactivated old yaml and created new one with versions, still doesn't run on ubuntu because of some error with curl (in renv) 
