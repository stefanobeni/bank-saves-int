import matplotlib.pyplot as plt
import numpy as np


def OBSA(OBSA_deposit, FSA_deposit, mthly, out_rt, int_1, int_2):
    """
    OBSA stands for Online Bonus Savings Account. It is a savings account offered by HSBC where the interest rate is
    higher if you do not withdraw money from that account for that month (as per 03/02/24 it is 4.00% vs 2.00%).

    The function assumes no income. The function also assumes that money taken out of the OBSA will be deposited into
    the Flexible Savings Account (FSA), so interest accumulates in that way too.

    Example:
    If

    :param OBSA_deposit:
    :param FSA_deposit:
    :param mthly:
    :param out_rt:          --- This is the withdrawal rate. In other words it is the number of months you withdraw
                                money for in the event that you withdraw.
                                Example:
                                If out_rt == 2, it means that you will withdraw money once every 2 months. It also means
                                that when you do withdraw money, you withdraw the money that you need for 2 months.
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

    output = {"Final_OBSA_deposit": OBSA_deposit,
              "Final_FSA_deposit": FSA_deposit,
              "Accumulated OBSA interest": accmltd_interest_OBSA,
              "Accumulated FSA interest": accmltd_interest_FSA}
    return output


# To be included:
# Check that interest rate increase is lower than the monthly need.


# Change these parameters with the values that apply to yourself.
init_OBSA_deposit = 8400  # Initial deposit in the OBSA account.
init_FSA_deposit = 0      # Initial deposit in the FSA account
monthly = 700             # Amount needed to live for a month
withdrawal_rate = 3
int_OBSA = 0.04
int_FSA = 0.02

results = OBSA(init_OBSA_deposit, init_FSA_deposit, monthly, withdrawal_rate, int_OBSA, int_FSA)

print("The final amount in the OBSA account is: £" + "%.2f" % results["Final_OBSA_deposit"])
print("The final amount in the FSA account is: £" + "%.2f" % results["Final_FSA_deposit"])

print("The accumulated interest is: £"+"%.2f" % (results["Accumulated OBSA interest"]
                                                + results["Accumulated FSA interest"]))


def graph(OBSA_deposit, FSA_deposit, mthly, int_1, int_2):
    """
    The function returns a graph that shows the optimum withdrawal rate to maximise the accumulated interest
    given the amount of money in your savings and the amount you need to live every month.
    """
    array_x = np.arange(1, 11)
    array_y = np.zeros(10)

    for element in array_x:
        results = OBSA(OBSA_deposit, FSA_deposit, mthly, array_x[element-1], int_1, int_2)
        array_y[element-1] = results["Accumulated OBSA interest"] + results["Accumulated FSA interest"]

    plt.plot(array_x, array_y)

    plt.xlabel("Rate of Withdrawal (Months)")
    plt.ylabel("Total Accumulated Interest at the End of the Year (£)")

    plt.show()
    return None


graph(init_OBSA_deposit, init_FSA_deposit, monthly, int_OBSA, int_FSA)
