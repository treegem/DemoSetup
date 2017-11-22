import os

import matplotlib.pyplot as plt
import numpy as np

from utility.config import paths


def plot_data(f, mes_data, path, description='raw'):
    plt.close('all')
    plt.figure(figsize=(7, 5))
    plt.plot(mes_data[:, 0], mes_data[:, 1])
    f_name = os.path.splitext(f)[0]
    plt.savefig(os.path.join(path, '{}_{}.jpg'.format(f_name, description)))


def measurements_per_point(filename):
    with open(filename, 'r') as of:
        for i, line in enumerate(of):
            if i == 7:
                mes_per_point = int(line.split()[-1])
            elif i > 7:
                break
    return mes_per_point


def load_data(path):
    mes_per_point = measurements_per_point(filename=path)
    return np.loadtxt(fname=path, skiprows=15, usecols=[0, 2], delimiter=';')[::mes_per_point]


def run_main(path):
    for f in os.listdir(path):
        if not f.endswith('.txt'):
            continue

        full_path = os.path.join(path, f)

        mes_data_raw = load_data(path=full_path)
        plot_data(f, mes_data_raw, path)


if __name__ == '__main__':
    FOLDER = '171122_odmr_rabis_echos'
    MES_PATH = os.path.join(paths['saves'], FOLDER, 'pulsed')
    run_main(MES_PATH)
