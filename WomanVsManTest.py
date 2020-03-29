import random



class ThrowStatistics:
    def __init__(self):
        self.womanF=0
        self.womanB=0
        self.womanTemp=0

        self.manF=0
        self.manB=0
        self.manTemp=0

        self.situationFF=0  ## Both front
        self.situationFB=0  ## Woman front and man back
        self.situationBF=0  ## Woman back and man front
        self.situationBB=0  ## Both back

        self.womanMoney=0
        self.manMoney=0

def do_throw(ts):
    ## 1 is front and 2 is back
    for i in range(1000): 
        ## Get woman temp
        ts.womanTemp = random.randint(1,2)
        if( ts.womanTemp is 1):
            ts.womanF = ts.womanF + 1
        else:
            ts.womanB = ts.womanB + 1
        
        ## Get man temp
        ts.manTemp = random.randint(1,2)
        if ts.manTemp is 1:
            ts.manF = ts.manF + 1
        else:
            ts.manB = ts.manB + 1

        ## Record situation
        if ( ts.womanTemp is 1 and ts.manTemp is 1):
            ts.situationFF = ts.situationFF + 1
        elif (  ts.womanTemp is 1 and ts.manTemp is 2 ):
            ts.situationFB = ts.situationFB + 1
        elif (  ts.womanTemp is 2 and ts.manTemp is 1 ):
            ts.situationBF = ts.situationBF + 1
        elif (  ts.womanTemp is 2 and ts.manTemp is 2 ):
            ts.situationBB = ts.situationBB + 1
    

def print_count(role, countF, countB):
    print(role + " throws front: " + str(countF) + ", and throws back: " + str(countB))

def print_result(ts):
    print_count("Woman", ts.womanF,ts.womanB)
    print_count("Man", ts.manF, ts.manB)

    print("FF count is: " + str(ts.situationFF))
    print("FB count is: " + str(ts.situationFB))
    print("BF count is: " + str(ts.situationBF))
    print("BB count is: " + str(ts.situationBB))

    ts.womanMoney = -3 * ts.situationFF + 2 * ts.situationFB + 2 * ts.situationBF - 1 * ts.situationBB
    ts.manMoney = - ts.womanMoney

    print("Woman get: " + str(ts.womanMoney))
    print("Man get: " + str(ts.manMoney))

def man():
    womanWinCount=0
    manWinCount=0
    dogfall=0

    womanWinMoney=0
    manWinMoney=0

    raceCont = 1000

    for i in range(raceCont):
        print("This is race " + str(i))
        ts = ThrowStatistics()
        do_throw(ts)
        print_result(ts)
        if ts.womanMoney < 0 :
            manWinCount = manWinCount + 1
        elif ts.womanMoney > 0 :
            womanWinCount = womanWinCount + 1
        else :
            dogfall = dogfall + 1
        womanWinMoney = womanWinMoney + ts.womanMoney
        manWinMoney = manWinMoney + ts.manMoney

    print("Played " + str(raceCont) + " races, woman win " + str(womanWinCount) + " times and man win " + str(manWinCount) + " times")
    print("Woman win money " + str (womanWinMoney) + ", and man win money " + str(manWinMoney))
man()