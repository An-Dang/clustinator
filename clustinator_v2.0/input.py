import re
import pandas as pd
from more_itertools import unique_everseen

class Input:

    def __init__(self, sessions_file):
        self.sessions_file = sessions_file

    def sessions(self):
        """
        In this function the raw session data is load in. Beside from the whole session data can be slice out dataframe.
        :param slice_from: start slice from - int
        :param slice_to: end slice to - int
        :return: The whole dataframe or sliced dataframe and the states.
        """
        df = pd.read_json(self.sessions_file)
        INITIAL = 'INITIAL'
        end_sign = '$'
        s_r_dict = {}
        states = []

        for sessions in df['sessions']:
            tmp_list = []
            key = sessions['unique-id']
            value = sessions['requests'][0]['endpoint']
            for value in sessions['requests']:
                tmp_list.append(value['endpoint'])
                states.append(value['endpoint'])
            s_r_dict[key] = tmp_list

        if len(states) > len(tmp_list):
            states = list(unique_everseen(states + tmp_list))
        else:
            states = list(unique_everseen(tmp_list + states))

        states.insert(0, INITIAL)
        states.append(end_sign)
        return s_r_dict, states

    def cluster_param(self):
        df = pd.read_json(self.sessions_file)
        epsilon = df.loc[[0], ['epsilon']].get_values()[0][0]
        min_samples = df.loc[[0], ['min-sample-size']].get_values()[0][0]
        return epsilon, min_samples

    def get_header(self):
        df = pd.read_json(self.sessions_file)
        df = df[['app-id', 'version', 'tailoring', 'min-sample-size', 'start-micros',
                 'interval-start-micros', 'end-micros']].to_dict('r')[0]
        return df
