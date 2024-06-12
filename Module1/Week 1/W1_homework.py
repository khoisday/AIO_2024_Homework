from math import exp, sqrt
import random


def calc_f1_score(tp, fp, fn):
    assert isinstance(tp, int), 'tp must be int'
    assert isinstance(fp, int), 'fp must be int'
    assert isinstance(fn, int), 'fn must be int'

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score


# Given
def is_number(n):
    try:
        float(n)  # Type - casting the string to
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def calc_sigmoid(x):
    return 1 / (1 + exp(-x))


def calc_relu(x):
    return max(0, x)


def calc_elu(x, alpha = 1):
    return x if x > 0 else alpha * (exp(x) - 1)


def exercise2(x, act_name):
    assert is_number(x), 'x must be a number'
    assert act_name in ['sigmoid', 'relu', 'elu'], f"{act_name} is not supported"

    if act_name == "sigmoid":
        print(f"Sigmoid({x}) = {calc_sigmoid(x)}")
        return calc_sigmoid(x)
    elif act_name == "relu":
        print(f"ReLU({x}) = {calc_relu(x)}")
        return calc_relu(x)
    else:
        print(f"ELU({x}) = {calc_elu(x)}")
        return calc_elu(x)


def mae(predictions, targets):
    return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)


def mse(predictions, targets):
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)


def rmse(predictions, targets):
    return sqrt(mse(predictions, targets))


def exercise3(num_samples, loss_name):
    assert is_number(num_samples), 'Number of samples must be an integer number.'
    loss_functions = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }

    assert loss_name.upper() in loss_functions, f'{loss_name} is not a supported loss function.'
    loss_function = loss_functions[loss_name]

    for i in range(num_samples):
        prediction = random.uniform(0, 10)
        target = random.uniform(0, 10)
        loss = loss_function([prediction], [target])
        print(f'Sample-{i}, Predict: {prediction}, Target: {target}, {loss_name}: {loss}')


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

greater_than_0_error_log = "n must be greater than 0"

def approx_sin(x, n):
    if n <= 0:
        raise ValueError(greater_than_0_error_log)
    return sum(((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))


def approx_cos(x, n):
    if n <= 0:
        raise ValueError(greater_than_0_error_log)
    return sum(((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) for i in range(n))


def approx_sinh(x, n):
    if n <= 0:
        raise ValueError(greater_than_0_error_log)
    return sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))


def approx_cosh(x, n):
    if n <= 0:
        raise ValueError(greater_than_0_error_log)
    return sum((x ** (2 * i)) / factorial(2 * i) for i in range(n))


def exercise5(y, y_hat, n, p):
    if n <= 0:
        raise ValueError(greater_than_0_error_log)
    return abs((y ** (1 / n) - y_hat ** (1 / n)) ** p)


if __name__ == "__main__":
    print(round(approx_cosh(x=3.14, n=10), 2))