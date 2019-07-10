import pandas as pd
def SecondsToDuration(seconds):
    days = seconds // 86400
    hours = (seconds - days * 86400) // 3600
    minutes = (seconds - days * 86400 - hours * 3600) // 60
    seconds = seconds - days * 86400 - hours * 3600 - minutes * 60
    if (len(str(days)) == 1):
        days = "0" + str(days)
    if (len(str(hours)) == 1):
        hours = "0" + str(hours)
    if (len(str(minutes)) == 1):
        minutes = "0" + str(minutes)
    if (len(str(seconds)) == 1):
        seconds = "0" + str(seconds)
    formatted_duration = str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return formatted_duration


seconds_input = 334751
result = SecondsToDuration(seconds_input)
print(result)

