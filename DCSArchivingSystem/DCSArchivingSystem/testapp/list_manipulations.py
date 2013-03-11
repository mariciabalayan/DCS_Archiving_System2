def remove_first_characters(list):
        for x in range(len(list)):
                list[x] = list[x][1:]

def subtract_list(minuend, subtrahend):
        for x in minuend[:]:
                if x in subtrahend:
                        minuend.remove(x)
