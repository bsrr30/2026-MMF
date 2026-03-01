# Functions go here from c03_yes_no_simple import yes_no
def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here


while True:
    want_instructions = string_check("Do you want to see the instructions ")
    print(f"you choose {want_instructions}")
    print()

