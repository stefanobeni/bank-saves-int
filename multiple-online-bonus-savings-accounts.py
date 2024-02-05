import matplotlib.pyplot as plt
import numpy as np


# This code is currently INCOMPLETE
# It is kept here for comparison
'''
def OBSA(OBSA_deposit, FSA_deposit, mthly, out_rt, int_1, int_2):
    """
    OBSA stands for Online Bonus Savings Account. It is a savings account offered by HSBC where the interest rate is
    higher if you do not withdraw money from that account for that month (currently 4.00% vs 2.00%).

    The function assumes no income. The function also assumes that money taken out of the OBSA will be deposited into
    the Flexible Savings Account (FSA), so interest accumulates in that way too.

    Example:
    If

    :param OBSA_deposit:
    :param FSA_deposit:
    :param mnthly_spend:
    :param out_rt:          --- This is the withdrawal rate. In other words it is the number of months you withdraw
                                money for in the event that you withdraw.
                                Example:
                                If out_rt == 2, it means that you will withdraw money once every 2 months. It also means
                                that when you do withdraw the money, you withdraw the money that you need for 2 months.
    :param int_1:
    :param int_2:

    :return: Final accumulated interest at the end of the year
    """

    # deposit = 3300
    # debit = 300
    # mthly = 300
    # int_1 = 0.04
    # int_2 = 0.02


    i = 1
    accmltd_interest_OBSA = 0
    accmltd_interest_FSA = 0

    for element in range(12):

        # These are the amounts in the deposits at the START of each month.
        print("Month = " + str(i))
        print("OBSA deposit = " + str(OBSA_deposit))
        print("FSA deposit  = " + str(FSA_deposit))


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
            Scenario 2: Not enough money in the FSA_deposit to last the month. Need to transfer money from OBSA account.
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

            print("WITHDRAW")
            FSA_deposit -= mthly
            i += 1

        elif FSA_deposit < mthly:
            """
            Scenario 3: Not enough money in the FSA account to last the month. Final transfer as money in OBSA account 
            is less then (out_rt * mnthly_need). All money in OBSA account is transferred to FSA account.
            """
            FSA_deposit = OBSA_deposit
            OBSA_deposit = 0

            # OBSA_mnthly_interest = OBSA_deposit * int_2 / 12
            FSA_mnthly_interest = (FSA_deposit - mthly) * int_2 / 12

            # OBSA_deposit += OBSA_mnthly_interest
            FSA_deposit += FSA_mnthly_interest

            # accmltd_interest_OBSA += OBSA_deposit * int_2 / 12
            accmltd_interest_FSA += (FSA_deposit - mthly) * int_2 / 12

            print("WITHDRAW TOTAL")
            FSA_deposit -= mthly
            i += 1

        else:
            print('ERROR: Negative deposit')
    results = {"Final_OBSA_deposit": OBSA_deposit,
               "Final_FSA_deposit": FSA_deposit,
               "Accumulated OBSA interest": accmltd_interest_OBSA,
               "Accumulated FSA interest": accmltd_interest_FSA}
    return results

# To be included:
# Make code work without having to have the monthly need be a factor of the total initial deposit.
# Check that interest rate increase is lower than the monthly need.


results = OBSA(3600, 0, 250, 3, 0.04, 0.02)

print("The final amount deposited in the OBSA account is: " + str(results["Final_OBSA_deposit"]))
print("The final amount deposited in the FSA account is: " + str(results["Final_FSA_deposit"]))

print("The accumulated interest is: "+str(results["Accumulated OBSA interest"] + results["Accumulated FSA interest"]))
# 63.7
'''


def multiple_OBSA(out_rt):
    i = 1
    accmltd_interest = 0
    accmltd_interest_extra = 0
    deposit = 3300
    debit = 300
    mthly = 300
    int_1 = 0.04
    int_2 = 0.02

    # rng = init_deposit / (mthly * out_rt)

    for element in range(12):

        print("Month = " + str(i))
        print("Deposit = " + str(deposit))
        print("Debit = " + str(debit))

        # print(mthly*out_rt)

        if debit > 0:
            accmltd_interest += deposit * int_1 / 12
            accmltd_interest_extra += (debit - mthly) * int_2 / 12

            debit -= mthly
            i += 1
        elif debit == 0 and deposit > (mthly*out_rt):
            debit = (mthly * out_rt)
            deposit -= (mthly * out_rt)

            accmltd_interest += deposit * int_2 / 12
            accmltd_interest_extra += (debit - mthly) * int_2 / 12

            print("TAKE OUT")
            debit -= mthly
            i += 1
        elif debit == 0:
            debit = deposit
            deposit = 0
            accmltd_interest += deposit * int_2 / 12
            accmltd_interest_extra += (debit - mthly) * int_2 / 12

            print("TAKE OUT")
            debit -= mthly
            i += 1
        else:
            print('ERROR: Negative debit')
    return accmltd_interest + accmltd_interest_extra


def graph():
    """
    The function returns a graph that shows the optimum withdrawal rate to maximise the accumulated interest.
    """
    array_x = np.arange(1, 11)
    array_y = np.zeros(10)
    # array_y_extra = np.zeros(10)

    for element in array_x:
        results = OBSA(3409.91, 0, 250, array_x[element-1], 0.04, 0.02)
        array_y[element-1] = results["Accumulated OBSA interest"] + results["Accumulated FSA interest"]
        # array_y_extra[element-1] = OBSA_extra(array_x[element-1])

    # plt.plot(array_x, array_y_extra)
    plt.plot(array_x, array_y)
    # plt.legend(['2 Savings Accounts', '1 Savings Account'])

    plt.xlabel("Rate of Withdrawal")
    plt.ylabel("Total Accumulated Interest at the End of the Year")

    plt.show()
    return None


graph()
