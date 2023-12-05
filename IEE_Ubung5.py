a = False
b = False
c = True
d = False
v = False


term1 = (not a and not b) or (a and b)           #1
term2 = (a and (b or c)) or (b and not c)        #2
term3 = a                                        #3 false ausgabe
term4 = a or (not b and not (a or c))            #4
term5 = a and not b                              #5
term6 = c or d                                   #6
term7 = not a or not c or (not b and v)          #7
term8 = not(not a or not b or c) or (a and c)    #8

print("1:", term1)
print("2:", term2)
print("3:", term3)
print("4:", term4)
print("5:", term5)
print("6:", term6)
print("7:", term7)
print("8:", term8)
