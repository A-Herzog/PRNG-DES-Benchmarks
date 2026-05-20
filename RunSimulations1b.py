# Run simulations for different random number generator modes and save the results to files.
# Models 1 (Log-normal - histogram)

import libs.tools as tools

import numpy as np

# Setup for log-normal distribution
input_model = 'models/model1Log.xml'
output_file = "statistics/results1Log-Histogram.txt"

# Run simulations for both RNG modes
rng_mode = "Drand48"
statistics1 = tools.run(input_model, rng_mode)

rng_mode = "ThreadLocalRandom"
statistics2 = tools.run(input_model, rng_mode)

# Extract histogram data
el = statistics1.find("QS:StatisticsInterArrivalTimesClients", tools.ns).find("QS:StationData", tools.ns)  # type: ignore
values1 = np.array([int(value) for value in el.attrib['Distribution'].split(";")])  # type: ignore

el = statistics2.find("QS:StatisticsInterArrivalTimesClients", tools.ns).find("QS:StationData", tools.ns)  # type: ignore
values2 = np.array([int(value) for value in el.attrib['Distribution'].split(";")])  # type: ignore

# Save results to file
with open(output_file, 'a') as file:
    for i, value in enumerate(values1):
        file.write("Drand48" + "\t" + str(i) + "\t" + str(value) + "\n")
    for i, value in enumerate(values2):
        file.write("ThreadLocalRandom" + "\t" + str(i) + "\t" + str(value) + "\n")
