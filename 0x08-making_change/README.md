# Make Change
Given a pile of coins of different values,
our script determines the fewest number of coins needed to meet a given amount total.

* Prototype: def makeChange(coins, total)
* Return: fewest number of coins needed to meet total
    * If total is 0 or less, return 0
    * If total cannot be met by any number of coins we have, return -1
* coins is a list of the values of the coins in our possession
* The value of a coin is an integer greater than 0
* We assume we have an infinite number of each denomination of coin in the list

```bash
Mado-Term$$~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

Mado-Term$$~/0x08-making_change$
Mado-Term$$~/0x08-making_change$ ./0-main.py
7
-1
Mado-Term$$~/0x08-making_change$
```
