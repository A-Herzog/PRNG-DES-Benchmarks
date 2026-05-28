# Benchmarking Pseudorandom Number Generators in Discrete-Event Simulation: Quality, Speed, and Practical Implications - Supplementary Material

This repository contains supplementary material for the "**Benchmarking Pseudorandom Number Generators in Discrete-Event Simulation: Quality, Speed, and Practical Implications**" report. The scripts in this repository were used to generate the tables and charts in the paper.

## Pseudorandom number generators under consideration

The following 30 pseudorandom number generators are available in Warteschlangengenerator and are analyzed in the report:

* ThreadLocalRandom
* Random
* SecureRandom
* Well512a
* Well1024a
* Well19937a
* Well19937c
* Well44497a
* Well44497b
* MersenneTwister
* ISAAC
* XoRoShiRo128++
* XoRoShiRo128**
* XoRoShiRo64**
* XoRoShiRo256++
* XoRoShiRo1024++
* XoRoShiRo1024*
* XoRoShiRo1024**
* L32X64Mix
* L64X128Mix
* L64X128
* L64X256Mix
* L64X1024Mix
* L128X128Mix
* L128X256Mix
* L128X1024Mix
* PcgRxsMXs64
* Philox4x64
* Drand48
* Drand48Mix

For more details see [Warteschlangensimulator wiki page about pseudorandom numbers generators](https://github.com/A-Herzog/Warteschlangensimulator/wiki/Pseudorandom-number-generators).

## Simulator

The simulations are carried out using the open source DES [**Warteschlangensimulator**](https://a-herzog.github.io/Warteschlangensimulator/) which has to be downloaded separately. Version 6.1alpha1 or higher is required to reproduce the results. The simulation Python scripts (see next section) communicate with Warteschlangensimulator via a localhost socket connection. To start the socket-based simulation server in Warteschlangensimulator:

* In GUI mode: Click **Extras** -> **Server services**, select 10000 as the port for the socket server and click **Start socket server**.
* In CLI mode: Run Warteschlangensimulator (via `Simulator.bat` oder `Simulator.sh`) with the command-line arguments: `ServerSocket 10000`.

## Running the simulations

The scripts for running the simulations are named `RunSimulations*.py` for the models corresponding to the numbers in the report. The scripts require a running Warteschlangensimulator socket server at port 10000 on localhost.

The models to be simulated are loaded from the `models` subfolder. The simulation results are stored in the `results*.txt` files in the `statistics` subfolder. New simulation results are added as new lines to the files. So if you want to start from scratch, delete the old results files first.

## Processing the results

The scripts `Results*.ipynb` will generate the tables and charts from the data stored in the `statistics` folder.

## Models and results

A detailed discussion of the different analyzed pseudorandom numbers generators is be presented in the report.

Result tables, the corresponding simulation models and the results raw data tables can be found on there pages:

* [**Models 1a and 1b: Direct PRNG comparison results**](Benchmark-Direct-PRNG-Comparison.md)
* [**Models 2a and 2b: Queueing model results**](Benchmark-Queueing-Models.md)
* [**Models 3a and 3b: Queueing model with branching results**](Benchmark-Queueing-Models-Branching.md)

## Contact

[Alexander Herzog](https://github.com/A-Herzog)

[![Orcid](ORCID-iD_icon_vector.svg) orcid.org/0009-0006-4303-9011](https://orcid.org/0009-0006-4303-9011)
