from settings import OS_SCALE, PROCESSOR_SCALE, BRAND_SCALE

class BaseMethod():

    def __init__(self, data_dict, **bobot):

        self.dataDict = data_dict

        # 1-7
        self.raw_weight = {
            'brand': 6,
            'ram': 5,
            'prosesor': 1,
            'storage': 2,
            'baterai': 4,
            'harga': 7,
            'os': 3
        }

        if bobot:
            for item in bobot.items():
                temp1 = bobot[item[0]]
                temp2 = {v: k for k, v in bobot.items()}[item[1]]

                bobot[item[0]] = item[1]
                bobot[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'nama_brand': oppo['brand'],
            'brand': BRAND_SCALE["".join([x for x in BRAND_SCALE.keys() if x.lower() in oppo['brand'].lower()])],
            'ram': int(oppo['ram'].replace(" GB", "")),
            'prosesor': PROCESSOR_SCALE[oppo['prosesor']],
            'storage': int(oppo['storage'].replace(" GB", "")),
            'baterai': int(oppo['baterai'].replace(" mAh", "")),
            'harga': oppo['harga'],
            'os': OS_SCALE[oppo['os']]

        } for oppo in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        brand = [] # max
        ram = [] # max
        prosesor = [] # max
        os = [] # max
        baterai = [] # max
        harga = [] # min
        storage = []

        for data in self.data:
            brand.append(data['brand'])
            ram.append(data['ram'])
            prosesor.append(data['prosesor'])
            os.append(data['os'])
            baterai.append(data['baterai'])
            harga.append(data['harga'])
            storage.append(data['storage'])

        max_brand = max(brand)
        max_ram = max(ram)
        max_prosesor = max(prosesor)
        max_os = max(os)
        max_baterai = max(baterai)
        min_harga = min(harga)
        max_storage = max(storage)

        return [{
            'nama_brand': data['nama_brand'],
            'brand': data['brand']/max_brand,
            'ram': data['ram']/max_ram, # benefit
            'prosesor': data['prosesor']/max_prosesor, # benefit
            'os': data['os']/max_os, # benefit
            'baterai': data['baterai']/max_baterai, # benefit
            'harga': min_harga/data['harga'], # cost
            'storage': data['storage']/max_storage, # benefit
        } for data in self.data]


class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, bobot):
        super().__init__(data_dict=dataDict, **bobot)

    @property
    def calculate(self):
        weight = self.weight

        # calculate data and weight[WP]
        hasil = {row['nama_brand']:
                row['brand'] ** weight['brand'] *
                row['ram'] ** weight['ram'] *
                row['prosesor'] ** weight['prosesor'] *
                row['os'] ** weight['os'] *
                row['baterai'] ** weight['baterai'] *
                row['harga'] ** (-weight['harga']) *
                row['storage'] ** weight['storage']
                for row in self.normalized_data}


        # sorting
        total_wp = sum(hasil.values())
        for k in hasil:
            hasil[k] = round(hasil[k]/total_wp, 3)
        hasil = dict(sorted(hasil.items(), key=lambda x:x[1], reverse=True))

        # return result
        return hasil

