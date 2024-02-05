

def LISA(yearly_deposit, age, interest_rt_perc):
    """
    LISA stands for Lifetime ISA. Code requires the amount you can deposit into your LISA account every year (Note that
    LISA accounts have a limit to the amount you can deposit every year, it is £4000 py in the UK). In the UK the
    government gives a government contribution that is equal to 1/4 of the amount you deposited that year. This
    contribution is included in this code.

    NOTE:
    It is important to note that what sets ISA account is that they are not taxable.
    The catch is that you can only have one ISA account at a time.

    For a comfortable retirement, your total yearly pension should be two-thirds of your pre-retirement income.

    :param yearly_deposit:   --- Amount deposited yearly into LISA account.
    :param age:              --- Your current age. This is used to calculate the number of years until you are 60 and
                                 can withdraw from the LISA account without penalties.
    :param interest_rt_perc: --- The yearly interest rate of your LISA account.
    :return new_deposit:     --- The amount of money you will have in your LISA account by the time you are 60.
    """

    # Compute the number of years until you are 60 and can take money out of the LISA account without penalties.
    years260 = 60 - age

    # Compute the interest rate as a fraction of one.
    interest_rt = interest_rt_perc/100

    # Calculate new_deposit: the amount you will have in your LISA account at 60.
    old_deposit = 0
    for element in range(years260):
        temp_deposit = (old_deposit + yearly_deposit + yearly_deposit/4)*(1 + interest_rt)
        old_deposit = temp_deposit
    new_deposit = old_deposit
    return new_deposit


# Change these parameters with the values that apply to yourself.
year_deposit = 4000     # The amount you are able to deposit every year into your LISA account.
years = 35              # Your age.
int_rate = 3.25         # The yearly interest rate of the account you are interested in.


print("At 60, your LISA account will hold: £" + '%.2f' % LISA(year_deposit, years, int_rate))


# To be included:
# Function to calculate the difference between LISA savings and the savings from a normal savings account.
