import re

with open('access_log2.txt', 'r') as file:
    step = 0
    for lines_of_file in file.readlines():
        pattern = r".+(((((07/Mar/2004:10:49|5[0-9]:(2[89]|[3-5][0-9])|(07/Mar/2004:(1[1-9]|2[0-4])):\d\d:\d\d)" \
                  r"|(08/Mar/2004:([1-9]|1[0-8]):\d\d:\d\d))|(08/Mar/2004:([1-9]|1[0-8]):\d\d:\d\d))|" \
                  r"(08/Mar/2004:19:([0-9]|[12][0-9]|3[0-5]):([0-9]|[12][0-9]|3[0-5])))).+HEAD.+200"
        if re.search(pattern, lines_of_file):
            step = step + 1
            print(lines_of_file)
print("Amount of requests : " + str(step))
# range: 07/Mar/2004:10:49:28 - 08/Mar/2004:19:35:11
