import numpy as np


def Fixed_Rate(tot_savs, year, out_rt):
    '''
    It is more complicated than this because you need to consider the interest gained on the interest generated every
    month by the Fixed Rates Savings Account.
    '''
    mthly = year/12  # Amount of money you need to live for a month.

    FRSA_deposit = tot_savs - year
    OBSA_deposit = year
    FSA_deposit = 0

    int_1 = 0.04  # Interest rate of bonus savings account (for withdrawal month) and flexible savings account.
    int_2 = 0.02  # Bonus interest rate of bonus savings account.
    int_3 = 0.05  # Interest rate of fixed rate savings account.

    i = 1
    accmltd_interest_FRSA = FRSA_deposit * int_3
    accmltd_interest_OBSA = 0
    accmltd_interest_FSA = 0


    for element in range(12):

        # These are the amounts in the deposits at the START of each month.
        # print("Month = " + str(i))
        # print("OBSA deposit = " + str(OBSA_deposit))
        # print("FSA deposit  = " + str(FSA_deposit))

        if FSA_deposit >= mthly:
            """
            Scenario 1: Enough money in the FSA_deposit to last the month. OBSA account will have higher interest rate.
            """
            OBSA_mnthly_interest = OBSA_deposit * int_1 / 12
            FSA_mnthly_interest = (FSA_deposit - mthly) * int_2 / 12

            OBSA_deposit += OBSA_mnthly_interest
            FSA_deposit += FSA_mnthly_interest

            accmltd_interest_OBSA += OBSA_mnthly_interest
            accmltd_interest_FSA += FSA_mnthly_interest

            FSA_deposit -= mthly
            i += 1

        elif FSA_deposit < mthly and OBSA_deposit > (mthly*out_rt):
            """
            Scenario 2: Not enough money in the FSA account to last the month. Need to transfer money from OBSA account.
                        OBSA account will have lower interest rate.
            """
            FSA_deposit  += (mthly * out_rt)
            OBSA_deposit -= (mthly * out_rt)

            OBSA_mnthly_interest = OBSA_deposit * int_2 / 12
            FSA_mnthly_interest  = (FSA_deposit - mthly) * int_2 / 12

            OBSA_deposit += OBSA_mnthly_interest
            FSA_deposit  += FSA_mnthly_interest

            accmltd_interest_OBSA += OBSA_deposit * int_2 / 12
            accmltd_interest_FSA  += (FSA_deposit - mthly) * int_2 / 12

            # print("WITHDRAW")
            FSA_deposit -= mthly
            i += 1

        elif FSA_deposit < mthly:
            """
            Scenario 3: Not enough money in the FSA account to last the month. Final transfer as money in OBSA account 
                        is less then (mnthly * out_rt). All money in OBSA account is transferred to FSA account.
            """
            FSA_deposit = OBSA_deposit
            OBSA_deposit = 0

            FSA_mnthly_interest = (FSA_deposit - mthly) * int_2 / 12
            FSA_deposit += FSA_mnthly_interest
            accmltd_interest_FSA += (FSA_deposit - mthly) * int_2 / 12

            # print("WITHDRAW TOTAL")
            FSA_deposit -= mthly
            i += 1

        else:
            print('ERROR: Negative deposit')

    output = {"Final FRSA deposit": FRSA_deposit,
              "Final OBSA deposit": OBSA_deposit,
              "Final FSA deposit": FSA_deposit,
              "Accumulated FRSA interest": accmltd_interest_FRSA,
              "Accumulated OBSA interest": accmltd_interest_OBSA,
              "Accumulated FSA interest": accmltd_interest_FSA}
    return output


total_savings = 12000     # The total amount of savings you have accumulated.
year_need = 3000          # The amount of savings you need to live for a year.
                          # (This is because you cannot access money in
                          # the fixed rate savings account for a whole year)
OBSA_withdrawal_rate = 3  # This is the withdrawal rate. In other words it is the number of months you withdraw
                          # money for in the event that you withdraw.

results = Fixed_Rate(total_savings, year_need, OBSA_withdrawal_rate)

print('With these parameters, the amount in your savings account after a year is '
      + '%.2f' % (results["Final FRSA deposit"]+results["Final OBSA deposit"]+results["Final FSA deposit"]))
