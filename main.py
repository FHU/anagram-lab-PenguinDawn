
def anagram(input1, input2):
    #variables
    list1 = []
    list2 = []
    endValue = True

    #lower the strings
    string1 = input1.lower()
    string2 = input2.lower()
        
    #create lists
    for x in string1:
        if x != " ":
            list1.append(x)

    for y in string2:
        if y != " ":
            list2.append(y)
    #sort lists
    list1.sort()
    list2.sort()

    #catch empty strings
    if input1 == " ":
        endValue = False
    
    if input2 == " ":
        endValue = False

    #catch uneven lists
    if len(list1) != len(list2):
        endValue = False

    #check anagrams
    while endValue != False:

        #They are sorted lists now
        for i in range(0, len(list1) - 1):

            #see if the values are the same
            if list1[i] != list2[i]:
                endValue = False

    #return the value stored in endValue
    return endValue



   #Do anagram
if __name__ == '__main__':
    input1 = input()
    input2 = input()
    print(anagram(input1, input2))
