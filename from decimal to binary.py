integ = 715337389448723032932884436
print("Decimal form: ", integ)

x_bin_str = bin(integ)
x_bin_str = x_bin_str[2::]
print("Binary string form: ", x_bin_str)

x_bin_list = []
for i in range(len(x_bin_str)):
    x_bin_list.append(int(x_bin_str[i]))
print("Binary list form: ", x_bin_list)
