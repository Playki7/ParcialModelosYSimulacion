import tkinter as tk
from tkinter import ttk

def calcular_remuneracion():
    pregrado = pregrado_var.get()
    especializacion = especializacion_entry.get()
    especializacion_1_anos = int(especializacion_1_anos_entry.get())
    especializacion_2_anos = int(especializacion_2_anos_entry.get())
    magister_cantidad = int(magister_cantidad_entry.get())
    doctorado_cantidad = int(doctorado_cantidad_entry.get())
    anos_investigacion = int(anos_investigacion_entry.get())
    meses_investigacion = int(meses_investigacion_entry.get())
    dias_investigacion = int(dias_investigacion_entry.get())
    anos_docencia = int(anos_docencia_entry.get())
    meses_docencia = int(meses_docencia_entry.get())
    dias_docencia = int(dias_docencia_entry.get())
    anos_direccion = int(anos_direccion_entry.get())
    meses_direccion = int(meses_direccion_entry.get())
    dias_direccion = int(dias_direccion_entry.get())
    anos_experiencia = int(anos_experiencia_entry.get())
    meses_experiencia = int(meses_experiencia_entry.get())
    dias_experiencia = int(dias_experiencia_entry.get())
    regimen = regimen_var.get()
    anos_universidad = int(anos_universidad_entry.get())
    meses_universidad = int(meses_universidad_entry.get())
    dias_universidad = int(dias_universidad_entry.get())
    escalafon = escalafon_var.get()
    

def mostrar_cajas_texto(event):
    num_articulos = int(num_articulos_combobox.get())
    for widget in cajas_texto:
        widget.destroy()
    cajas_texto.clear()
    for i in range(num_articulos):
        caja_texto = ttk.Entry(cajas_frame)
        caja_texto.grid(row=i, column=0, sticky="we", pady=2)
        cajas_texto.append(caja_texto)


    print("La remuneración mensual es: XXXX")

root = tk.Tk()
root.title("Remuneración Mensual de Docentes")
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Agregar barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear un marco dentro del lienzo para colocar todos los widgets
main_frame = ttk.Frame(canvas)
canvas.create_window((0,0), window=main_frame, anchor="nw")



pregrado_label = ttk.Label(main_frame, text="Tipo de Pregrado:")
pregrado_label.grid(row=0, column=0, sticky="w")
pregrado_var = tk.StringVar()
pregrado_combobox = ttk.Combobox(main_frame, textvariable=pregrado_var, values=["Normal", "Medicina Humana", "Composición Musical"])
pregrado_combobox.grid(row=0, column=1)

posgrado_label = ttk.Label(main_frame, text="Posgrado:")
posgrado_label.grid(row=1, column=0, sticky="w")


especializacion_1_anos_label = ttk.Label(main_frame, text="Años de Especialización 1:")
especializacion_1_anos_label.grid(row=2, column=0, sticky="w")
especializacion_1_anos_entry = ttk.Entry(main_frame)
especializacion_1_anos_entry.grid(row=2, column=1)

especializacion_2_anos_label = ttk.Label(main_frame, text="Años de Especialización 2:")
especializacion_2_anos_label.grid(row=3, column=0, sticky="w")
especializacion_2_anos_entry = ttk.Entry(main_frame)
especializacion_2_anos_entry.grid(row=3, column=1)

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=4, column=0)

magister_cantidad_label = ttk.Label(main_frame, text="Cantidad de Magíster:")
magister_cantidad_label.grid(row=5, column=0, sticky="w")
magister_cantidad_entry = ttk.Entry(main_frame)
magister_cantidad_entry.grid(row=5, column=1)

doctorado_cantidad_label = ttk.Label(main_frame, text="Cantidad de Doctorado:")
doctorado_cantidad_label.grid(row=6, column=0, sticky="w")
doctorado_cantidad_entry = ttk.Entry(main_frame)
doctorado_cantidad_entry.grid(row=6, column=1)

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=7, column=0)


num_articulos_label = ttk.Label(main_frame, text="Artículos A1:")
num_articulos_label.grid(row=8, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=8, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=9, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Artículos A2:")
num_articulos_label.grid(row=10, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=10, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=11, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Artículos B:")
num_articulos_label.grid(row=12, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=12, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=13, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Artículos C:")
num_articulos_label.grid(row=14, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=14, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=15, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=16, column=0)

num_articulos_label = ttk.Label(main_frame, text="Artículos Cortos A1:")
num_articulos_label.grid(row=17, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=17, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=18, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Artículos Cortos A2:")
num_articulos_label.grid(row=19, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=19, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=20, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Artículos Cortos B:")
num_articulos_label.grid(row=21, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=21, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=22, column=0, columnspan=2, pady=5)

cajas_texto = []


num_articulos_label = ttk.Label(main_frame, text="Artículos Cortos C:")
num_articulos_label.grid(row=23, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=23, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=24, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=25, column=0)


num_articulos_label = ttk.Label(main_frame, text="Otras Formas A1:")
num_articulos_label.grid(row=26, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=26, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=27, column=0, columnspan=2, pady=5)

cajas_texto = []


num_articulos_label = ttk.Label(main_frame, text="Otras Formas A2:")
num_articulos_label.grid(row=28, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=28, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=29, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Otras Formas B:")
num_articulos_label.grid(row=30, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=30, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=31, column=0, columnspan=2, pady=5)

cajas_texto = []


num_articulos_label = ttk.Label(main_frame, text="Otras Formas C:")
num_articulos_label.grid(row=32, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=32, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=33, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=34, column=0)

num_articulos_label = ttk.Label(main_frame, text="Videos Internacionales:")
num_articulos_label.grid(row=35, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=35, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=36, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Videos Nacionales:")
num_articulos_label.grid(row=36, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=36, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=37, column=0, columnspan=2, pady=5)

cajas_texto = []


num_articulos_label = ttk.Label(main_frame, text="Videos Documentales Internacionales:")
num_articulos_label.grid(row=38, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=38, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=39, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Videos Documentales Nacionales:")
num_articulos_label.grid(row=40, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=40, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=41, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=42, column=0)

num_articulos_label = ttk.Label(main_frame, text="Libros Investigativos:")
num_articulos_label.grid(row=43, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=43, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=44, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Libros de Texto:")
num_articulos_label.grid(row=45, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=45, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=46, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Libros Ensayo:")
num_articulos_label.grid(row=47, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=47, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=48, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Patentes:")
num_articulos_label.grid(row=49, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=49, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=50, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Traduciones de Libros:")
num_articulos_label.grid(row=51, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=51, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=52, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=53, column=0)

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Originales Internacioneles:")
num_articulos_label.grid(row=54, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=54, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=55, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Originales Nacioneles:")
num_articulos_label.grid(row=56, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=56, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=57, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Complementaria Internacioneles:")
num_articulos_label.grid(row=58, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=58, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=59, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Complementarias Nacioneles:")
num_articulos_label.grid(row=60, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=60, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=61, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Interpretadas Nacioneles:")
num_articulos_label.grid(row=62, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=62, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=63, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Obras Artisitcas Interpretadas Internacioneles:")
num_articulos_label.grid(row=64, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=64, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=65, column=0, columnspan=2, pady=5)

cajas_texto = []


blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=66, column=0)

num_articulos_label = ttk.Label(main_frame, text="Innovacion Tecnologica:")
num_articulos_label.grid(row=67, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=67, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=68, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Adaptacion Tecnologica:")
num_articulos_label.grid(row=69, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=69, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=70, column=0, columnspan=2, pady=5)

cajas_texto = []

num_articulos_label = ttk.Label(main_frame, text="Produccion de software:")
num_articulos_label.grid(row=71, column=0, sticky="w")
num_articulos_combobox = ttk.Combobox(main_frame, values=list(range(1, 11)))
num_articulos_combobox.grid(row=71, column=1)
num_articulos_combobox.bind("<<ComboboxSelected>>", mostrar_cajas_texto)


cajas_frame = ttk.Frame(main_frame)
cajas_frame.grid(row=72, column=0, columnspan=2, pady=5)

cajas_texto = []

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=73, column=0)

anos_investigacion_label = ttk.Label(main_frame, text="Años de Investigación:")
anos_investigacion_label.grid(row=74, column=0, sticky="w")
anos_investigacion_entry = ttk.Entry(main_frame)
anos_investigacion_entry.grid(row=74, column=1)

meses_investigacion_label = ttk.Label(main_frame, text="Meses de Investigación:")
meses_investigacion_label.grid(row=75, column=0, sticky="w")
meses_investigacion_entry = ttk.Entry(main_frame)
meses_investigacion_entry.grid(row=75, column=1)

dias_investigacion_label = ttk.Label(main_frame, text="Días de Investigación:")
dias_investigacion_label.grid(row=76, column=0, sticky="w")
dias_investigacion_entry = ttk.Entry(main_frame)
dias_investigacion_entry.grid(row=76, column=1)


blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=77, column=0)


anos_docencia_label = ttk.Label(main_frame, text="Años de Docencia:")
anos_docencia_label.grid(row=78, column=0, sticky="w")
anos_docencia_entry = ttk.Entry(main_frame)
anos_docencia_entry.grid(row=78, column=1)

anos_docencia_label = ttk.Label(main_frame, text="Meses de Docencia:")
anos_docencia_label.grid(row=79, column=0, sticky="w")
anos_docencia_entry = ttk.Entry(main_frame)
anos_docencia_entry.grid(row=79, column=1)

anos_docencia_label = ttk.Label(main_frame, text="Dias de Docencia:")
anos_docencia_label.grid(row=80, column=0, sticky="w")
anos_docencia_entry = ttk.Entry(main_frame)
anos_docencia_entry.grid(row=80, column=1)

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=81, column=0)

anos_direccion_label = ttk.Label(main_frame, text="Años de Direción:")
anos_direccion_label.grid(row=82, column=0, sticky="w")
anos_direccion_entry = ttk.Entry(main_frame)
anos_direccion_entry.grid(row=82, column=1)

meses_direccion_label = ttk.Label(main_frame, text="Meses de Direción:")
meses_direccion_label.grid(row=83, column=0, sticky="w")
meses_direccion_entry = ttk.Entry(main_frame)
meses_direccion_entry.grid(row=83, column=1)

dias_direccion_label = ttk.Label(main_frame, text="Dias de Direción:")
dias_direccion_label.grid(row=84, column=0, sticky="w")
dias_direccion_entry = ttk.Entry(main_frame)
dias_direccion_entry.grid(row=84, column=1)

blank_space_label2 = ttk.Label(main_frame, text="")
blank_space_label2.grid(row=85, column=0)

anos_Experiencia_label = ttk.Label(main_frame, text="Años de Experiencia:")
anos_Experiencia_label.grid(row=86, column=0, sticky="w")
anos_Experiencia_entry = ttk.Entry(main_frame)
anos_Experiencia_entry.grid(row=86, column=1)

meses_Experiencia_label = ttk.Label(main_frame, text="Meses de Experiencia:")
meses_Experiencia_label.grid(row=87, column=0, sticky="w")
meses_Experiencia_entry = ttk.Entry(main_frame)
meses_Experiencia_entry.grid(row=87, column=1)

dias_Experiencia_label = ttk.Label(main_frame, text="Dias de Experiencia:")
dias_Experiencia_label.grid(row=88, column=0, sticky="w")
dias_Experiencia_entry = ttk.Entry(main_frame)
dias_Experiencia_entry.grid(row=88, column=1)




calcular_button = ttk.Button(main_frame, text="Calcular Remuneración", command=calcular_remuneracion)
calcular_button.grid(row=89, columnspan=2)


regimen_label = ttk.Label(main_frame, text="Régimen:")
regimen_label.grid(row=90, column=0, sticky="w")
regimen_var = tk.StringVar()
regimen_combobox = ttk.Combobox(main_frame, textvariable=regimen_var, values=["Nuevo", "Del 1444", "Otro"])
regimen_combobox.grid(row=90, column=1)


escalafon_label = ttk.Label(main_frame, text="Escalafón Docente:")
escalafon_label.grid(row=91, column=0, sticky="w")
escalafon_var = tk.StringVar()
escalafon_combobox = ttk.Combobox(main_frame, textvariable=escalafon_var, values=["Instructor", "Profesor Auxiliar", "Instructor Asistente", "Profesor Asistente", "Profesor Asociado", "Profesor Titular"])
escalafon_combobox.grid(row=92, column=1)


root.mainloop()
