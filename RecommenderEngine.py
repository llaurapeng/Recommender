'''
@author: Laura Peng
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''

    ret = {}
    count = 0

    for x in items:
        sum = 0
        num = 0

        for (a,b) in ratings.items():
            if b[count] !=0:
                sum+=b[count]
                num+=1
        count+=1

        if num !=0:
            ret [x] = sum/num
        else:
            ret [x]=float (0)

    return sorted (ret.items(), key = lambda x: (-x[1],x[0]))

pass


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    nameLst = ratings.get(name)
    ret = {}

    for (x,y) in ratings.items():
        sum = 0
        if x != name:
            for a in range (len (y)):
                sum+=y[a]*nameLst [a]

            ret [x]=sum

    return sorted (ret.items(), key = lambda x: (-x[1],x[0]))


    pass
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''

    sim = similarities(name, ratings)


    sim = sim[:numUsers]
    sim = dict (sim)
    newRatings = {}

    for (x,y) in ratings.items():
        if x in sim.keys():
            val = []
            newRatings [x]= val
            for a in y:

                val.append (a* (sim.get (x)))

    ret = averages(items, newRatings)

    return sorted (ret, key = lambda x: (-x[1], x[0]))
        

if __name__ == '__main__':

    name = 'Liam'
    items = ['Cat', 'Dog', 'Zebra']
    ratings = {'Liam': [10, 2, 5], 'Man-Lin': [2, 5, 0], 'Max': [7, 9, 1], 'Jose': [1, 2, 3]}
    size = 2
    print (recommendations(name, items, ratings, size))