def get_sum_metrics(predictions, metrics= None):

    if not metrics:
        metrics = []
    for i in range(3):
        metrics.append(gen_add_i(i))
        # print(f'i = {i}')

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)
        # print(metric(predictions),predictions)
    # print('iterations ends')

    return sum_metrics
def gen_add_i(i):
    return lambda x : x+i


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    x = gen_add_i(1)
    print(f'x = {x(2)}')

if __name__ == "__main__":
    main()
