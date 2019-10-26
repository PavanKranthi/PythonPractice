def commonCharecters(*inpStr):
    for nameList in inpStr:
        commonChar = set(nameList[0].intersection(*nameList[1:]))
    if(len(commonChar) == 0):
        return None
    else:
        return commonChar

strList = []
while True:
    inputTxt = input("Please enter the text (enter end to stop) : ").strip()

    if inputTxt.upper() == "END":
        break
    else:
        strList.append(set(inputTxt))
# this will result you in a list of sets , idea is to find the intersection between list of sets to get the common characters
print(len(strList))
if(len(strList) == 1):
    print("commonCharecters for that string alone")
else:
    print(commonCharecters(strList))

