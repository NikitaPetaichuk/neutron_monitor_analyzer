# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_NeutronMonitorDataAnalizer(object):
    def setupUi(self, NeutronMonitorDataAnalizer):
        if not NeutronMonitorDataAnalizer.objectName():
            NeutronMonitorDataAnalizer.setObjectName(u"NeutronMonitorDataAnalizer")
        NeutronMonitorDataAnalizer.resize(800, 179)
        self.verticalLayoutWidget = QWidget(NeutronMonitorDataAnalizer)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 10, 781, 151))
        self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.select_file_layout = QHBoxLayout()
        self.select_file_layout.setObjectName(u"select_file_layout")
        self.neutron_monitor_data_file_path_input = QLineEdit(self.verticalLayoutWidget)
        self.neutron_monitor_data_file_path_input.setObjectName(u"neutron_monitor_data_file_path_input")

        self.select_file_layout.addWidget(self.neutron_monitor_data_file_path_input)

        self.select_file_button = QPushButton(self.verticalLayoutWidget)
        self.select_file_button.setObjectName(u"select_file_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_button.sizePolicy().hasHeightForWidth())
        self.select_file_button.setSizePolicy(sizePolicy)
        self.select_file_button.setMinimumSize(QSize(100, 0))

        self.select_file_layout.addWidget(self.select_file_button)


        self.main_layout.addLayout(self.select_file_layout)

        self.analize_button = QPushButton(self.verticalLayoutWidget)
        self.analize_button.setObjectName(u"analize_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.analize_button.sizePolicy().hasHeightForWidth())
        self.analize_button.setSizePolicy(sizePolicy1)

        self.main_layout.addWidget(self.analize_button)

        self.analysis_result_label = QLabel(self.verticalLayoutWidget)
        self.analysis_result_label.setObjectName(u"analysis_result_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.analysis_result_label.sizePolicy().hasHeightForWidth())
        self.analysis_result_label.setSizePolicy(sizePolicy2)
        self.analysis_result_label.setMaximumSize(QSize(16777215, 20))

        self.main_layout.addWidget(self.analysis_result_label)


        self.retranslateUi(NeutronMonitorDataAnalizer)

        QMetaObject.connectSlotsByName(NeutronMonitorDataAnalizer)
    # setupUi

    def retranslateUi(self, NeutronMonitorDataAnalizer):
        NeutronMonitorDataAnalizer.setWindowTitle(QCoreApplication.translate("NeutronMonitorDataAnalizer", u"NeutronMonitorDataAnalizer", None))
        self.neutron_monitor_data_file_path_input.setPlaceholderText(QCoreApplication.translate("NeutronMonitorDataAnalizer", u"Write the path to the file with the neutron monitor data", None))
        self.select_file_button.setText(QCoreApplication.translate("NeutronMonitorDataAnalizer", u"Search", None))
        self.analize_button.setText(QCoreApplication.translate("NeutronMonitorDataAnalizer", u"Analize neutron monitor data for the selected day", None))
        self.analysis_result_label.setText(QCoreApplication.translate("NeutronMonitorDataAnalizer", u"Analysis result: ", None))
    # retranslateUi

