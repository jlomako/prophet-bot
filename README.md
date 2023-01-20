# prophet-bot

[![get-predictions-py](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_Python.yml/badge.svg)](https://github.com/jlomako/prophet-bot/actions/workflows/prophet_bot_Python.yml)

Github action that reads data from <a href="https://github.com/jlomako/hospital-occupancy-tracker">hospital-occupancy-tracker</a> repository, then runs prophet and calculates predictions for <a href = "https://github.com/jlomako/Montreal-ER">Montreal-ER</a> web app (visit app <a href="https://jlomako.shinyapps.io/Montreal_ER/">here</a>)

### Notes:
* data is updated daily around 17:25 utc
* Holiday effects for Quebec were added manually
* made some changes to the bot to make it faster, now runs in python instead of R
* R files have been moved to another repository, see <a href = "https://github.com/jlomako/prophet-bot-R">prophet-bot-R</a>
