import os

import matplotlib.pyplot as plt
import numpy as np

from utility.config import paths


def measurements_per_point(filename):
    with open(filename, 'r') as of:
        for i, line in enumerate(of):
            if i == 6:
                mes_per_point = int(line.split()[-1])
            elif i > 6:
                break
    return mes_per_point


def load_data(path):
    mes_per_point = measurements_per_point(filename=path)
    return np.loadtxt(fname=path, skiprows=14, usecols=[1, 3], delimiter=';')[::mes_per_point]


def run_main(path):
    for f in os.listdir(path):
        if not f.endswith('.txt'):
            continue

        full_path = os.path.join(path, f)

        mes_data_raw = load_data(path=full_path)
        plot_data(f, mes_data_raw, path)

        corrected_data = linear_correct(mes_data_raw, n_points=3, lskip=3, rskip=3)
        plot_data(f, corrected_data, path, description='corrected')


def linear_correct(raw_data, n_points, lskip, rskip):
    fitting_edge_data = np.zeros((2 * n_points, 2))
    fitting_edge_data[:n_points] = raw_data[lskip:lskip + n_points]
    if rskip == 0:
        fitting_edge_data[n_points:] = raw_data[-rskip - n_points:]
    else:
        fitting_edge_data[n_points:] = raw_data[-rskip - n_points:-rskip]
    fit = np.polyfit(fitting_edge_data[:, 0], fitting_edge_data[:, 1], 1)
    fit_fn = np.poly1d(fit)
    # fit_fn takes x input and estimates y
    corrected_data = np.copy(raw_data)
    for i, data in enumerate(raw_data):
        linear_correction = fit_fn(data[0])
        corrected_data[i, 1] = data[1] - linear_correction + np.average(raw_data[:, 1])
    return corrected_data


def plot_data(f, mes_data, path, description='raw'):
    plt.close('all')
    plt.figure(figsize=(7, 5))
    plt.plot(mes_data[:, 0], mes_data[:, 1])
    f_name = os.path.splitext(f)[0]
    plt.savefig(os.path.join(path, '{}_{}.jpg'.format(f_name, description)))


if __name__ == '__main__':
    FOLDER = ''
    MES_PATH = os.path.join(paths['saves'], FOLDER, 'odmr')
    run_main(MES_PATH)
