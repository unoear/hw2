# This is a sample Python script.

month_list={ "january":"1","february":"2", "march":"3","april":"4", "may":"5", "june":"6","july":"7", "august":"8", "september":"9","october":"10", "november":"11", "december":"12"}

input_file=open('C:\\Users\\Desktop\\inputDates.txt', 'r')
output_file=open('C:\\Users\\Desktop\\parsedDates.txt','w')

for each in input_file:
    if each != "-1":
        list1=each.split()
    if len (list1) >= 3:
        month=list1 [0]
        day=list1[1]
        year=list1 [2]
    if month.lower() in month_list:
        comma=day[-1]
    if comma ==',':
        day = day[:len (day)-1]
        month_num = month_list[month.lower()]
        final = month_num+"/"+day+"/"+year

    output_file.write (final)
    output_file.write("\n")


    output_file.close()
    input_file.close()
