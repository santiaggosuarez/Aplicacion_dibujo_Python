from tkinter import Canvas, Tk, Frame, Button, messagebox, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab

linea_x = 0
linea_y= 0
color = "black"

def linea_xy(event):
	global linea_x, linea_y
	linea_x = event.x
	linea_y = event.y

def linea(event):
	global linea_x, linea_y
	canvas.create_line((linea_x, linea_y, event.x, event.y), fill=color, width = espesor_pincel.get())
	linea_x = event.x
	linea_y = event.y

def mostrar_color(nueva_color):
	global color
	color = nueva_color

def borrar():
	global color
	color = "White"

def limpiar():
	canvas.delete(ALL)

def salir():
	ventana.destroy()
	ventana.quit()

def guardar_dibujo():
	try:
		filename = filedialog.asksaveasfilename (defaultextension=".png")
		x = (ventana.winfo_rootx() +canvas.winfo_x())
		y = (ventana.winfo_rooty() + canvas.winfo_y())

		x1 = x + canvas.winfo_width()
		y1 = y + canvas.winfo_height()

		ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
		messagebox.showinfo("Guardar Dibujo", "Imagen guardada en: " + str(filename))

	except:
		messagebox.showerror("Guardar Dibujo", "Imagen no guardada\n Error")

ventana = Tk()
ventana.state("zoomed")
ventana.config(bg="black")
ventana.title( "PAINT en PYTHON")
#ventana.iconbitmap("icono_dibujo.ico")

ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

#frame principal comandos y Canvas de dibujo
frame = Frame(ventana, bg="white", height=200)
frame.grid(column=0, row=0, sticky="ew")
frame.columnconfigure(0, minsize=200, weight=1)

#Canvas de dibujo
canvas = Canvas(ventana, height=650, bg="white")
canvas.grid(row=1, column=0, sticky="nsew")
canvas.rowconfigure(0, weight=1)
canvas.columnconfigure(0, weight=1, minsize=100)
canvas.bind('<Button-1>', linea_xy)
canvas.bind('<B1-Motion>', linea)

# Canvas para colores
canvas_colores = Canvas(frame, bg="white", width=5, height=40)
canvas_colores.grid(column=0, row=0, sticky="ew", padx=1, pady=1)

id = canvas_colores.create_rectangle((10,10,30,30), fill="black")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("black"))

id = canvas_colores.create_rectangle((40,10,60,30), fill="blue")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("blue"))

id = canvas_colores.create_rectangle((70,10,90,30), fill = "red")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("red"))

id = canvas_colores.create_rectangle((100,10,120,30), fill="green")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("green"))

id = canvas_colores.create_rectangle((130,10,150,30), fill="yellow")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("yellow"))

id = canvas_colores.create_rectangle((160,10,180,30), fill="orange")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("orange"))

id = canvas_colores.create_rectangle((190,10,210,30), fill="sky blue")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("sky blue"))

id = canvas_colores.create_rectangle((220,10,240,30), fill="pink")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("pink"))

id = canvas_colores.create_rectangle((250,10,270,30), fill="gold")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("gold"))

id = canvas_colores.create_rectangle((280,10,300,30), fill="green2")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("green2"))

id = canvas_colores.create_rectangle((310,10,330,30), fill="silver")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("gray"))

id = canvas_colores.create_rectangle((340,10,360,30), fill="brown")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("red"))

id = canvas_colores.create_rectangle((370,10,390,30), fill="gray")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("gray"))

id = canvas_colores.create_rectangle((400,10,420,30), fill="purple")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("purple"))

id = canvas_colores.create_rectangle((430,10,450,30), fill="green2")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("green2"))

id = canvas_colores.create_rectangle((460,10,480,30), fill="dodger blue")
canvas_colores.tag_bind(id, "<Button-1>", lambda x: mostrar_color("dodger blue"))

#botones y control de grosor
color1 = "#3AB4F2"

espesor_pincel = Scale(frame, orient=HORIZONTAL, from_=1, to=100, length=150, relief="solid", bg=color1, width=17, sliderlength=20, highlightbackground="white", activebackground="#0078AA")
espesor_pincel.set(25)
espesor_pincel.grid(column=1, row=0, sticky="ew", pady=1, padx=2)

bt_guardar = Button(frame, text="Guardar", bg=color1, command = guardar_dibujo, width=10, height=2, activebackground="white", font=("Monserrat", 10, "bold"))
bt_guardar.grid(column=2, row=0, sticky="ew",pady=1,padx=4)

bt_borrar = Button (frame, text="Borrar", bg=color1, command = borrar, width=10, height=2, activebackground="white", font=("Monserrat",10, "bold"))
bt_borrar.grid(column=3, row=0, sticky="ew", pady=1, padx=4)

bt_limpiar = Button(frame, text="Limpiar", bg=color1, command = limpiar, width=10, height=2,activebackground="white", font=("Monserrat", 10, "bold"))
bt_limpiar.grid(column=4, row=0, sticky="ew", pady=1, padx=4)

bt_salir = Button(frame, text="Salir", bg=color1, command=salir, width=10, height=2, activebackground="white", font=("Monserrat",10,"bold"))
bt_salir.grid(column=5, row=0, sticky="ew",pady=1, padx=4)

ventana.mainloop()