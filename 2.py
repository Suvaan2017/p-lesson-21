test_dict = {'condingal': 2, 'is': 2, 'fun': 2}
print ("the original dictoinary:", str(test_dict))
k= 2
res = 0 
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
        print ("frequency of k is:" + str(res))
