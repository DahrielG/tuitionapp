# weeks = (years * 52) + (months * 4)

#tuition calculation
def weeksLeft(gYear, gMonth, cYear, cMonth):
    years = int(gYear) - int(cYear)
    months = int(gMonth) - int(cMonth)
    weeks = (years * 52) + (months * 4)
    print(weeks)
    return weeks
    
# weeksLeft()

def equation(weeksAmount, tuition):
    weekly = int(tuition) / int(weeksAmount)
    weekly = round(weekly, 2)
    print(weekly)
    return weekly
# print("You need to save " + str(round(weekly, 2)) + " every week.")

def neededAid(tuition, weeksleft, contribution):
    totalContribution = int(weeksleft) * int(contribution)
    extraMoney = int(tuition) - int(totalContribution)
    return extraMoney
    
# determineForm = 0

def interestCalc(yearGap, advancedAmount, interestrate):
    global saved
    savings = 0
    yearlyAmount =  int(advancedAmount) * 52
    rate = float(interestrate) * 0.01
    thisValue = 1 + float(rate)
    for year in range(0, yearGap):
        savings = savings + yearlyAmount
        savings = savings * float(thisValue)
    saved = float(savings)
    saved = round(saved)
    return saved
    
def sad(tuition, yearGap):
    global htuition
    htuition = 0
    ituition = int(tuition)/4
    endPoint = yearGap + 3
    for year in (0, yearGap):
        if year == yearGap:
           htuition = htuition + ituition 
           ituition = ituition * (1.046)
           htuition = htuition + ituition 
           ituition = ituition * (1.046)
           htuition = htuition + ituition 
           ituition = ituition * (1.046)
           htuition = htuition + ituition 
           ituition = ituition * (1.046)
        else:
            ituition = ituition * (1.046)
    htuition = round(htuition)
    return htuition
        
        
        
# import college_datalist
# print (college_datalist)


