'''
@author: Laura Peng
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''

    movie = r'/Users/mqw/Downloads/assign6f22-recommender/data/books.txt'
    data = open(movie, "r")

    movies = []
    ret = {}
    val = data.readline().split(",")

    count =1
    while (count < len(val)):
        movies.append(val[count])
        count += 2

    print (movies)


    for x in data:
        name = x[:x.find(",")]


        if name not in ret:
            ret[name] = []


    for (x, y) in ret.items():
        for a in range(len(movies)):
            ret[x].append(0)
    # trying to find the ratings and adding that to ret


    name = ""
    data = open(movie, "r")

    for x in data:

        val = []
        new = x.split(",")
        name = new[0]
        count =2
        while (count<len (new)):
            val.append (int (new[count]))
            count+=2
        ret [name]= val


    return (movies, ret)

    pass

if __name__ == '__main__':
    print (getdata())