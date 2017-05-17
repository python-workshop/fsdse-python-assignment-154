class InsertionSort(object):

    def build(data):
        if data is None:
            return False
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
        return data

    # result= build([2])
    # print(result)