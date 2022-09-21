def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)
        while response != "":
            return response
        else:
            print(error)


def int_check(question, low_num, high_num):
    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seats left".format(MAX_TICKETS - count))
    name = not_blank("Name: ", "cannot be blank")

    if name == "xxx":
        break

    age = int_check("Age: ", 12, 130)
    count += 1

if count == MAX_TICKETS:
    print("You have sold all the available tickets")
else:
    print("You have sold {} tickets. \n""There are {} places still available".format(count, MAX_TICKETS - count))
