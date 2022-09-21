def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print(error)


name = not_blank("What is your name?: ", "Sorry this can't be blank," " what is your name?")

