import datetime
import webbrowser

answer_format = "%m/%d"
link_format = "%b_%d"
link = "https://en.wikipedia.org/wiki/{}"

while True:
    answer = input("What date would you like to learn about? Please use MM/DD format. Enter 'quit' to QUIT.")
    if answer.upper == "QUIT":
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(webbrowser.open(output))
    except ValueError:
        print("That is not a valid date, please try again.")
