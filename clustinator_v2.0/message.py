import json


class Message:

    def __init__(self, header, cluster_mean):
        self.header = header
        self.cluster_mean = cluster_mean

    def build_json(self):
        self.header['mean-markov-chains'] = [self.cluster_mean]

        return json.dumps(self.header)
