# This Python file uses the following encoding: utf-8
from datetime import datetime
import csv
from multiprocessing.pool import ThreadPool
import sys

import matplotlib.pyplot as plt
import torch
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QProgressDialog

from process_neutron_monitor_data import process_neutron_monitor_data
from model.neutron_monitor_data_lenet import NeutronMonitorDataLeNet

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_NeutronMonitorDataAnalizer


def _nongui(fun):
    def wrap(*args, **kwargs):
        pool = ThreadPool(processes=1)
        async_process = pool.apply_async(fun, args, kwargs)
        while not async_process.ready():
            async_process.wait(0.01)
            QApplication.processEvents()
        return async_process.get()
    return wrap


@_nongui
def process_data(model, neutron_monitor_data, timestamps, progress):
    return process_neutron_monitor_data(model, neutron_monitor_data, timestamps, progress)


def _create_plots(timestamps, neutron_monitor_data, wavelet_matrix):
    figure, (ax_1, ax_2) = plt.subplots(2, 1, figsize=(12.5, 9))
    figure.canvas.manager.set_window_title('Neutron Monitor Data Plots')

    ax_1.plot(timestamps[2876:4316], neutron_monitor_data[2876:4316])
    ax_1.set_title("Neutron monitor data")
    ax_2.matshow(wavelet_matrix)

    ax_2.set_title("Neutron monitor data after wavelet transformation")
    ax_2.set_aspect(3/2)

    plt.show()


class NeutronMonitorDataAnalizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NeutronMonitorDataAnalizer()
        self.ui.setupUi(self)
        self.ui.select_file_button.clicked.connect(self.select_file_with_neutron_monitor_data)
        self.ui.analize_button.clicked.connect(self.process_neutron_monitor_data)

        self._model = torch.load("./model/model_snapshot", map_location=torch.device('cpu'))

    def select_file_with_neutron_monitor_data(self):
        neutron_monitor_data_file_path, _ = QFileDialog.getOpenFileName(
            self, "Select file with neutron monitor data", "..", "Text files (*.txt)"
        )
        if neutron_monitor_data_file_path:
            self.ui.neutron_monitor_data_file_path_input.setText(neutron_monitor_data_file_path)

    def process_neutron_monitor_data(self):
        neutron_monitor_data_file_path = self.ui.neutron_monitor_data_file_path_input.text()
        with open(neutron_monitor_data_file_path, "r") as neutron_monitor_data_file:
            neutron_monitor_data_reader = csv.reader(neutron_monitor_data_file, delimiter=";")
            timestamps, neutron_monitor_data = [], []
            for row in neutron_monitor_data_reader:
                if len(row) != 0:
                    timestamps.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
                    neutron_monitor_data.append(float(row[1]))

        progress = QProgressDialog("Processing neutron monitor data", "Cancel", 0, 10, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.forceShow()
        progress.setValue(1)

        day_class, wavelet_matrix = process_data(self._model, neutron_monitor_data, timestamps, progress)
        _create_plots(timestamps, neutron_monitor_data, wavelet_matrix)
        if day_class == 0:
            self.ui.analysis_result_label.setText("Analysis result: Calm day")
        elif day_class == 1:
            self.ui.analysis_result_label.setText("Analysis result: Day with weak storm")
        elif day_class == 2:
            self.ui.analysis_result_label.setText("Analysis result: Day with strong storm storm")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NeutronMonitorDataAnalizer()
    widget.show()
    sys.exit(app.exec())
