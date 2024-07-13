import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("C:/Users/madri/Downloads/base_datos_semilleros_comunicaciones.xlsx")

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Ruta del archivo de texto que quieres crear
    nombresemillero = row['Semillero de Investigación']  # Cambia 'A' por el nombre de tu columna
    nombresemillero.replace("/", "")
    escuela = row['Escuela']
    Programa = row['Programa']
    areaConocimiento = row['Área del conocimiento grupo Minciencias']
    docente = row['Docente coordinador ']
    emailDocente = row['E-mail']
    estudiante = row['Estudiante coordinador']
    emailEstudiante = row["E-mailEstudiante"]
    lineasInvestigacion = row["Lineas de investigación "]
    redes = row["Redes Sociales  "]
    descSemillero = row["Este Semillero Es Para Ti Si"]
    logros = row["Logros Más Grandes "]
    notas = row["Nota/ Observación"]


    ruta_archivo = "C:/Users/madri/Desktop/constructorSemilleros/Semilleros/" + nombresemillero + ".txt"


    # Acceder a los valores de las columnas de la fila actual

# Abrir el archivo en modo escritura ('w')
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        # Escribir algunas líneas en el archivo
        archivo.write("-------------------- titulo -----------------------\n")
        archivo.write(f"""<div class="row">
   <div class="col-sm-12 col-lg-2">​​​​​​​​ 
      <br/></div>
   <div class="col-sm-12 col-lg-8">
      <p>
      </p>
      <h1 class="ed-rteElement-H1">{nombresemillero}&#160;​<br/></h1>
      <p class="ed-rteElement-P"> 
         <br/> 
      </p>
   </div>
   <div class="col-sm-12 col-lg-2"> 
      <br/> 
      <br/> 
      <br/> 
   </div>
</div>​​<br/>""")
        archivo.write("\n-------------------- Zona gris -----------------------\n")
        archivo.write(f"""<div class="row">
   <div class="col-sm-12 col-lg-2"> 
      <br/> 
   </div>
   <div class="col-sm-12 col-lg-8">
      <div class="row">
         <div class="col-sm-12 col-lg-6">
            <p class="ed-rteElement-P"> 
               <strong>Nombre:</strong><br/>{nombresemillero}<br/><strong>Escuela: </strong>{escuela}<br/><strong>Programa: </strong>{Programa}&#160;​​<br/><strong>Área del conocimiento: </strong>​{areaConocimiento}&#160;​<br/></p>
         </div>
         <div class="col-sm-12 col-lg-6">
            <p class="ed-rteElement-P"> ​ 
               <strong>Docente Coordinador​: &#160;<br/></strong>{docente}<br/><strong>Contacto:&#160;<a href="mailto:{emailDocente}" target="_blank">{emailDocente}</a>​</strong>​<br/>​​​​<br/><strong>Estudiante coordinador: &#160;<br/></strong>{estudiante}<br/><strong>​​​Contacto:&#160;<a href="mailto:{emailEstudiante}" target="_blank">{emailEstudiante}​​​</a>​</strong>​<br/>​​​​​<br/> </p>
         </div>
      </div>
   </div>
   <div class="col-sm-12 col-lg-2"> 
      <br/> ​<br/>​<br/></div>
</div>

<div class="row">
   <div class="col-sm-12 col-lg-2"> 
      <br/> 
   </div>
   <div class="col-sm-12 col-lg-8">​ 

      {redes}
      <div class="col-sm-12 col-lg-6">
         <strong>Red social 1: &#160;</strong>UserName </div>
      <div class="col-sm-12 col-lg-6">
         <strong>Red social 2: &#160;​</strong> UserName​ </div>
   </div>
   <div class="col-sm-12 col-lg-2"> 
      <br/> 
   </div>
</div>
<br/>​<br/><br/> ​<br/>""")
        archivo.write("\n--------------------  Cuerpo -----------------------\n")
        archivo.write(f""" <div class="row">
   <div class="col-sm-12 col-lg-2">
      <br/>
   </div>
   <div class="col-sm-12 col-lg-8">
      <h3>El semillero<br/></h3>
      
      <!-- Descripcion del semillero -->
                      
      <h3>Lineas de investiga​ción&#160;</h3>
                      
      {lineasInvestigacion}
    
      <h3>Este Semillero es para ti si...<br/></h3>
      
      {descSemillero}
      
      <h3>Logros del semi​​llero</h3>
                      
      {logros}

   </div>​ 
   <div class="col-sm-12 col-lg-2">
      <br/>
   </div>
</div> 
<br/>
<br/>
                      
                      """)
        archivo.write("\n--------------------  Notas -----------------------\n")
        archivo.write(f"{notas}")

    print(f"{ruta_archivo}")
    
    # Realizar alguna operación con los datos de la fila

    # Ejemplo de operación: sumar los valores de las columnas A, B y C

