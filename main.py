import math
import argparse

parser = argparse.ArgumentParser(description="This program is a loan calculator.")

parser.add_argument("--type", "--first_parameter", type=str, choices=["annuity", "diff"],
                    help="Indicates the type of payment.")
parser.add_argument("--payment", "--second_parameter", type=int, help="Monthly payment amount.")
parser.add_argument("--principal", "--third_parameter", type=int, help="Principal amount of the loan.")
parser.add_argument("--periods", "--fourth_parameter", type=int, help="Number of months needed to repay the loan.")
parser.add_argument("--interest", "--fifth_parameter", type=float, help="Interest rate.")

args = parser.parse_args()

if args.type is None:
    print("Incorrect parameters")
elif args.type not in {"diff", "annuity"}:
    print("Incorrect parameters")
elif len(vars(args)) < 4:
    print("Incorrect parameters")
elif (args.payment or args.principal or args.periods or args.interest) <= 0:
    print("Incorrect parameters")

if args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    elif args.interest is None:
        print("Incorrect parameters")
    else:

        p = args.principal
        n = args.periods
        i = args.interest / (12 * 100)
        m = 0
        all_payments = []

        while True:
            m += 1
            sum1 = p / n
            sum2 = i * (p - (p * ((m - 1) / n)))
            diff_payment = sum1 + sum2
            print(f'Month {m}: payment is {math.ceil(diff_payment)}.')
            all_payments.append(math.ceil(diff_payment))
            if m == n:
                break

        overpayment = sum(all_payments) - p
        print(f'Overpayment = {math.ceil(overpayment)}')

if args.type == "annuity":

    if args.interest is None:
        print("Incorrect parameters")

    elif args.periods is None:
        p = args.principal
        a = args.payment
        i_base = args.interest
        i = i_base / (12 * 100)
        x = abs(a / (a - i * p))
        base = 1 + i
        num_mon = math.log(x, base)
        num_mon = math.ceil(num_mon)
        years, month = divmod(num_mon, 12)
        if years > 0 and month > 0:
            print(f'It will take {years} years and {month} months to repay this loan!.')
        elif years == 0 and month > 0:
            print(f'It will take {month} months to repay this loan!.')
        elif years > 0 and month == 0:
            print(f'It will take {years} years to repay this loan!.')
        elif years == 1 and month == 0:
            print(f'It will take {years} year to repay this loan!.')
        elif years == 0 and month == 1:
            print(f'It will take {month} month to repay this loan!.')
        overpayment = a * num_mon - p
        print(f'Overpayment = {math.ceil(overpayment)}')

    elif args.payment is None:
        p = args.principal
        n = args.periods
        i_base = args.interest
        i = i_base / (12 * 100)
        num = i * ((1 + i) ** n)
        den = (1 + i) ** n - 1
        a = p * (num / den)
        print(f'Your annuity payment = {math.ceil(a)}!')
        overpayment = math.ceil(a) * n - p
        print(f'Overpayment = {math.ceil(overpayment)}')

    elif args.principal is None:
        a = args.payment
        n = args.periods
        i_base = args.interest
        i = i_base / (12 * 100)
        num = abs((i * ((1 + i) ** n)))
        den = ((1 + i) ** n) - 1
        den2 = num / den
        p = a / den2
        p = int(p)
        print(f'Your loan principal = {p}!')
        overpayment = a * n - p
        print(f'Overpayment = {math.ceil(overpayment)}')
