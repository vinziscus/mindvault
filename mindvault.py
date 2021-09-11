import os.path

print("Welcome to MindVault")
# start loop
while True:
    # Navigation bar
    a = input(""" ----------------
    new - n \noverwrite - o \nappend - ap \nview - v \nsearch - sc
    """)
    # directory where markdown files are stored
    save_path = 'C:/Users/Christopher/Desktop/NShellFiles'

    # creating new note
    if a == "n":
        print("creating new note")
        name_of_file = input("title: ")
        # open new markdown file
        completeName0 = os.path.join(save_path, name_of_file + ".md")
        new_file = open(completeName0, "w")
        # embed text in markdown file
        c = ""
        written_file = new_file.write(c)
        with open(completeName0, "r") as myfile:
            data = myfile.read()
        cba = input("text:")
        append_note = open(completeName0, "a")
        append_note.write(cba)
        append_note.close()
        print("finished creating " + name_of_file)


    # overwrite note
    elif a == "o":
        print("overwrite note")
        name_of_file1 = input("title: ")
        # print text in file
        completeName1 = os.path.join(save_path, name_of_file1 + ".md")
        with open(completeName1, "r") as myfile:
            data = myfile.read()
            print(data)
        # write new text in k
        new_data = input("new text: ")
        with open(completeName1, "w") as myfile:
            myfile.write(new_data)

    # view note
    elif a == "v":
        print("view note")
        name_of_file2 = input("title: ")
        completeName2 = os.path.join(save_path, name_of_file2 + ".md")
        with open(completeName2, "r") as myfile:
            data = myfile.read()
            print(data)

    # append note
    elif a =="ap":
        print("append note")
        name_of_file3 = input("title:")
        completeName3 = os.path.join(save_path, name_of_file3 + ".md")
        with open(completeName3, "r") as myfile:
            data = myfile.read()
            print(data)
        cba = input("append text:")
        append_note = open(completeName3, "a")
        append_note.write(cba)
        append_note.close()

    # search for string in all files
    import os

    if a == "sc":
        # ask for tag to search for
        searching_for = input("search for tag:")
        # search for tag in every file of the directory
        directory = os.listdir(save_path + "/")
        for fname in directory:
            if os.path.isfile(save_path + "/" + os.sep + fname):
                f = open(save_path + "/" + os.sep + fname, 'r')

                # print all files that contain the tag
                if searching_for in f.read():
                    print("found ''" + searching_for + "'' in file %s" % fname)

                else:
                    f.close()

    while True:
        answer = str(input('continue f/j '))
        if answer in ('f', 'j'):
            break
        print("invalid input")
    if answer == 'f':
        continue
    else:
        print("---closing program---")
        break
