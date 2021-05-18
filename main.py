import tkinter as tk
import Toolbar as tb
import Playground as pg

window = tk.Tk()
window.configure(background="#1f1f1f")
window.resizable(False, False)
window.title("hahaha")
frm_tb = tk.Frame(window)
frm_pg = tk.Frame(window, padx=50, pady=50)
frm_tb.configure(background="#1f1f1f")
frm_pg.configure(background="#1f1f1f")

frm_tb.pack(side='left')
frm_pg.pack(side='left')

playground = pg.Playground(frm_pg)
toolbar = tb.Toolbar(frm_tb)

tk.mainloop()
