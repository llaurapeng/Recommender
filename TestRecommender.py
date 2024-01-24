'''
@author: Laura Peng
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    avg2= [('DivinityCafe', 4.0), ('TheCommons', 3.0),

 ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),

 ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0),

 ('TheSkillet', 0.0), ('PandaExpress', -0.2),

 ('McDonalds', -0.3333333333333333)]

    print("average",avg)
    ret = "averages works"

    count = 0
    for (x,y) in avg:
        comp = avg2[count][1]
        if y-comp<0.001:
            ret = "averages works"
        else:
            ret = "averages fails"
            break
        count+=1

    print (ret)

    sim2 = [('Wei', 1), ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6),

 ('J J', -14), ('Harry', -24), ('Nana Grace', -29)]

    rec2 = [('Tandoor', 149.5), ('TheCommons', 128.0),

 ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5),

 ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),

 ('IlForno', 33.0), ('McDonalds', -69.5),

 ('PandaExpress', -165.0)]
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)


        print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        print("top",r3)

    print ("______")
    print (slist)

    print (sim2)
    ret = "similarities works"
    count = 0
    for (x, y) in slist:
        comp = sim2[count][1]
        if y - comp < 0.001:
            ret = "similarities works"
        else:
            ret = "similarities fails"
            break
        count += 1

    print(ret)
    print ("____________")
    print (r3)
    print (rec2)
    ret = "rec works"
    count = 0
    for (x, y) in r3:
        comp = rec2[count][1]
        if y - comp < 0.001:
            ret = "rec works"
        else:
            ret = "rec fails"
            break
        count += 1

    print(ret)
        
if __name__ == '__main__':
    driver()
