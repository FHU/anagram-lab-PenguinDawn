

def anagram(input1, input2):
    list1 = []
    list2 = []
    end = True


    
    if input1 == " ":
        end = False
        return False
    
    elif input2 == " ":
        end = False
        return False
    
    else:

        for x in input1:

            if x == " ":
                pass
            else:
                list1.append(x)

        for y in input2:

            if y == " ":
                pass
            else:
                list2.append(y)
        
        list1.sort()
        list2.sort()

        if len(list1) != len(list2):
            end = False
            return False

        for z in range(0, len(list1)):

            if list1[z] != list2[z]:
                end = False
                return False
            else:
                end == True
        
        if end == True:
            return end
            
                


    

if __name__ == '__main__':
    input1 = input()
    input2 = input()
    string1 = input1.lower()
    string2 = input2.lower()
    print(anagram(string1, string2))
    