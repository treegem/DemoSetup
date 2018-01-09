import os

from plotting.plot_pulsed import load_data, plot_data
from utility.config import paths


def run_main(data_paths, filename, ending='', skip=0):
    data_corrected = corrected_data(data_paths)
    filename = '{}_diff{}'.format(filename, ending)
    plot_data(filename, data_corrected, data_paths['parent'], skip=skip)


def corrected_data(data_paths):
    mes_data_raw = load_data(path=data_paths['data'])
    mes_data_correction = load_data(path=data_paths['correction'])
    # mes_data_raw = mes_data_raw / mes_data_raw[0] * mes_data_correction[0]
    mes_data_raw[:, 1] = (mes_data_raw[:, 1] - mes_data_correction[:, 1])
    return mes_data_raw


if __name__ == '__main__':
    FOLDER = ''
    MES_PATH = os.path.join(paths['saves'], FOLDER, 'pulsed')
    data_name = 'pulsed7_lowbg_corr.txt'
    correction_name = 'pulsed7_lowbg_corr_off.txt'
    run_main({'data': os.path.join(MES_PATH, data_name),
              'correction': os.path.join(MES_PATH, correction_name),
              'parent': MES_PATH},
             filename=os.path.splitext(data_name)[0],
             ending='',
             skip=0)
