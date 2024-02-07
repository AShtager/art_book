def sorted_page(*text):
    count_line = {}
    number_line = 1
    count = 0 
    for i in text:
        with open(i, encoding="utf-8") as f:
            for i in f:
                count += 1
            count_line[count] = f"{number_line}.txt"
            count = 0
            number_line += 1
    line_sorted = dict(sorted(count_line.items()))
    for i in line_sorted.items():
        with open(i[1], encoding='utf-8') as f_1, open("book.txt", "a", encoding="utf-8") as f_2:
            f_2.write(i[1])
            f_2.write("\n")
            f_2.write(str(i[0]))
            f_2.write("\n")
            for line in f_1:
                f_2.write(line)
            f_2.write("\n")
            

sorted_page("1.txt", "2.txt", "3.txt")