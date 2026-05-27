# Run simulations for different random number generator modes and save the results to files.
# Models 1 (Exponential, Log-normal, Gamma, Triangular - Autocorrelation)

from math import sqrt
import libs.tools as tools
import libs.setup as setup
import libs.stattools as stattools

import numpy as np


def run_test(rng_mode: str) -> dict[str, float | int | list[float]]:
    """Runs the test by loading the model, communicating with the Warteschlangensimulator via socket connection, and calculating the mean, standard deviation, and delta^2 of the simulated values.

    Args:
        rng_mode (str): The random number generator mode to use in the simulation.

    Returns:
        dict[str, float | int]: A dictionary containing the results of the simulation.
    """

    statistics = tools.run(input_model, rng_mode)

    el = statistics.find("QS:StatisticsWaitingTimesAllClients", tools.ns)
    n = int(el.attrib["Count"])  # type: ignore
    mean = float(el.attrib["Mean"])  # type: ignore
    std = float(el.attrib["StandardDeviation"])  # type: ignore
    autocorrelation = [float(x) for x in el.attrib["Autocorrelation"].split(";")]  # type: ignore
    autocorrelation_sum = sum([abs(x) for x in autocorrelation[1:]])

    el = statistics.find('QS:SimulationData', tools.ns).find("QS:StatisticsRunTime", tools.ns)  # type: ignore
    time = int(el.text)  # type: ignore

    return {"n": n, "mean": mean, "std": std, "autocorrelation": autocorrelation, "autocorrelation_sum": autocorrelation_sum, "time": time}


def save_results_to_file(prng_mode: str, results: dict[str, float | int | list[float]], filename: str) -> None:
    """Saves the results of the simulation to a file.

    Args:
        prng_mode (str): The pseudo random number generator mode used in the simulation.
        results (dict[str, float | int | list[float]]): A dictionary containing the results of the simulation.
        filename (str): The name of the file to save the results to.
    """
    with open(filename, 'a') as file:
        file.write(prng_mode + "\t" + str(results["n"]) + "\t" + str(results["mean"]) + "\t" + str(results["std"]) + "\t" + str(results["autocorrelation"][1])+ "\t" + str(results["autocorrelation"][2])+ "\t" + str(results["autocorrelation"][3]) + "\t" + str(results["autocorrelation_sum"]) + "\t" + str(results["time"]) + "\n")  # type: ignore


# Setup for exponential distribution
# input_model = 'models/model1Exp-Autocorrelation.xml'
# output_file = "statistics/results1ExpAutocorrelation.txt"

# Setup for log-normal distribution
# input_model= 'models/model1Log-Autocorrelation.xml'
# output_file = "statistics/results1LogAutocorrelation.txt"

# Setup for gamma distribution
# input_model = 'models/model1Gamma-Autocorrelation.xml'
# output_file = "statistics/results1GammaAutocorrelation.txt"

# Setup for triangular distribution
# input_model = 'models/model1Triangular-Autocorrelation.xml'
# output_file = "statistics/results1TriangularAutocorrelation.txt"

# Setup for Poisson distribution
# input_model = 'models/model1Poisson-Autocorrelation.xml'
# output_file = "statistics/results1PoissonAutocorrelation.txt"

# Setup for geometric distribution
input_model = 'models/model1Geometric-Autocorrelation.xml'
output_file = "statistics/results1GeometricAutocorrelation.txt"


for random_mode in setup.prng_modes:
    # Warm-up run
    print(random_mode, "warm-up")
    run_test(random_mode)
    # Actual test runs
    for i in range(100):
        print(random_mode, i)
        result = run_test(random_mode)
        save_results_to_file(random_mode, result, output_file)
