def deleteLeftLineSelect(leftLine,lineToSelect):
    """Deletes integers near leftLine number.

    Args:
        leftLine: an integer has been selected for the left line of a current line
        lineToSelect: a list indicating integers which can be chosen before deleting

    Returns:
        None 
    """

    if leftLine in lineToSelect:
        lineToSelect.remove(leftLine)
    if leftLine+1 in lineToSelect:
        lineToSelect.remove(leftLine+1)
    if leftLine-1 in lineToSelect:
        lineToSelect.remove(leftLine-1)

def selectLine(lineSelected,lineToSelect):
    """Selects an integer from a list of integers which can be chosen.

    Args:
        lineSelected: an integer which will be selected for the current line
        lineToSelect: a list indicating integers which can be chosen

    Returns:
        None
    """

    for i in  lineSelected:
        if i in lineToSelect:
            lineToSelect.remove(i)
    if len(lineToSelect)>1:
        lineSelected.append(lineToSelect[1])
        lineToSelect.remove(lineToSelect[1])
    elif len(lineToSelect)>0:
        lineSelected.append(lineToSelect[0])
        lineToSelect.remove(lineToSelect[0])


lineSelected=[1]
lineToSelect=[]

for i in range(1,9):

    lineToSelect=[1,2,3,4,5,6,7,8]
    deleteLeftLineSelect(lineSelected[-1],lineToSelect)
    print("deleteLeftLineSelect:","lineToSelect",lineToSelect,"lineSelected",lineSelected)
    selectLine(lineSelected,lineToSelect)
    print("lineToSelect", lineToSelect, "lineSelected", lineSelected)
    print("selectLine:", "lineToSelect", lineToSelect, "lineSelected", lineSelected)
    if len(lineSelected)<8 and lineToSelect==[]:
        print("The method is invalid.")
        break

# print the graph
for i in range(0,8):
    for j in range(0,8):
        if lineSelected[j]==i+1:
            print("|Q",end="")
        else:
            print("| ",end="")
    print("|")











