def sum_range(start, end):
    if start < end:
        print(sum(range(start, end+1)))
    else:
        print(sum(range(end+1, start)))


sum_range(1, 5)
