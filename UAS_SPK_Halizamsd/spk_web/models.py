import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Oppo():

    def __init__(self) -> None:
        self.oppo = pd.read_csv('data/handphone_202310311540.csv')
        self.smartphone_oppo = np.array(self.oppo)

    @property
    def oppo_data(self):
        data = []
        for oppo in self.smartphone_oppo:
            data.append({'brand': oppo[0]})
        return data

    @property
    def oppo_data_dict(self):
        data = {}
        i = 0
        for oppo in self.smartphone_oppo:
            data[i] = oppo[1]
            i += 1
        return data

    def get_recs(self, kriteria:dict):
        wp = WeightedProduct(self.oppo.to_dict(orient="records"), kriteria)
        return wp.calculate

if __name__ == "__main__":
    a = pd.read_csv('data/handphone_202310311540.csv').to_dict(orient="records")
    print(a)