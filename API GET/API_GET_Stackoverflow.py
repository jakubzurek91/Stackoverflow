import datetime
import json
import requests
import webbrowser
import time

start = time.perf_counter()
tag = input("enter searching tag: ")
operation = input(" search by date press 1 \n search period from today press 2 \n")
score = input("min score: ")
params = {
        "site": "stackoverflow.com",
        "sort": "votes",
        "order": "desc",
        "fromdate": None,
        "todate": None,
        "tagged": tag,
        "min": score}

if operation == "1":
    from_date, to_date = input("from date (yyy-mm-dd): "), input("to date (yyy-mm-dd): ")
    params["fromdate"] = from_date
    params["todate"] = to_date

elif operation == "2":
    period = input("period (days): ")
    params["fromdate"] = datetime.date.today() - datetime.timedelta(int(period))
    params["todate"] = datetime.date.today()


r = requests.get("http://api.stackexchange.com/2.2/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
end = time.perf_counter()
print(f"operation time:  {end-start:.2f}s")

