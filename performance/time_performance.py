import time

def time_function(callable, args, n=1):
    print("--- time performance for {} on {} runs ---".format(callable.__name__, n))
    average = 0
    longest = 0

    for _ in range(n):
        start_time = time.time()
        callable(*args)
        exec_time = time.time() - start_time
        average += exec_time
        longest = max(longest, exec_time)

    print("  - average : {:.6f} ms".format(((average/n) * 1000)))
    print("  - longest : {:.6f} ms".format(longest * 1000))