import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5 import QtGui,QtCore
from AppMainWindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import matplotlib as mpl
from machine_statistics import MachineStatistics

b = MachineStatistics()
class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self,fig,parent=None):
        self.fig = fig
        FigureCanvasQTAgg.__init__(self,self.fig)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

def plot():
    #plt.rcParams['figure.facecolor'] = '#262a2f'
    #plt.rcParams['legend.frameon'] = 'False'
    #mpl.rcParams['axes.facecolor'] = 'ffffff'
    mpl.rcParams['font.size'] = 10
    fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3, figsize=(16,10))
    axes = [ax1,ax2,ax3,ax4,ax5,ax6]
    vals = [10,20]
    for ax in axes:
        ax.pie(vals, labels=vals, autopct='%1.1f%%', shadow=False,
               rotatelabels=True,
               colors=('#ff5533', 'w'),
               pctdistance=0.7,
               textprops=dict(color="black"),
               radius=0.1)
    #plt.axis('off')
    #(nrows=1, ncols=1,figsize= (10,7), dpi=85, facecolor='white', frameon=True, edgecolor='black', linewidth=1)
    # fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)
    # ax.grid(True, c='lightgrey', alpha=0.5)
    # ax.set_xlabel('', fontsize=8)
    # ax.set_ylabel('', fontsize=8)
    # ax.set_title('Диаграмма', fontsize=10)
    vals[1] +=10
    return fig, axes

def prepare_canvas_and_toolbar(widget,parent= None):#(func,wiget,id_num,time=300,parent= None):
    parent.fig, parent.ax = plot()#func(id_num,time)

    # fig, ax = func(id_num, time)
    parent.componovka_for_mpl = QVBoxLayout(widget)

    # if parent.canvas:
    #     parent.companovka_for_mpl.removeWidget(parent.canvas)
    #     parent.canvas.deleteLater()
    #     parent.canvas.hide()

    parent.canvas = MyMplCanvas(parent.fig) #parent.fig
    parent.componovka_for_mpl.addWidget(parent.canvas)




class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # self.PrevMonPlot.setMaximumSize(300,300)
        # self.CurMonPlot.setMaximumSize(300, 300)
        #self.curr_plot_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.curr_plot_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.show_curr_mon_plots()
        self.btn_functions()
        # prepare_canvas_and_toolbar(self.curr_plot_widget, parent=self)
        # prepare_canvas_and_toolbar(self.prev_plot_widget, parent=self)
        #self.time_curr_mon.setWordWrapMode(QtGui.QTextOption.NoWrap)
        #prepare_canvas_and_toolbar(parent=self)
        self.btn_toggle.clicked.connect(lambda: self.toggleMenu(250, True))

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # получаем значение Width
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standart = 150

            # задаем макс значание width
            if width == 150:
                widthExtend = maxExtend
            else:
                widthExtend = standart

            # анимация
            self.animation = QPropertyAnimation(self.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def btn_functions(self):

        # кнопки перехода между страницами
        self.btn_cur_mon.clicked.connect(lambda: self.Pages_Widjet.setCurrentWidget(self.curr_mon_page))
        self.btn_prev_mon.clicked.connect(lambda: self.Pages_Widjet.setCurrentWidget(self.prev_mon_page))
        self.btn_select_date.clicked.connect(self.temp_plot)

        #self.btn__select_date.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.selected_date_page))
        # self.btn__select_date.clicked.connect()
        # кнопки обновления страниц
        self.update_curr_mon.clicked.connect(self.show_curr_mon_plots)
        #self.update_prev_mon.clicked.connect(self.show_prev_mon_plots)


    def temp_plot(self):
        # #plot_df = b.test_plot()
        # explode = (0.1, 0)
        # vals = [10,20] #plot_df['секунды']

        self.ax.clear()
        # for ax in self.ax:
        #     ax.pie(vals, labels=vals, autopct='%1.1f%%', shadow=False,
        #         explode=explode,
        #         rotatelabels=True,
        #         colors=('#ff5533', 'w'),
        #         pctdistance=0.7,
        #         textprops=dict(color="black"),
        #         radius=0.1)

        self.fig.canvas.draw()
    def show_curr_mon_plots(self):
        prepare_canvas_and_toolbar(self.curr_plot_widget, parent=self)


    def show_prev_mon_plots(self):

        prepare_canvas_and_toolbar(b.prev_mon_pie_plot,self.prev_plot_1,1, parent=self)
        prepare_canvas_and_toolbar(b.prev_mon_pie_plot,self.prev_plot_2,2, parent=self)
        prepare_canvas_and_toolbar(b.prev_mon_pie_plot,self.prev_plot_3,4, parent=self)
        prepare_canvas_and_toolbar(b.prev_mon_pie_plot,self.prev_plot_4,5,parent=self)
        prepare_canvas_and_toolbar(b.prev_mon_pie_plot,self.prev_plot_5,6, parent=self)


def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_application()

