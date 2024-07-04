# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget, QMessageBox, QCompleter, QVBoxLayout, QDialog)

class ModalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.setWindowTitle("Map")
        self.setModal(True)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ceci est une fenêtre modale"))
        self.setLayout(layout)
        self.resize(300, 300)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(404, 344)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mapnpc = QWidget()
        self.mapnpc.setObjectName(u"mapnpc")
        self.mapnpc.setEnabled(True)
        self.npclabel = QLabel(self.mapnpc)
        self.npclabel.setObjectName(u"npclabel")
        self.npclabel.setGeometry(QRect(10, 10, 161, 20))
        self.npclabel.setAutoFillBackground(True)
        self.npclabel.setFrameShape(QFrame.StyledPanel)
        self.npclabel.setAlignment(Qt.AlignCenter)

        # NPC List #
        self.npclist = QComboBox(self.mapnpc)
        self.npclist.setObjectName(u"npclist")
        self.npclist.setGeometry(QRect(10, 40, 161, 22))
        self.npclist.setEditable(True)

        # creation of a list template
        self.npclistmodel = QStringListModel()

        npcCompleter = QCompleter(self.npclistmodel, self.npclist)
        npcCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        npcCompleter.setFilterMode(Qt.MatchContains)
        self.npclist.setCompleter(npcCompleter)
        # -------- #

        self.npcimg = QLabel(self.mapnpc)
        self.npcimg.setObjectName(u"npcimg")
        self.npcimg.setGeometry(QRect(10, 70, 161, 201))
        self.npcimg.setAutoFillBackground(True)
        self.npcimg.setAlignment(Qt.AlignCenter)
        self.npcname = QLabel(self.mapnpc)
        self.npcname.setObjectName(u"npcname")
        self.npcname.setGeometry(QRect(200, 10, 171, 20))
        self.npcname.setFrameShape(QFrame.StyledPanel)
        self.npcname.setAlignment(Qt.AlignCenter)
        self.maplabel = QLabel(self.mapnpc)
        self.maplabel.setObjectName(u"maplabel")
        self.maplabel.setGeometry(QRect(200, 70, 171, 21))
        self.maplabel.setAutoFillBackground(True)
        self.maplabel.setFrameShape(QFrame.StyledPanel)
        self.maplabel.setAlignment(Qt.AlignCenter)

        self.maplist = QComboBox(self.mapnpc)
        self.maplist.setObjectName(u"maplist")
        self.maplist.setGeometry(QRect(200, 100, 171, 22))
        self.maplist.setEditable(True)

        # creation of a list template
        self.maplistmodel = QStringListModel()

        mapCompleter = QCompleter(self.maplistmodel, self.maplist)
        mapCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        mapCompleter.setFilterMode(Qt.MatchContains)
        self.maplist.setCompleter(mapCompleter)
        # -------- #

        self.posxlabel = QLabel(self.mapnpc)
        self.posxlabel.setObjectName(u"posxlabel")
        self.posxlabel.setGeometry(QRect(200, 130, 71, 16))
        self.posxlabel.setAlignment(Qt.AlignCenter)
        self.posylabel = QLabel(self.mapnpc)
        self.posylabel.setObjectName(u"posylabel")
        self.posylabel.setGeometry(QRect(290, 130, 71, 16))
        self.posylabel.setAlignment(Qt.AlignCenter)
        self.npcinput = QLineEdit(self.mapnpc)
        self.npcinput.setObjectName(u"npcinput")
        self.npcinput.setGeometry(QRect(200, 40, 171, 22))
        self.inputposx = QLineEdit(self.mapnpc)
        self.inputposx.setObjectName(u"inputposx")
        self.inputposx.setGeometry(QRect(200, 150, 71, 22))
        self.inputposx.setAlignment(Qt.AlignCenter)
        self.inputposy = QLineEdit(self.mapnpc)
        self.inputposy.setObjectName(u"inputposy")
        self.inputposy.setGeometry(QRect(290, 150, 71, 22))
        self.inputposy.setAlignment(Qt.AlignCenter)
        self.maplabel_2 = QLabel(self.mapnpc)
        self.maplabel_2.setObjectName(u"maplabel_2")
        self.maplabel_2.setGeometry(QRect(200, 180, 161, 16))
        self.maplabel_2.setAutoFillBackground(True)
        self.maplabel_2.setAlignment(Qt.AlignCenter)
        self.inputpos = QLineEdit(self.mapnpc)
        self.inputpos.setObjectName(u"inputpos")
        self.inputpos.setGeometry(QRect(200, 210, 161, 22))
        self.inputpos.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.mapnpc)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 270, 75, 24))
        self.showmapbutton = QPushButton(self.mapnpc)
        self.showmapbutton.setObjectName(u"showmapbutton")
        self.showmapbutton.setGeometry(QRect(200, 270, 75, 24))
        self.tabWidget.addTab(self.mapnpc, "")
        self.shopitem = QWidget()
        self.shopitem.setObjectName(u"shopitem")
        self.npclabel_2 = QLabel(self.shopitem)
        self.npclabel_2.setObjectName(u"npclabel_2")
        self.npclabel_2.setGeometry(QRect(10, 10, 161, 20))
        self.npclabel_2.setAutoFillBackground(True)
        self.npclabel_2.setFrameShape(QFrame.StyledPanel)
        self.npclabel_2.setAlignment(Qt.AlignCenter)
        self.npcinput_2 = QLineEdit(self.shopitem)
        self.npcinput_2.setObjectName(u"npcinput_2")
        self.npcinput_2.setGeometry(QRect(10, 40, 161, 22))
        self.npclabel_3 = QLabel(self.shopitem)
        self.npclabel_3.setObjectName(u"npclabel_3")
        self.npclabel_3.setGeometry(QRect(10, 70, 161, 20))
        self.npclabel_3.setAutoFillBackground(True)
        self.npclabel_3.setFrameShape(QFrame.StyledPanel)
        self.npclabel_3.setAlignment(Qt.AlignCenter)
        self.npcinput_3 = QLineEdit(self.shopitem)
        self.npcinput_3.setObjectName(u"npcinput_3")
        self.npcinput_3.setGeometry(QRect(10, 100, 161, 22))
        self.npclabel_4 = QLabel(self.shopitem)
        self.npclabel_4.setObjectName(u"npclabel_4")
        self.npclabel_4.setGeometry(QRect(190, 10, 161, 20))
        self.npclabel_4.setAutoFillBackground(True)
        self.npclabel_4.setFrameShape(QFrame.StyledPanel)
        self.npclabel_4.setAlignment(Qt.AlignCenter)
        self.npcinput_4 = QLineEdit(self.shopitem)
        self.npcinput_4.setObjectName(u"npcinput_4")
        self.npcinput_4.setGeometry(QRect(190, 40, 161, 22))
        self.pushButton_2 = QPushButton(self.shopitem)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 270, 75, 24))
        self.tabWidget.addTab(self.shopitem, "")
        self.shop = QWidget()
        self.shop.setObjectName(u"shop")
        self.pushButton_3 = QPushButton(self.shop)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 270, 75, 24))
        self.npclabel_5 = QLabel(self.shop)
        self.npclabel_5.setObjectName(u"npclabel_5")
        self.npclabel_5.setGeometry(QRect(10, 10, 161, 20))
        self.npclabel_5.setAutoFillBackground(True)
        self.npclabel_5.setFrameShape(QFrame.StyledPanel)
        self.npclabel_5.setAlignment(Qt.AlignCenter)
        self.npclist_2 = QComboBox(self.shop)
        self.npclist_2.addItem("")
        self.npclist_2.addItem("")
        self.npclist_2.addItem("")
        self.npclist_2.setObjectName(u"npclist_2")
        self.npclist_2.setGeometry(QRect(10, 40, 161, 22))
        self.npclist_2.setEditable(False)
        self.npclabel_6 = QLabel(self.shop)
        self.npclabel_6.setObjectName(u"npclabel_6")
        self.npclabel_6.setGeometry(QRect(10, 70, 161, 20))
        self.npclabel_6.setAutoFillBackground(True)
        self.npclabel_6.setFrameShape(QFrame.StyledPanel)
        self.npclabel_6.setAlignment(Qt.AlignCenter)
        self.npcinput_5 = QLineEdit(self.shop)
        self.npcinput_5.setObjectName(u"npcinput_5")
        self.npcinput_5.setGeometry(QRect(10, 100, 161, 22))
        self.npclabel_7 = QLabel(self.shop)
        self.npclabel_7.setObjectName(u"npclabel_7")
        self.npclabel_7.setGeometry(QRect(190, 10, 161, 20))
        self.npclabel_7.setAutoFillBackground(True)
        self.npclabel_7.setFrameShape(QFrame.StyledPanel)
        self.npclabel_7.setAlignment(Qt.AlignCenter)
        self.npcinput_6 = QLineEdit(self.shop)
        self.npcinput_6.setObjectName(u"npcinput_6")
        self.npcinput_6.setGeometry(QRect(190, 40, 161, 22))
        self.npclabel_8 = QLabel(self.shop)
        self.npclabel_8.setObjectName(u"npclabel_8")
        self.npclabel_8.setGeometry(QRect(190, 70, 161, 20))
        self.npclabel_8.setAutoFillBackground(True)
        self.npclabel_8.setFrameShape(QFrame.StyledPanel)
        self.npclabel_8.setAlignment(Qt.AlignCenter)
        self.npcinput_7 = QLineEdit(self.shop)
        self.npcinput_7.setObjectName(u"npcinput_7")
        self.npcinput_7.setGeometry(QRect(190, 100, 161, 22))
        self.npclabel_9 = QLabel(self.shop)
        self.npclabel_9.setObjectName(u"npclabel_9")
        self.npclabel_9.setGeometry(QRect(10, 130, 161, 20))
        self.npclabel_9.setAutoFillBackground(True)
        self.npclabel_9.setFrameShape(QFrame.StyledPanel)
        self.npclabel_9.setAlignment(Qt.AlignCenter)
        self.npcinput_8 = QLineEdit(self.shop)
        self.npcinput_8.setObjectName(u"npcinput_8")
        self.npcinput_8.setGeometry(QRect(10, 160, 161, 22))
        self.npclabel_10 = QLabel(self.shop)
        self.npclabel_10.setObjectName(u"npclabel_10")
        self.npclabel_10.setGeometry(QRect(190, 130, 161, 20))
        self.npclabel_10.setAutoFillBackground(True)
        self.npclabel_10.setFrameShape(QFrame.StyledPanel)
        self.npclabel_10.setAlignment(Qt.AlignCenter)
        self.npcinput_9 = QLineEdit(self.shop)
        self.npcinput_9.setObjectName(u"npcinput_9")
        self.npcinput_9.setGeometry(QRect(190, 160, 161, 22))
        self.tabWidget.addTab(self.shop, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"NPC Maker", None))
#if QT_CONFIG(accessibility)
        self.mapnpc.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.npclabel.setText(QCoreApplication.translate("Widget", u"NPC", None))

        self.npcimg.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.npcname.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.maplabel.setText(QCoreApplication.translate("Widget", u"Map", None))

        self.posxlabel.setText(QCoreApplication.translate("Widget", u"POS X", None))
        self.posylabel.setText(QCoreApplication.translate("Widget", u"POS Y", None))
        self.maplabel_2.setText(QCoreApplication.translate("Widget", u"Direction", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Ajouter", None))
        self.showmapbutton.setText(QCoreApplication.translate("Widget", u"Show Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapnpc), QCoreApplication.translate("Widget", u"NPC", None))
        self.npclabel_2.setText(QCoreApplication.translate("Widget", u"Map NPC ID", None))
        self.npclabel_3.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.npclabel_4.setText(QCoreApplication.translate("Widget", u"Shop Type", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Ajouter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shopitem), QCoreApplication.translate("Widget", u"Shop", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Ajouter", None))
        self.npclabel_5.setText(QCoreApplication.translate("Widget", u"Item", None))
        self.npclist_2.setItemText(0, QCoreApplication.translate("Widget", u"Baton", None))
        self.npclist_2.setItemText(1, QCoreApplication.translate("Widget", u"Arc", None))
        self.npclist_2.setItemText(2, QCoreApplication.translate("Widget", u"Epee", None))

        self.npclabel_6.setText(QCoreApplication.translate("Widget", u"Rare", None))
        self.npclabel_7.setText(QCoreApplication.translate("Widget", u"Shop ID", None))
        self.npclabel_8.setText(QCoreApplication.translate("Widget", u"Slot", None))
        self.npclabel_9.setText(QCoreApplication.translate("Widget", u"Upgrade", None))
        self.npclabel_10.setText(QCoreApplication.translate("Widget", u"Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shop), QCoreApplication.translate("Widget", u"Shop Item", None))
    # retranslateUi

    @staticmethod
    def show_message_box(self, text, informtext, title):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(text)
        msg_box.setInformativeText(informtext)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg_box.exec()

        if retval == QMessageBox.Ok:
            print("OK pressed")
        else:
            print("Cancel pressed")

    def modal(self):    
        # Créer une instance de la fenêtre modale
        modal = ModalDialog(self)
        modal.exec()