# prophet-bot

[![get-predictions-py](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_Python.yml/badge.svg)](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_Python.yml)

* Github action that reads data from <a href="https://github.com/jlomako/hospital-occupancy-tracker">hospital-occupancy-tracker</a> repository, then runs prophet in R and gets predictions for Shiny <a href = "https://github.com/jlomako/Montreal-ER">Montreal-ER</a> app (visit app <a href="https://jlomako.shinyapps.io/Montreal_ER/">here</a>)
* Holiday effects for Quebec were added manually as prophet function <code>add_country_holidays</code> is not supported in R 4.2. (holiday package was removed from CRAN). 
* deactivated old yaml and created new one with versions, still doesn't run on ubuntu because of some error with curl (in renv) 
* doesn't work on ubuntu with <code>DESCRIPTON</code> either
* runs every 2nd day at 1:25 pm local time
* re-wrote the script in python, added requirements.txt, added new yml (runs on ubuntu) -- bot runs much faster now :)
