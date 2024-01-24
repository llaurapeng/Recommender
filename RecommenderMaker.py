'''
@author: Laura Peng
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''

    val = RecommenderEngine.recommendations (name, items, ratings, numUsers)

    nums = ratings [name]
    first = []
    second = []
    for (x,y) in val:
        ind = items.index (x)
        if nums[ind] !=0:
            first.append ((x,y))
        else:
            second.append ((x,y))

    first = sorted (first[0:top], key = lambda x: -x[1])
    second = sorted(second[0:top], key=lambda x: -x[1])

    return (first,second)


    pass


if __name__ == '__main__':
    name = 'student1367'

    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street',
             'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar',
             'Black Swan']

    ratings = {'student1367': [0, 3, -5, 0, 0, 1, 5, 1, 3, 0],

               'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5],

               'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],

               'student1103': [-3, 3, -3, 5, 0, 0, 5, 3, 5, 5]}

    numUsers = 2

    top = 3

    print (makerecs (name, items, ratings, numUsers, top))
             



