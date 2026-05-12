# Performance Analysis for cProfile1.txt

Link to file [here](../cProfile/cProfile1.txt)

How to identify bottlenecks

1. High cumulative time
  - Above is the function eating the most total time
2. High ncalls (number of calls) with decent time
  - A function called thousands of times adds up fast even if each call is cheap
3. The ratio that matters
  - If tottime (time in the function) is high -> the function is the problem
  - If cumtime is high but tottime is low -> the problem is inside something it calls

## Profile 1 Analysis

Highest ncalls:

      942    0.001    0.000    0.001    0.000 {method 'isupper' of 'str' objects}

Highest cumtime:

      2/1    0.000    0.000    1.056    1.056 {built-in method builtins.exec}
        1    0.000    0.000    1.056    1.056 main.py:1(<module>)

Highest tottime:

      1    1.028    1.028    1.028    1.028 {method 'connect' of '_socket.socket' objects

  - Ratio is fine (1:1)

## Summary

Nothing stands out as a bottleneck

Git commit for first analysis

Portscanner need to actually be widened enough to optimize
