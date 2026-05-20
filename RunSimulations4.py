# Run simulations for different random number generator modes for a M/G/1 queueing model with varying rho and save the results to files.
# Not used in the report because the results do not show significant variation between different random number generator modes, but it was used to check if the results are consistent with the expected values for different rho values.
# The results are saved in "statistics/results2MG1-variatingRho.txt".

import libs.tools as tools
import libs.setup as setup


def run_test(rng_mode: str, ES: int | None = None) -> dict[str, float | int]:
    """Runs the simulation with the given random number generator mode and returns the results.
    Args:
        rng_mode (str): The random number generator mode to use in the simulation.
        ES (int): The expected service time for the log-normal distribution. Default is None, which means that the expected service time will not be changed in the model.
    Returns:
        dict[str, float | int]: A dictionary containing the mean waiting time, mean residence time, mean number of customers waiting and mean number of customers in the system.
    """

    model = tools.load_model(input_model, setup.arrival_count * 10, rng_mode)
    if ES is not None:
        model = model.replace(b"Lognormal distribution (90;45)", b"Lognormal distribution (" + str(ES).encode() + b";45)")  # type: ignore

    statistics = tools.run_model(model)

    EW = statistics.find("QS:StatisticsWaitingTimesClients", tools.ns).find("QS:ClientType", tools.ns).attrib["Mean"]  # type: ignore
    EV = statistics.find("QS:StatisticsResidenceTimesClients", tools.ns).find("QS:ClientType", tools.ns).attrib["Mean"]  # type: ignore
    ENQ = statistics.find("QS:StatisticsClientsInSystemAllQueues", tools.ns).attrib["Mean"]  # type: ignore
    EN = statistics.find("QS:StatisticsClientsInSystem", tools.ns).attrib["Mean"]  # type: ignore
    time = int(statistics.find('QS:SimulationData', tools.ns).find("QS:StatisticsRunTime", tools.ns).text)  # type: ignore

    return {"EW": float(EW), "EV": float(EV), "ENQ": float(ENQ), "EN": float(EN), "time": time}


def save_results_to_file(prng_mode: str, ES: int, results: dict[str, float | int], filename: str) -> None:
    """Saves the results of the simulation to a file.

    Args:
        prng_mode (str): The pseudo random number generator mode used in the simulation.
        ES (int): The expected service time for the log-normal distribution.
        results (dict[str, float | int]): A dictionary containing the results of the simulation.
        filename (str): The name of the file to save the results to.
    """

    with open(filename, 'a') as file:
        file.write(prng_mode + "\t" + str(ES) + "\t" + str(results["EW"]) + "\t" + str(results["EV"]) + "\t" + str(results["ENQ"]) + "\t" + str(results["EN"]) + "\t" + str(results["time"]) + "\n")


# M/G/1 queueing model with log-normal service times and ρ = 0.6..0.98
input_model = 'models/model2MG1rho90.xml'
output_file = "statistics/results2MG1-variatingRho.txt"

for ES in range(60, 99):
    for random_mode in setup.prng_modes:
        print(random_mode, "ES =", ES)
        result = run_test(random_mode, ES)
        save_results_to_file(random_mode, ES, result, output_file)
