# Calculate Savings with Interest Rates
The code in this repository looks at different strategies that could be used to maximise the earnings from savings accounts. (Last update: 05/02/2024)

The code looks at three different types of savings accounts, all of which can be obtained from HSBC:
1. **Fixed Rate Savings Account**: Interest rate of 5%, but no withdrawals are allowed for the duration of the account (either 1 or 2 years).
2. **Online Bonus Savings Account**: Interest rate of 4% if no withdrawal that month and interest rate of 2% if there was a withdrawal that month.
3. **Flexible Savings Account**: Interest rate of 2%. Can withdraw at any point.

The code also includes a `graph()` function. This function illustrates the optimum times to withdraw from the **Online Bonus Savings Account**. The output is a graph like the one below.

![withdrawal rate graph](https://github.com/stefanobeni/bank-saves-int/blob/main/withdrawal-rate-graph.png?raw=true)
*Figure 1*: Graph showing the interest accumulated over a year depending on the withdrawal rate.

**Example**: With the example parameters in the 'online-bonus-savings-account' code, the optimum number of months to withdraw money from the OBSA account would be 4 months (although the accumulated interest doesn't change much in this case for 3 and 5 months).
