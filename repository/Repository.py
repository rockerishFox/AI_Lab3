from Utils import read_network, get_parameters, read_gml


class Repository:
    def __init__(self, fileName):
        self.__fileName = fileName

    def getData(self):
        net = read_gml(self.__fileName)
        p = get_parameters(net)

        return net, p
