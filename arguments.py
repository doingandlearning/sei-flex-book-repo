# what are *args and **kwargs

def my_sum(first=None, second=None, *args, **kwargs):
    return second


print(my_sum(99, 100, 200, 200, name="Kevin"))
