import sys

from colorama import Fore, Style
from models import Base, Oppo
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import OS_SCALE, PROCESSOR_SCALE, BRAND_SCALE

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')


class BaseMethod():
    def __init__(self):
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

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k,v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Oppo)
        return [{
            'nama_brand': oppo.brand,
            'brand': BRAND_SCALE["".join([x for x in BRAND_SCALE.keys() if x.lower() in oppo.brand.lower()])],
            'ram': int(oppo.ram.replace(" GB", "")),
            'prosesor': PROCESSOR_SCALE[oppo.prosesor],
            'storage': int(oppo.storage.replace(" GB", "")),
            'baterai': int(oppo.baterai.replace(" mAh", "")),
            'harga': int(oppo.harga),
            'os': OS_SCALE[oppo.os]

        } for oppo in session.scalars(query)]

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
    @property
    def calculate(self):
        weight = self.weight

        # calculate data and weight[WP]
        hasil = {row['nama_brand']: round(
                row['brand'] ** weight['brand'] *
                row['ram'] ** weight['ram'] *
                row['prosesor'] ** weight['prosesor'] *
                row['os'] ** weight['os'] *
                row['baterai'] ** weight['baterai'] *
                row['harga'] ** (-weight['harga']) *
                row['storage'] ** weight['storage']
                , 2)
                for row in self.normalized_data}


        # sorting
        total = sum(hasil.values())
        for s in hasil:
            hasil[s] = round(hasil[s]/total, 2)

        # return result
        return dict(sorted(hasil.items(), key=lambda x:x[1], reverse=True))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight

        # calculate data and weight[SAW]
        result =  {row['nama_brand']:
            round(
                row['brand'] * weight['brand'] +
                row['ram'] * weight['ram'] +
                row['prosesor'] * weight['prosesor'] +
                row['os'] * weight['os'] +
                row['baterai'] * weight['baterai'] +
                row['harga'] * weight['harga'] +
                row['storage'] * weight['storage']
                , 2
            )
            for row in self.normalized_data
        }

        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))


def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
