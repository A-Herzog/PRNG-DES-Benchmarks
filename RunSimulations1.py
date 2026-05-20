# Run simulations for different random number generator modes and save the results to files.
# Models 1 (Exponential, Log-normal, Gamma, Triangular)

from math import sqrt
import libs.tools as tools
import libs.setup as setup
import libs.stattools as stattools

import numpy as np


def run_test(rng_mode: str, mean: float, std: float, distribution_histogram: np.ndarray) -> dict[str, float | int]:
    """Runs the test by loading the model, communicating with the Warteschlangensimulator via socket connection, and calculating the mean, standard deviation, and delta^2 of the simulated values.

    Args:
        rng_mode (str): The random number generator mode to use in the simulation.
        mean (float): The actual mean of the log-normal distribution.
        std (float): The actual standard deviation of the log-normal distribution.
        distribution_histogram (np.ndarray): The histogram values of the distribution.

    Returns:
        dict[str, float | int]: A dictionary containing the results of the simulation.
    """

    statistics = tools.run(input_model, rng_mode)

    el = statistics.find("QS:StatisticsInterArrivalTimesClients", tools.ns).find("QS:StationData", tools.ns)  # type: ignore
    values = np.array([int(value) for value in el.attrib['Distribution'].split(";")])  # type: ignore
    n = np.sum(values)
    density = values / n

    el = statistics.find('QS:SimulationData', tools.ns).find("QS:StatisticsRunTime", tools.ns)  # type: ignore
    time = int(el.text)  # type: ignore

    mean, std = stattools.get_mean_std(density)
    delta2 = sum((density - distribution_histogram)**2)

    return {"n": n, "mean": mean, "std": std, "delta2": delta2, "time": time}


def save_results_to_file(prng_mode: str, results: dict[str, float | int], filename: str) -> None:
    """Saves the results of the simulation to a file.

    Args:
        prng_mode (str): The pseudo random number generator mode used in the simulation.
        results (dict[str, float | int]): A dictionary containing the results of the simulation.
        filename (str): The name of the file to save the results to.
    """
    with open(filename, 'a') as file:
        file.write(prng_mode + "\t" + str(results["n"]) + "\t" + str(results["mean"]) + "\t" + str(results["std"]) + "\t" + str(results["delta2"]) + "\t" + str(results["time"]) + "\n")


# Actual mean and standard deviation of the log-normal distribution used in the model
mean = 200
std = 50

# Setup for exponential distribution
# input_model = 'models/model1Exp.xml'
# output_file = "statistics/results1Exp.txt"
# distribution_histogram = stattools.generate_exp_histogram(mean, 3600)

# Setup for log-normal distribution
# input_model= 'models/model1Log.xml'
# output_file = "statistics/results1Log.txt"
# distribution_histogram = stattools.generate_log_normal_histogram(mean, std, 3600)

# Setup for gamma distribution
# input_model = 'models/model1Gamma.xml'
# output_file = "statistics/results1Gamma.txt"
# distribution_histogram = stattools.generate_gamma_histogram(mean, std, 3600)

# Setup for triangular distribution
input_model = 'models/model1Triangular.xml'
output_file = "statistics/results1Triangular.txt"
distribution_histogram = stattools.generate_triangular_histogram(200 - 50 * sqrt(6), 200, 200 + 50 * sqrt(6), 3600)


for random_mode in setup.prng_modes:
    # Warm-up run
    print(random_mode, "warm-up")
    run_test(random_mode, mean, std, distribution_histogram)
    # Actual test runs
    for i in range(100):
        print(random_mode, i)
        result = run_test(random_mode, mean, std, distribution_histogram)
        save_results_to_file(random_mode, result, output_file)
