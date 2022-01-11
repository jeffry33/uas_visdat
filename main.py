from bokeh.models.widgets.tables import TableWidget
import numpy as np
from random import randint

from bokeh.io import curdoc, show, output_notebook
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn, CustomJS, Dropdown
from bokeh.models import ColumnDataSource, Select, Div, Title, WidgetBox, Panel, Tabs, Paragraph
from bokeh.models.widgets import Button

from bokeh.plotting import figure

# from test import datetime
from datetime import date
import bokeh.sampledata

import os

bokeh.sampledata.download()
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
# Helper untuk formatting data date & time
def datetime(x):
    return np.array(x, dtype=np.datetime64)

# Grafik untuk ADJ Close Apple Stock
p1 = figure(x_axis_type="datetime", title="Apple Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Tahun'
p1.yaxis.axis_label = 'Stock'

p1.line(datetime(AAPL['date']), AAPL['adj_close'], line_width=3, color='purple', alpha=0.5)
# Masukan Grafik ke tab 1 # nntinya berguna untuk pindah konten grafik
tab1 = Panel(child=p1, title="Apple Stock")

# Grafik untuk ADJ Close Google Stock
p2 = figure(x_axis_type="datetime", title="Google Stock Closing Prices")
p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Tahun'
p2.yaxis.axis_label = 'Stock'

p2.line(datetime(GOOG['date']), GOOG['adj_close'], line_width=3, color="green", alpha=0.5)
# Masukan Grafik ke tab 2
tab2 = Panel(child=p2, title="Google Stock")

# Grafik untuk ADJ Close IBM Stock
p3 = figure(x_axis_type="datetime", title="IBM Stock Closing Prices")
p3.grid.grid_line_alpha=0.3
p3.xaxis.axis_label = 'Tahun'
p3.yaxis.axis_label = 'Stock'

p3.line(datetime(IBM['date']), IBM['adj_close'], line_width=3, color="red", alpha=0.5)
# Masukan Grafik ke tab 3
tab3 = Panel(child=p3, title="IBM Stock")


# Grafik untuk ADJ Close MSFT Stock
p4 = figure(x_axis_type="datetime", title="MSFT Stock Closing Prices")
p4.grid.grid_line_alpha=0.3
p4.xaxis.axis_label = 'Tahun'
p4.yaxis.axis_label = 'Stock'

p4.line(datetime(MSFT['date']), MSFT['adj_close'], line_width=3, color="blue", alpha=0.5)
# Masukan Grafik ke tab 4
tab4 = Panel(child=p4, title="MSFT Stock")


# Inisiasi Tabel Dataset Apple
data = dict(
        # dates=[date(2014, 3, i+1) for i in range(10)],
        dates=[(AAPL['date'], i+1) for i in range(10)],
        adj_close=[(AAPL['adj_close'], i+1) for i in range(10)],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="dates", title="Date"),
        TableColumn(field="adj_close", title="Adj Close"),
    ]
data_table = DataTable(source=source, columns=columns, width=700, height=280)

# Paragraf untuk Judul Pada Tabel
p = Paragraph(text="""Dataset Closing Stock Market Apple""",
width=400, height=10)

# Tombol Download untuk mengunduh dataset AAPL Stock
source = ColumnDataSource({'Date':AAPL['date'],'Adj_Close':AAPL['adj_close']})
button = Button(label="Download Dataset AAPL Stock", button_type="success")
button.js_on_click(CustomJS(args=dict(source=source),code=open(os.path.join(os.path.dirname(__file__),"download.js")).read()))
# show(button)

# Dropdown
menu = [("Fauzi Dzulfiqar", "item_1"), ("Oktavius Jeffry", "item_2"), ("M Rian Fahriza", "item_3")]

dropdown = Dropdown(label="Dibuat Oleh", button_type="primary", menu=menu)
dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

# Gabungkan semua konten grafik pada 1 tab menggunakan Tabs
Left_content = Tabs(tabs=[tab1, tab2, tab3, tab4])
# Gabungkan dan urutkan sesuai Paragraf, Tabel, Tombol Download, & juga Dropdown
Right_Content = column(p, data_table, button, dropdown)

# Buat Layout dan gabungkan Left & Right Content
layout = row(Left_content, Right_Content)
# show(layout) # akan otomatis membuka Browser (dir)

curdoc().add_root(layout)
# curdoc().title = "Stock Interactive Visualization using Bokeh"
