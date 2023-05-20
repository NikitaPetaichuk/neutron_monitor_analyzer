# This Python file uses the following encoding: utf-8
import time

import numpy as np
import pywt
import torch


def _do_wavelet_transform(neutron_monitor_data):
    padded_neutron_monitor_data = np.pad(neutron_monitor_data, 5760, 'symmetric')
    signal_sampling_freq, wavelet_central_freq = 0.016, pywt.central_frequency(pywt.Wavelet('coif2'))
    freq_boundaries = [0.000005, 0.016]
    scales_range = [wavelet_central_freq / (freq * (1 / signal_sampling_freq)) for freq in freq_boundaries]
    scales = np.arange(scales_range[1], scales_range[0], 10)
    coefficients, _ = pywt.cwt(padded_neutron_monitor_data, scales, 'mexh')
    coefficients = coefficients[:, 5759:len(padded_neutron_monitor_data) - 5761]
    wavelet_matrix = coefficients[:, 2876:4316]
    return wavelet_matrix


def _analize_data_via_lenet_model(analize_model, wavelet_matrix):
    wavelet_preprocessed_matrix = np.expand_dims(wavelet_matrix.astype('float32'), axis=0)
    wavelet_tensor = torch.from_numpy(wavelet_preprocessed_matrix)
    _, probs = analize_model(wavelet_tensor)
    _, predicted_label = torch.max(probs, 0)
    return predicted_label


def process_neutron_monitor_data(analize_model, neutron_monitor_data, timestamps, progress):
    start_wavelet_time = time.time()
    wavelet_matrix = _do_wavelet_transform(neutron_monitor_data)
    print(f"Time to do wavelet transformation: {time.time() - start_wavelet_time} seconds")
    progress.setValue(9)
    time.sleep(1)

    start_process_time = time.time()
    day_class = _analize_data_via_lenet_model(analize_model, wavelet_matrix)
    print(f"Time to process data via model: {time.time() - start_process_time} seconds")
    progress.setValue(10)
    return day_class, wavelet_matrix
