# prophet-bot

[![get-predictions v2](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_v2.yml/badge.svg)](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_v2.yml)

* Github action that reads data from <a href="https://github.com/jlomako/hospital-occupancy-tracker">hospital-occupancy-tracker</a> repository, then runs prophet in R and gets predictions for shiny <a href = "https://github.com/jlomako/Montreal-ER">Montreal-ER</a> app.
* Holiday effects for Quebec were added manually as prophet function <code>add_country_holidays</code> is not supported in R 4.2. (holiday package was removed from CRAN). 
* deactivated old yaml and created new one with versions, still doesn't run on ubuntu because of some error with curl (in renv) 
