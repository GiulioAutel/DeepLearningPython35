
"""
    Testing code for different neural network configurations.
    Adapted for Python 3.5.2

    Usage in shell:
        python3.5 test.py

    Network (network.py and network2.py) parameters:
        2nd param is epochs count
        3rd param is batch size
        4th param is learning rate (eta)

    Author:
        Michał Dobrzański, 2016
        dobrzanski.michal.daniel@gmail.com
"""

# ----------------------
# - read the input data:

import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

import network2

net = network2.Network([784, 30, 30, 10], cost=network2.CrossEntropyCost)

net.SGD(training_data, 500, 10, 0.1, 25, 5, evaluation_data=validation_data,
    monitor_evaluation_accuracy=True, early_stopping=True)
