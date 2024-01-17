investment = 200000
income = 2000
loss = 1610

def roi(investment, income, loss):
    net_profit = income * 12 - loss
    roi = (net_profit/investment)*100
    print(roi)

roi(investment, income, loss)