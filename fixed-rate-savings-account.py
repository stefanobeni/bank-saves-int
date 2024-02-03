import numpy as np

def Fixed_Rate(tot_savs, init_f):
    mthly = init_f/12  # Amount of money you need to live for a month.

    fxd_rt = 0
    bonus = tot_savs - init_f
    flex = init_f

    int_1 = 0.00  # Interest rate of fixed rate savings account.
    int_2 = 0.00  # Bonus interest rate of bonus savings account.
    int_3 = 0.00  # Interest rate of bonus savings account (for withdrawal month) and flexible savings account

    bonus = bonus * (1 + int_2)
    for j in range(12):
        if mthly > 0:
            fxd_rt += mthly
            fxd_rt = fxd_rt * (1 + int_1/12)
    for i in range(12):
        if flex > 0:
            flex -= mthly
            flex = flex * (1 + int_3/12)
        elif flex < 0:
            print('ERROR: Negative Balance')
    # print('... from the fixed rate account: ' + str(fxd_rt))
    # print('... from the bonus account: ' + str(bonus))
    # print('... from the flexible account: ' + str(flex))
    return fxd_rt + bonus + flex


total_savings = 00000       # The total amount of savings you have accumulated.
initial_flexible = 00000    # The amount of savings you need to live for a year.
                            # (This is because you cannot access money in
                            # the fixed rate savings account for a whole year)

print('Monthly addition to Fixed Account: ' + '%.2f' % (initial_flexible/12))
print('Initial amount in the Bonus Account: ' + '%.2f' % (total_savings-initial_flexible))
print('Initial amount in the Flexible Account: ' + '%.2f' % initial_flexible + '\n')
print('With these parameters, the amount in your savings account after a year is '
      + '%.2f' % Fixed_Rate(total_savings, initial_flexible))
