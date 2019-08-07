import json


class Message:
    """
    DF = todict
    rest appenden
    """
    def __init__(self, header, cluster_mean):
        self.header = header
        self.cluster_mean = cluster_mean

    def build_json(self):
        self.header['mean_markov_chains'] = [self.cluster_mean]

        #print(json.dumps(self.header))

        return json.dumps(self.header)


