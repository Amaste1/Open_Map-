from tkinter import *
import tkintermapview



window = Tk()
window.title('kirill')
window.geometry('800x800+300+50')
map_widget = tkintermapview.TkinterMapView(window, width=800, height=800, corner_radius=0)
map_widget.place(x = 0, y = 0)

map_widget.set_address('Москва Россия')

window.mainloop()