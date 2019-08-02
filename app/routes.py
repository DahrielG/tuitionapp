from app import app
from flask import render_template, request
from app.models import model, formopener

import os
from app import app

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'tuitionapp' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:wONmnr26uAo5Nz6A@cluster0-tqevt.mongodb.net/tuitionapp?retryWrites=true&w=majority' 

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/calculatorOptions')
def calculatorOptions():
    return render_template('/CalculatorOptions.html')
    
@app.route('/calculator')
def calculator():
    return render_template('index.html')
    
@app.route('/calculatorA')
def calculatorA():
    determineForm = "A"
    return render_template('indexA.html')
    
@app.route('/calculatorB')
def calculatorB():
    determineForm = "B"
    return render_template('indexB.html')
    
@app.route('/calculatorC')
def calculatorC():
    determineForm = "C"
    return render_template('indexC.html')

@app.route('/calculatorD')
def calculatorD():
    determineForm = "D"
    return render_template('indexD.html') 

@app.route('/calculatorE')
def calculatorE():
    determineForm = "E"
    return render_template('indexE.html')

# @app.route('/add')
# def add():
#     # connect to the database
#     user = mongo.db.users

#     # insert new data
#     user.insert({'name':'Lisette', 'age':17})

#     # return a message to the user
#     return "User has been added!"
yearGap = 0
tuition = 0

@app.route('/LogIn')
def LogIn():
    return render_template('LogIn.html')

@app.route('/SignUp')
def SignUp():
    return render_template('SignUp.html')

@app.route('/sendUserData', methods = ['GET', 'POST'])
def sendUserData():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = userInfo["collegename"]
        tuition = userInfo["tuition"]
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)

@app.route('/sendUserDataA', methods = ['GET', 'POST'])
def sendUserDataA():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = "an average private college"
        tuition = 129640
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)
        
@app.route('/sendUserDataB', methods = ['GET', 'POST'])
def sendUserDataB():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = "an in state college"
        tuition = 95560
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)

@app.route('/sendUserDataC', methods = ['GET', 'POST'])
def sendUserDataC():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = "an average out of state college"
        tuition = 95560
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)
        
@app.route('/sendUserDataD', methods = ['GET', 'POST'])
def sendUserDataD():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = "an average 2-year college"
        tuition = 6880
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)
        
@app.route('/sendUserDataE', methods = ['GET', 'POST'])
def sendUserDataE():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        userInfo = dict(request.form)
        collegename = "just about any college without worry"
        tuition = 239548
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        yearGap = int(gradYear) - int(currentYear)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)
 
@app.route('/aidPage')
def aidPage():
    return render_template('aid.html')

@app.route('/aid', methods = ['GET', 'POST'])
def aid():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else:
        newContribution = dict(request.form)
        contribution = newContribution["contribution"]
        print("Contribution = " + contribution)
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        extraMoney = model.neededAid(tuition, weeksleft, contribution)
        return render_template("newCost.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, contribution = contribution, extraMoney = extraMoney)
        
@app.route('/advancedInfo', methods = ['GET', 'POST'])
def advancedInfo():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else:
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving, yearGap
        newData = dict(request.form)
        interestrate = newData["interestrate"]
        advancedAmount = newData['advancedAmount']
        totalSaved = model.interestCalc(yearGap, advancedAmount, interestrate)
        highTuition = model.sad(tuition, yearGap)
        elsewhere = int(highTuition) - int(totalSaved)
        if elsewhere < 0:
            elsewhere = 0
        return render_template("advancedInfo.html", tuition = tuition, totalSaved = totalSaved, yearGap = yearGap, saved = model.saved, highTuition = highTuition, elsewhere = elsewhere)
        
    