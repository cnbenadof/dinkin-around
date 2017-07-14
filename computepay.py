#!/usr/bin/python
def computepay(h,r):
    if h>40:
        ot = h - 40
        otr = r * 1.5
        pay = ot * otr + 40 * r
        return pay
    else:
        pay = h * r
        return pay

hrs = input("Enter Hours:")
rt = input("Enter Rate:")
hours = float(hrs)
rate = float(rt)
p = computepay(hours, rate)
print(p)
