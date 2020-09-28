#-------------------------------------------- SCRIPT DESCRIPTION --------------------------------------------------#
# Lifestore Project EMTECH
# Created by: Mario Sepulveda
# Created on: 2020-09-27 12:38:10
#------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- Python Library ---------------------------------------------------#
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
from lifestore_file import lifestore_searches
import tkinter
from tkinter import *
from tkinter import messagebox
#------------------------------------------------------------------------------------------------------------------#
def menu_screen():
	global pantalla
	pantalla=Tk()
	pantalla.geometry("500x300")
	pantalla.title("Welcome to LifeStore")
	pantalla.iconbitmap("lifestore.ico")

	image=PhotoImage(file="lifestore.gif")
	image=image.subsample(2,2)
	label=Label(image=image)
	label.pack()

	Label(text="Welcome! To continue please click in Log In Button", bg="red", fg="white", width="300", height="3", font=("Sancoale", 12)).pack()
	Label(text="").pack()

	Button(text="Log In", height="3", width="35", font=("Sancoale",12), command=inicio_sesion).pack()

	pantalla.mainloop()

def inicio_sesion():
	global pantalla1
	pantalla1 = Toplevel(pantalla)
	pantalla1.geometry("400x250")
	pantalla1.title("Log In")
	pantalla1.iconbitmap("lifestore.ico")

	Label(pantalla1, text="Please enter your credentials", bg="navy", fg="white", width="300", height="3", font=("Sancoale", 12)).pack()
	Label(pantalla1, text="").pack()

	global username_verify
	global password_verify

	username_verify=StringVar()
	password_verify=StringVar()

	global username_entry
	global password_entry


	Label(pantalla1, text="Username").pack()
	username_entry = Entry(pantalla1, textvariable=username_verify)
	username_entry.pack()
	Label(pantalla1).pack()

	Label(pantalla1, text="Password").pack()
	password_entry = Entry(pantalla1, textvariable=password_verify, show="*")
	password_entry.pack()
	Label(pantalla1).pack()

	Button(pantalla1, text="Log In", command=log_in).pack()
	# pantalla.mainloop()

def log_in():
	admin_user = ["123", "123"]
	if username_verify.get() == "" and password_verify.get() == "":
		messagebox.showerror(title="Security Verfication", message="Please insert ypur credentials")
	else: 
		if admin_user[0] == username_verify.get() and admin_user[1] == password_verify.get():
			messagebox.showinfo(title="Security Verfication", message="Logged In Successfully")
			general_view()
		else:
			messagebox.showerror(title="Security Verfication", message="Invalid Credentials")


def general_view():
	global pantalla2
	pantalla2 = Toplevel(pantalla1)
	pantalla2.geometry("700x450")
	pantalla2.title("Invetory and General Information -- LifeStore.")
	pantalla2.iconbitmap("lifestore.ico")
	Label(pantalla2, text="Inventory and General Information", bg="orange", fg="white", width="250", height="1", font=("Sancoale", 12)).pack()

	prod_top = tkinter.Button(pantalla2, text="50 top-selling products", bg="purple", fg="white", font=("Sancoale", 12), command=prod_top_project).place(x=15, y=50)

	prod_search = tkinter.Button(pantalla2, text="100 top-searching products", bg="brown", fg="white", font=("Sancoale", 12), command=prod_search_project).place(x=15, y=90)

	category_prod = tkinter.Button(pantalla2, text="50 bottom-selling products", bg="yellow", fg="black", font=("Sancoale", 12), command=category_prod_project).place(x=15, y=130)

	best_review = tkinter.Button(pantalla2, text="20 top-review products", bg="green", fg="white", font=("Sancoale", 12),  command=best_review_project).place(x=15, y=170) 

	bottom_review = tkinter.Button(pantalla2, text="20 bottom-review products", bg="blue", fg="white", font=("Sancoale", 12), command=bottom_review_project).place(x=15, y=210) 

	total_ingresos = tkinter.Button(pantalla2, text="Total Revenue", bg="red", fg="white", font=("Sancoale", 12)).place(x=15, y=250)

	average_sales = tkinter.Button(pantalla2, text="Monthly Average Sales", bg="black", fg="white", font=("Sancoale", 12)).place(x=15, y=290)

	anual_Sales = tkinter.Button(pantalla2, text="Total Anual Sales", bg="gold", fg="white", font=("Sancoale", 12)).place(x=15, y=330)

	best_moths = tkinter.Button(pantalla2, text="Best Months", bg="cyan", fg="white", font=("Sancoale", 12)).place(x=15, y=370)


def prod_top_project():
	count = 0
	total_ventas = []

	for prod_index in lifestore_products:
		# print(prod_index[0],prod_index[1])
		for venta in lifestore_sales:
			if prod_index[0] == venta[1]:
				count += 1
		format_f = [prod_index[1], count]
		total_ventas.append(format_f)
		count = 0
	# print(list(total_ventas))
	ordenados = []
	while total_ventas:
		min_var = total_ventas[0][1]
		actual = total_ventas[0]
		for test in total_ventas:
			if test[1] > min_var:
				min_var = test[1]
				actual = test
		ordenados.append(actual)
		total_ventas.remove(actual)
	# print(ordenados)
	for total in ordenados[0:50]:
		print('\nThe product: \n', total[0], ' was sold: ', total[1])

def prod_search_project():
	count = 0
	total_searches = []

	for prod_index in lifestore_products:
		# print(prod_index[0],prod_index[1])
		for search in lifestore_searches:
			if prod_index[0] == search[1]:
				count += 1
		format_f = [prod_index[1], count]
		total_searches.append(format_f)
		count = 0
	# print(list(total_ventas))

	ordenados = []
	while total_searches:
		min_var = total_searches[0][1]
		actual = total_searches[0]
		for test in total_searches:
			if test[1] > min_var:
				min_var = test[1]
				actual = test
		ordenados.append(actual)
		total_searches.remove(actual)
	# print(ordenados)


	for total in ordenados[0:100]:
		print('\nThe product: \n', total[0], ' was searched: ', total[1])

def category_prod_project():
	count = 0
	total_ventas = []

	for prod_index in lifestore_products:
		# print(prod_index[0],prod_index[1])
		for venta in lifestore_sales:
			if prod_index[0] == venta[1]:
				count += 1
		format_f = [prod_index[3],prod_index[1], count]
		total_ventas.append(format_f)
		count = 0
	# print(list(total_ventas))

	ordenados = []
	while total_ventas:
		min_var = total_ventas[0][2]
		actual = total_ventas[0]
		for test in total_ventas:
			if test[2] > min_var:
				min_var = test[2]
				actual = test
		ordenados.append(actual)
		total_ventas.remove(actual)
	# print(ordenados)

	ident_t = 0
	for total in ordenados[0:-50]:
		ident_t += 1
		print(ident_t,'\nCategory: \n', total[0],'\n Products: \n',total[1], ' was sold: ', total[2])

def best_review_project():
	count = 0
	total_ventas = []

	for prod_index in lifestore_products:
		# print(prod_index[0],prod_index[1])
		for venta in lifestore_sales:
			if prod_index[0] == venta[1] and venta[2] >= 4:
				count += 1
		format_f = [prod_index[1], count]
		total_ventas.append(format_f)
		count = 0

	# print(list(total_ventas))

	ordenados = []
	while total_ventas:
		min_var = total_ventas[0][1]
		actual = total_ventas[0]
		for test in total_ventas:
			if test[1] > min_var:
				min_var = test[1]
				actual = test
		ordenados.append(actual)
		total_ventas.remove(actual)
	# print(ordenados)

	ident = 0
	for total in ordenados[0:20]:
		ident += 1 
		print(ident, '\nThe product: \n', total[0], ' was evaluated equal or greather than 4')



def bottom_review_project():
	count = 0
	total_ventas = []

	for prod_index in lifestore_products:
		# print(prod_index[0],prod_index[1])
		for venta in lifestore_sales:
			if prod_index[0] == venta[1] and venta[2] <= 3:
				count += 1
		format_f = [prod_index[1], count]
		total_ventas.append(format_f)
		count = 0

	# print(list(total_ventas))

	ordenados = []
	while total_ventas:
		min_var = total_ventas[0][1]
		actual = total_ventas[0]
		for test in total_ventas:
			if test[1] > min_var:
				min_var = test[1]
				actual = test
		ordenados.append(actual)
		total_ventas.remove(actual)
	# print(ordenados)

	ident = 0
	for total in ordenados[0:20]:
		ident += 1 
		print(ident, '\nThe product: \n', total[0], ' was evaluated equal or lower than 3 ')
menu_screen()




