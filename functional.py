global i
i = 0


def smart_function():
    global i
    i += 1
    return i


for real_call_count in range(1, 5):
    assert smart_function() == real_call_count
