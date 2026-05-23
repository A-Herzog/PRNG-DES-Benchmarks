from math import sqrt, exp, log
import numpy as np
import scipy.stats as stats


def get_mean_std(density: np.ndarray) -> tuple[float, float]:
    """Calculates mean and standard deviation from the normalized density of the simulated values.

    Args:
        density (np.ndarray): The normalized density array of the simulated values.

    Returns:
        tuple[float, float]: The mean and standard deviation of the simulated values.
    """
    count = len(density)
    value_sum = np.sum(density)
    fraction = density / value_sum

    fraction_x = sum(fraction * range(count))
    fraction_x2 = sum(fraction * np.array(range(count))**2)
    return fraction_x, sqrt(fraction_x2 - fraction_x**2)


def generate_exp_histogram(mean: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on an exponential distribution with the given mean.

    Args:
        mean (float): The mean of the exponential distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the exponential distribution for the given mean.
    """
    scale = mean
    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.expon.cdf(x, scale=scale)
    upper = stats.expon.cdf(y, scale=scale)

    return upper - lower


def generate_log_normal_histogram(mean: float, std: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on a log-normal distribution with the given mean and standard deviation.

    Args:
        mean (float): The mean of the log-normal distribution.
        std (float): The standard deviation of the log-normal distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the log-normal distribution for the given mean and standard deviation.
    """
    sigma = sqrt(log(std**2 / mean**2 + 1))
    mu = log(mean) - sigma**2 / 2
    s = sigma
    scale = exp(mu)

    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.lognorm.cdf(x, s, scale=scale)
    upper = stats.lognorm.cdf(y, s, scale=scale)

    return upper - lower


def generate_gamma_histogram(mean: float, std: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on a gamma distribution with the given mean and standard deviation.

    Args:
        mean (float): The mean of the gamma distribution.
        std (float): The standard deviation of the gamma distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the gamma distribution for the given mean and standard deviation.
    """
    beta = std**2 / mean
    alpha = mean / beta

    a = alpha
    scale = beta

    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.gamma.cdf(x, a, scale=scale)
    upper = stats.gamma.cdf(y, a, scale=scale)

    return upper - lower


def generate_triangular_histogram(a: float, b: float, c: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on a triangular distribution with the min, mode and max.

    Args:
        a (float): The minimum value of the support of the triangular distribution.
        b (float): The mode of the triangular distribution.
        c (float): The minimum value of the support of the triangular distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the triangular distribution for the given parameters.
    """
    c_param = (b - a) / (c - a)
    loc = a
    scale = c - a

    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.triang.cdf(x, c_param, loc=loc, scale=scale)
    upper = stats.triang.cdf(y, c_param, loc=loc, scale=scale)

    return upper - lower


def generate_poisson_histogram(mean: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on a Poisson distribution with the given mean.

    Args:
        mean (float): The mean of the Poisson distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the Poisson distribution for the given mean.
    """
    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.poisson.cdf(x, mean)
    upper = stats.poisson.cdf(y, mean)

    return upper - lower

def generate_geometric_histogram(mean: float, count: int) -> np.ndarray:
    """Calculated histogram values for comparison with the simulated values based on a geometric distribution with the given mean.

    Args:
        mean (float): The mean of the geometric distribution.
        count (int): The number of histogram bins to be calculated.

    Returns:
        np.ndarray: The histogram values of the geometric distribution for the given mean.
    """
    p = 1 / (mean + 1)

    arr = np.array(range(count))
    x = arr - 0.5
    y = arr + 0.5

    lower = stats.geom.cdf(x+1, p)  # The geometric distribution in scipy is defined as the number of trials until the first success, so we need to add 1 to x and y to get the correct CDF values for the histogram bins.
    upper = stats.geom.cdf(y+1, p)

    return upper - lower
