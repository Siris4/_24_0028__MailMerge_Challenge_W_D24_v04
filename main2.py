
PLACEHOLDER = "[name]"

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

#TODO: Get ahold of the file we need to start with that has the data to extract from, must scan the file, and generate individual line items as it's own item in a list:
with open("Input/Names/invited_names.txt") as invited_names_file:
    names = invited_names_file.readlines()

#then, we need to get ahold of where we plan on taking this list to, clean the data/prepare the data to function and look well aesthetically (in this case, we will be formatting the names to not include \n after) and to replace each Placeholder with the stripped name that was from the first list)
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)

        #when you open a file, that does not exist, Python will go ahead and create that file as a new one.
# then we have to write into the file that we indicate (in this case, it is a new file name, so Python creates a new file, and places all the stripped data into the proper spots, and resaves that as the newly created separate file):
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)





    # for iteration in range(8):
    #     print(names[iteration])




# with open("C:/Users/guber/Desktop/CODEX-~1/Python/100DAY~1/__LEAR~1/DAY24S~1/MAILME~1/Input/Names/invited_names.txt", mode="r") as invited_names_file:
#     unstripped_names_in_list_form = invited_names_file.readlines()
#     invited_names = [name.strip() for name in unstripped_names_in_list_form]
#     print(f"unstripped_names_in_list_form is: {unstripped_names_in_list_form}")
#     print(f"invited_names is: {invited_names}")


# with open("C:/Users/guber/Desktop/CoDex - Code Index - GitHub for HDD/Python/100 Days of Code - Projects Code - in PyCharm/__Learning Only Files - Only Mini-Projects here__/Day 24 Start - File Saving System inside Python/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="w") as write_letter_file:
#     for iteration in range(8):
#         x = invited_names[iteration].replace("[name]", invited_names[iteration])

    # contents = write_letter_file.write("\nanything you want to write here")
    # print(contents)


    # for iteration in range(8):
    #     x = invited_names[iteration].replace("[name]", invited_names[iteration])

    # with open("my_file.txt", mode="w") as file:





    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# x = txt.replace("bananas", "apples")

        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# with open("C:/Users/guber/Desktop/CODEX-~1/Python/100DAY~1/__LEAR~1/DAY24S~1/MAILME~1/Input/Names/invited_names.txt", mode="r") as invited_names_file:
#     for line in invited_names_file:

