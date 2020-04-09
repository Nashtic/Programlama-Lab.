import sys

input,output=sys.argv[1],sys.argv[2]

def dictionary_frequency_function(dict_list_a):

    dictionary_frequency_dict = {}

    for item in dict_list_a:
        item = int(item)
        if item in dictionary_frequency_dict:
            dictionary_frequency_dict[item] = dictionary_frequency_dict[item] + 1
        else:
            dictionary_frequency_dict[item] = 1

    print(dictionary_frequency_dict)
    return dictionary_frequency_dict

def bubble_sort(bubble_list):

    n = len(bubble_list)

    for k in range(n):
        for j in range(0, n - k - 1):
            if bubble_list[j] > bubble_list[j + 1]:
                bubble_list[j], bubble_list[j + 1] = bubble_list[j + 1], bubble_list[j]

    return bubble_list

def dictionary_mode_function(list_mode):

    least_frequency = -1
    mode_value = -1

    for k_value in list_mode.keys():
        if list_mode[k_value] > least_frequency:
            least_frequency = list_mode[k_value]
            mode_value = k_value

    return mode_value,least_frequency

def list_mean_function(list_mean):

    total_value = 0
    sample = 0

    for item in list_mean:
        total_value += int(item)
        sample += 1
    return int(total_value/sample)

def find_median_value(median_list):

    median_list = bubble_sort(median_list)

    if len(median_list)%2 == 1:
        middle_value = int(len(median_list)/2)+1
        return median_list[middle_value-1]
    else:
        median_first,median_second = median_list[int(len(median_list)/2)],median_list[int(len(median_list)/2)-1]
        return (median_first+median_second)/2



with open(input+"input_hw_2.csv", "r") as file:

    a_values_array = []
    b_values_array = file.read()
    value_line = b_values_array.split(';')
    a_values_array.append(value_line)
    date = []
    bol = []

    for f in range(3, len(value_line), 3):
        bol.append(value_line[f].split("-"))

    all_months = []

    for f in range(len(bol)):
        all_months.append(int(bol[f][1]))

bubble_sort(all_months)
value_2 = dictionary_frequency_function(all_months)
last_list = [value_2[f] for f in value_2]


with open(output+"190401090_hw_2_output.txt", "w") as file:

    file.write("Medyan :"+ "" + str(find_median_value(last_list))+"\n")
    file.write("Ortalama:" + ""+ str(list_mean_function(last_list)))
