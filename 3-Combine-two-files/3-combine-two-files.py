file1 = ""
file2 = ""
with open("sample1.txt", "r") as first_file:
    file1 = first_file.readlines()

    with open("sample2.txt", "r") as second_file:
        file2 =second_file.readlines()
        with open("sample3.txt", "w")as third_file:

            for i in range(len(file1)):
                words = file1[i].strip() + ' ' + file2[i]
                print(words.strip("\n"), file=third_file)