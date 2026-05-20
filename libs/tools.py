import xml.etree.ElementTree as ET
from libs.socket_connect import QS_socket_connect as QS
import libs.setup as setup

ET.register_namespace('', 'https://a-herzog.github.io')


# Define the namespace for the XML elements
ns = {'QS': 'https://a-herzog.github.io'}


def load_model(xml_file: str, count: int, random_mode: str, seed: int | None = None) -> str:
    """Loads the model from the given XML file and modifies it with the given arrival count and random numbers generator mode.

    Args:
        xml_file (str): The file name of the XML file containing the base model.
        count (int): The number of client arrivals to be simulated.
        random_mode (str): The pseudo random number generators mode to be used in the simulation.
        seed (int, optional): Seed.

    Returns:
        str: The model to be simulated as XML string.
    """

    tree = ET.parse(xml_file)
    root = tree.getroot()
    el = root.find('QS:ModelRandomNumbersMode', ns)
    if el is None:
        raise ValueError("Element 'QS:ModelRandomNumbersMode' not found in the XML file.")
    el.text = random_mode

    el = root.find('QS:ModelClients', ns)
    if el is None:
        raise ValueError("Element 'QS:ModelClients' not found in the XML file.")
    el.text = str(count)

    if seed is not None:
        el = root.find('QS:ModelRandomNumbersSeed', ns)
        if el is None:
            raise ValueError("Element 'QS:ModelClients' not found in the XML file.")
        el.text = str(seed)

    return ET.tostring(root, encoding='utf-8', method='xml')


def run_model(model: str) -> ET.Element:
    """Runs the simulation with the given model and returns the results.

    Args:
        model (str): The model to be simulated as XML string.

    Returns:
        bytes: The result of the simulation as XML string in bytes.
    """

    # Communicate with Warteschlangensimulator via socket connection
    socket = QS(setup.host, setup.port)
    statistics = socket.run_task(model)

    # Load the result of the simulation as XML tree and return the root element
    tree = ET.ElementTree(ET.fromstring(statistics))
    root = tree.getroot()
    if root is None:
        raise ValueError("Failed to get root element from XML tree.")
    return root


def run(xml_file: str, random_mode: str, count: int | None = None) -> ET.Element:
    """Runs the simulation with the given XML file and random number generator mode.
    Args:
        xml_file (str): The file name of the XML file containing the base model.
        random_mode (str): The pseudo random number generators mode to be used in the simulation.
        count (int, optional): Client arrivals to be simulated.

    Returns:
        bytes: The result of the simulation as XML string in bytes.
    """

    # Load base model and set number of arrivals to be simulated and random number generator mode to use in the simulation
    model = load_model(xml_file, count if count is not None else setup.arrival_count, random_mode, None)

    # Run the simulation and return the results
    return run_model(model)


def run_with_seed(xml_file: str, random_mode: str, seed: int, count: int | None = None) -> ET.Element:
    """Runs the simulation with the given XML file and random number generator mode.
    Args:
        xml_file (str): The file name of the XML file containing the base model.
        random_mode (str): The pseudo random number generators mode to be used in the simulation.
        seed (int): Seed.
        count (int, optional): Client arrivals to be simulated.

    Returns:
        bytes: The result of the simulation as XML string in bytes.
    """

    # Load base model and set number of arrivals to be simulated and random number generator mode to use in the simulation
    model = load_model(xml_file, count if count is not None else setup.arrival_count, random_mode, seed)

    # Run the simulation and return the results
    return run_model(model)