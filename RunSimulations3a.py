# Run simulations for different random number generator modes for models with branching (and no processing) and save the results to files.
# Models 3a (Branching - no processing)

import libs.tools as tools
import libs.setup as setup
import libs.stattools as stattools

import numpy as np


def run_test(rng_mode: str) -> dict[str, float | int]:
    """Runs the simulation with the given random number generator mode and returns the results.
    Args:
        rng_mode (str): The random number generator mode to use in the simulation.
    Returns:
        dict[str, float | int]: A dictionary containing the mean waiting time, mean residence time, mean number of customers waiting and mean number of customers in the system.
    """

    statistics = tools.run(input_model, rng_mode)

    el = statistics.find("QS:StatisticsInterArrivalTimesClients", tools.ns).find("QS:StationData", tools.ns)  # type: ignore
    values = np.array([int(value) for value in el.attrib['Distribution'].split(";")])  # type: ignore
    n = np.sum(values)
    density = values / n

    inter_arrival_station = statistics.find("QS:StatisticsInterArrivalTimesStations", tools.ns)
    a = b = 0
    for station in inter_arrival_station:  # type: ignore
        if station.attrib["Type"] == 'Exit "A" (id=4)':
            a = int(station.attrib["Count"])
        if station.attrib["Type"] == 'Exit "B" (id=5)':
            b = int(station.attrib["Count"])

    el = statistics.find('QS:SimulationData', tools.ns).find("QS:StatisticsRunTime", tools.ns)  # type: ignore
    time = int(el.text)  # type: ignore

    mean, std = stattools.get_mean_std(density)

    return {"n": n, "mean": mean, "std": std, "a": a, "b": b, "time": time}


def save_results_to_file(prng_mode: str, results: dict[str, float | int], filename: str) -> None:
    """Saves the results of the simulation to a file.

    Args:
        prng_mode (str): The pseudo random number generator mode used in the simulation.
        results (dict[str, float | int]): A dictionary containing the results of the simulation.
        filename (str): The name of the file to save the results to.
    """

    with open(filename, 'a') as file:
        file.write(prng_mode + "\t" + str(results["mean"]) + "\t" + str(results["a"]) + "\t" + str(results["b"]) + "\t" + str(results["n"]) + "\t" + str(results["time"]) + "\n")


# Branching - no processing
input_model = 'models/model3a.xml'
output_file = "statistics/results3a.txt"

for random_mode in setup.prng_modes:
    # Warm-up run
    print(random_mode, "warm-up")
    run_test(random_mode)

    # Actual test runs
    for i in range(100):
        print(random_mode, i)
        result = run_test(random_mode)
        save_results_to_file(random_mode, result, output_file)
