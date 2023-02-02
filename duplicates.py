array=[1,2,3,6,5,6,5,7,8]
output=[]
for ele in array:
    if ele not in output:
        output.append(ele)
for i in range(0, len(output)):
    for j in range(i+1, len(output)):
        if(output[i] > output[j]):
            temp = output[i];
            output[i] = output[j];
            output[j] = temp;
print(output)



