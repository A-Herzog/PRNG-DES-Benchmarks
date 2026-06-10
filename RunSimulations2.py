# Run simulations for different random number generator modes for M/M/1 and M/G/1 models and save the results to files.
# Models 2 (M/M/1, M/G/1 with log-normal service times)

import libs.tools as tools
import libs.setup as setup


def run_test(rng_mode: str) -> dict[str, float | int]:
    """Runs the simulation with the given random number generator mode and returns the results.
    Args:
        rng_mode (str): The random number generator mode to use in the simulation.
    Returns:
        dict[str, float | int]: A dictionary containing the mean waiting time, mean residence time, mean number of customers waiting and mean number of customers in the system.
    """

    statistics = tools.run(input_model, rng_mode)

    EW = statistics.find("QS:StatisticsWaitingTimesClients", tools.ns).find("QS:ClientType", tools.ns).attrib["Mean"]  # type: ignore
    EV = statistics.find("QS:StatisticsResidenceTimesClients", tools.ns).find("QS:ClientType", tools.ns).attrib["Mean"]  # type: ignore
    ENQ = statistics.find("QS:StatisticsClientsInSystemAllQueues", tools.ns).attrib["Mean"]  # type: ignore
    EN = statistics.find("QS:StatisticsClientsInSystem", tools.ns).attrib["Mean"]  # type: ignore
    time = int(statistics.find('QS:SimulationData', tools.ns).find("QS:StatisticsRunTime", tools.ns).text)  # type: ignore

    return {"EW": float(EW), "EV": float(EV), "ENQ": float(ENQ), "EN": float(EN), "time": time}


def save_results_to_file(prng_mode: str, results: dict[str, float | int], filename: str) -> None:
    """Saves the results of the simulation to a file.

    Args:
        prng_mode (str): The pseudo random number generator mode used in the simulation.
        results (dict[str, float | int]): A dictionary containing the results of the simulation.
        filename (str): The name of the file to save the results to.
    """

    with open(filename, 'a') as file:
        file.write(prng_mode + "\t" + str(results["EW"]) + "\t" + str(results["EV"]) + "\t" + str(results["ENQ"]) + "\t" + str(results["EN"]) + "\t" + str(results["time"]) + "\n")

# M/M/1 queueing model with ρ = 0.8
# input_model = 'models/model2MM1rho80.xml'
# output_file = "statistics/results2MM1rho80.txt"

# M/M/1 queueing model with ρ = 0.9
# input_model = 'models/model2MM1rho90.xml'
# output_file = "statistics/results2MM1rho90.txt"

# M/G/1 queueing model with log-normal service times and ρ = 0.9
# input_model = 'models/model2MG1LogRho90.xml'
# output_file = "statistics/results2MG1LogRho90.txt"

# M/G/1 queueing model with gamma service times and ρ = 0.9
# input_model = 'models/model2MG1GammaRho90.xml'
# output_file = "statistics/results2MG1GammaRho90.txt"

# M/M/1 queueing model with ρ = 0.95
# input_model = 'models/model2MM1rho95.xml'
# output_file = "statistics/results2MM1rho95.txt"

# M/G/1 queueing model with log-normal service times and ρ = 0.95
# input_model = 'models/model2MG1LogRho95.xml'
# output_file = "statistics/results2MG1LogRho95.txt"

# M/G/1 queueing model with gamma service times and ρ = 0.95
input_model = 'models/model2MG1GammaRho95.xml'
output_file = "statistics/results2MG1GammaRho95.txt"


for random_mode in setup.prng_modes:
    # Warm-up run
    print(random_mode, "warm-up")
    run_test(random_mode)
    # Actual test runs
    for i in range(100):
        print(random_mode, i)
        result = run_test(random_mode)
        save_results_to_file(random_mode, result, output_file)
