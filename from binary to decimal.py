x_bin_str = '1010111110101010011011010000001010101'

x_bin_list = []
for i in range(len(x_bin_str)):
    x_bin_list.append(int(x_bin_str[i]))

x_dec = 0
for i in range(len(x_bin_list)):
    x_dec = x_dec + x_bin_list[i]*(2**(len(x_bin_list) - i -1))
print(x_dec)