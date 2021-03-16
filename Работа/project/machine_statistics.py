import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import date, timedelta
import mysql.connector
from mysql.connector import Error
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.size'] = 12.0


class MachineStatistics:

    def __init__(self):
        self.machines_id = {1: '11010401', 2: '11030401', 4: '12040401', 5: '12060401', 6: '13070401'}
        self.today = date.today()
        self.prev_month_last_day = self.today.replace(day=1) - timedelta(days=1)
        self.prev_month_start_day = self.today.replace(day=1) - timedelta(days=self.prev_month_last_day.day)
        self.curr_month_start_day = self.today.replace(day=1)

    def read_database(self, date_in, date_out, id_num=1):
        conn = mysql.connector.connect(host='172.15.0.225',
                                       database='dispall_cbk',
                                       user='reader',
                                       password='12341234')

        query = '''SELECT date_in
                 FROM ustr
                 WHERE id= {id} and znach>0 and
                 date_in BETWEEN  "{datein}" and "{dateout}" '''.format(datein=date_in,
                                                                        dateout=date_out,
                                                                        id=self.machines_id[id_num])
        df = pd.read_sql_query(query, conn)
        df = df.rename(columns={'date_in': 'date'})
        return df

    def find_diff(self, df):
        df['ts'] = df.date.values.astype(np.int64) // 10 ** 9
        df_diff = pd.DataFrame(np.diff(df.ts), columns=['time_diff'])
        return df_diff

    def prev_mon_date(self, id_num=1, time=300):
        day_in = str(self.prev_month_start_day) + ' 00:00:00'
        day_out = str(self.prev_month_last_day) + ' 23:59:59'
        df = self.find_diff(self.read_database(day_in, day_out, id_num))

        # day_in_sec = dt.strptime(day_in,'%Y-%m-%d %H:%M:%S').timestamp()
        # day_out_sec = dt.strptime(day_out,'%Y-%m-%d %H:%M:%S').timestamp()

        down_time = df.query('time_diff > @time').time_diff.sum()  # время простоя
        total_time = df.time_diff.sum()  # общее время
        work_time = total_time - down_time  # время работы

        plot_df = pd.DataFrame([down_time, work_time], index=['Время простоя', 'Время работы'], columns=['секунды'])
        return plot_df

    def curr_mon_date(self, id_num=1, time=300):
        day_in = str(self.curr_month_start_day) + ' 00:00:00'
        day_out = str(self.today) + ' 23:59:59'
        df = self.find_diff(self.read_database(day_in, day_out, id_num))
        # day_in_sec = dt.strptime(day_in,'%Y-%m-%d %H:%M:%S').timestamp()
        # day_out_sec = dt.strptime(day_out,'%Y-%m-%d %H:%M:%S').timestamp()

        down_time = df.query('time_diff > @time').time_diff.sum()  # время простоя
        total_time = df.time_diff.sum()  # общее время
        work_time = total_time - down_time  # время работы

        plot_df = pd.DataFrame([down_time, work_time], index=['Время простоя', 'Время работы'], columns=['секунды'])
        return plot_df

    def selected_date(self, day_in, day_out, id_num=1, time=300):
        df = self.find_diff(self.read_database(day_in, day_out, id_num))

        down_time = df.query('time_diff > @time').time_diff.sum()  # время простоя
        total_time = df.time_diff.sum()  # общее время
        work_time = total_time - down_time  # время работы

        plot_df = pd.DataFrame([down_time, work_time], index=['Время простоя', 'Время работы'], columns=['секунды'])

        return plot_df


    def bild_plot(self,plot_df):
        plt.rcParams['figure.facecolor'] = '#262a2f'
        plt.rcParams['legend.frameon'] = 'False'

        vals = plot_df['секунды']
        labels = ['Время простоя', 'Время работы']
        explode = (0.1, 0)
        fig, ax = plt.subplots(figsize=(10,10))

        ax.pie(vals, labels=None, autopct='%1.1f%%', shadow=False,
               explode=explode,
               rotatelabels=True,
               colors=('#ff5533', 'w'),
               pctdistance=0.6,
               textprops=dict(color="black"),
               radius=1.4)
        #ax.axis('equal')
        return fig, ax


    def test_plot(self, id_num=1, time=400):
        day_in = str(self.curr_month_start_day) + ' 00:00:00'
        day_out = str(self.today) + ' 23:59:59'
        # day_in = str(self.prev_month_start_day) + ' 00:00:00'
        # day_out = str(self.prev_month_last_day) + ' 23:59:59'
        df = self.find_diff(self.read_database(day_in, day_out, id_num))

        down_time = df.query('time_diff > @time').time_diff.sum()  # время простоя
        total_time = df.time_diff.sum()  # общее время
        work_time = total_time - down_time  # время работы
        plot_df = pd.DataFrame([down_time, work_time], index=['Время простоя', 'Время работы'], columns=['секунды'])
        return plot_df