import os
# open files in read mode
accuracy = open('accuracy.txt', 'r')
input = open('input.txt', 'r')
accu_report_file = open('accuracy_report.txt', 'r')

# save data in variables
acc_data = accuracy.read()
input_data = input.read()
accu_report_data = accu_report_file.read()

# split the data
input_list = input_data.split('\n')
accu_report_split_data = accu_report_data.split('\n')

if float(acc_data) < 96:
    # list comprehension with exclude last
    input_list = [ int(input_list[i]) + 5 if i == 4  else int(input_list[i]) * 2  for i in range(5) ]
    print(input_list)
    input.close()
    print("Successfully twick the values!")

elif float(acc_data) < 97.75:
    # list comprehension with exclude last
    input_list = [ int(input_list[i]) + 5 if i == 4  else int(input_list[i]) * 2  for i in range(5) ]
    print(input_list)
    input.close()
    print("Successfully twick the values!")

else:
	print("values are not twicked!")
	input.close()

with open('input.txt', 'w') as file_handler:
    for item in input_list:
        file_handler.write("{}\n".format(item))

os.system('cat input.txt')

# accuracy report file
acc_report = accu_report_split_data
acc_report.append(acc_data)
accu_report_file.close()

with open('accuracy_report.txt', 'w') as file:
    for item in acc_report:
        file.write("{}\n".format(item))

os.system('cat accuracy_report.txt')