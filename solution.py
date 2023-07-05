def main():
    totalCombine = int(input())
    output = processResult(totalCombine)
    print(output)


def processResult(totalCombine):
    output = ""
    if (totalCombine > 0):
        size = int(input())
        data = input()
        dataArray = data.split(" ")
        result = handleData(dataArray, size - 1)
        output += str(result)
        if (totalCombine > 1):
            output += '\n'
        output += processResult(totalCombine - 1)
    return output



def handleData(dataArray, index):
    if (index >= 0):
        value = int(dataArray[index])
        return handleData(dataArray, index - 1) + pow(value, 2) if value > 0 else handleData(dataArray, index - 1)
    else:
        return 0


if __name__== "__main__":
    main()