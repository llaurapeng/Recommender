'''
@author: Laura Peng
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    movie = r'/Users/mqw/Downloads/assign6f22-recommender/data/movies.txt'
    data = open (movie, "r")

    movies = []
    ret = {}

    for x in data:
        movie  = x[x.find(",") + 1:x.rfind(",")]
        if movie not in movies:
            movies.append(x[x.find(",") + 1:x.rfind(",")])

        name = x[:x.find (",")]

        if name not in ret:
            ret [name]=[]


    movies = sorted (movies)


    for (x,y) in ret.items():
        for a in range (len (movies)):
            ret[x].append (0)
    #trying to find the ratings and adding that to ret
    data = open ("movie.txt", "r")

    name = ""
    for x in data:
        name = x[:x.find(",")]
        movie = x[x.find(",") + 1:x.rfind(",")]
        rate = x[x.rfind (",")+1:]
        ind = movies.index (movie)
        ret[name][ind]=int (rate)

    return (movies, ret)


if __name__ == '__main__':
    print (getdata())