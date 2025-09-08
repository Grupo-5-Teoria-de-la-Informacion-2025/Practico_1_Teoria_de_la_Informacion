import os
import math
from collections import Counter


#Clase para calcular entropía y redundancia de archivos 
class CalculadoraEntropia:
    
    def __init__(self):
        self.resultados = {}
    
    #Calcula la entropía considerando símbolos independientes
    def calcular_entropia_independiente(self, datos):
        
        if not datos:
            return 0, 0
        
        # Contar frecuencias de cada byte
        frecuencias = Counter(datos)
        total_bytes = len(datos)
        
        # Calcular probabilidades y entropía
        entropia = 0
        for byte, frecuencia in frecuencias.items():
            probabilidad = frecuencia / total_bytes
            if probabilidad > 0:
                entropia -= probabilidad * math.log2(probabilidad)
        
        # Calcular redundancia (entropía máxima - entropía actual)
        entropia_maxima = 8  # Para bytes (8 bits)
        redundancia = entropia_maxima - entropia
        
        return entropia, redundancia


    #Calcula la entropía considerando dependencias entre símbolos
    def calcular_entropia_dependiente(self, datos, orden=1):
        
        if len(datos) < orden + 1:
            return 0, 0
        
        # Crear contexto de n-gramas
        ngramas = []
        for i in range(len(datos) - orden):
            ngrama = tuple(datos[i:i+orden])
            ngramas.append(ngrama)
        
        # Contar frecuencias de n-gramas
        frecuencias_ngramas = Counter(ngramas)
        total_ngramas = len(ngramas)
        
        # Calcular entropía condicional
        entropia_condicional = 0
        for ngrama, frecuencia in frecuencias_ngramas.items():
            probabilidad_ngrama = frecuencia / total_ngramas
            
            # Contar símbolos que siguen a este n-grama
            simbolos_siguientes = []
            for i in range(len(datos) - orden):
                if tuple(datos[i:i+orden]) == ngrama:
                    if i + orden < len(datos):
                        simbolos_siguientes.append(datos[i + orden])
            
            if simbolos_siguientes:
                frecuencias_siguientes = Counter(simbolos_siguientes)
                entropia_parcial = 0
                for simbolo, freq in frecuencias_siguientes.items():
                    prob_condicional = freq / len(simbolos_siguientes)
                    if prob_condicional > 0:
                        entropia_parcial -= prob_condicional * math.log2(prob_condicional)
                
                entropia_condicional += probabilidad_ngrama * entropia_parcial
        
        # Calcular redundancia
        entropia_maxima = 8
        redundancia = entropia_maxima - entropia_condicional
        
        return entropia_condicional, redundancia
    
    #Analiza un archivo y calcula entropía y redundancia
    def analizar_archivo(self, ruta_archivo):
        

        try:
            with open(ruta_archivo, 'rb') as f:
                datos = f.read()
            
            # Obtener información del archivo
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1].lower()
            tamaño = len(datos)
            
            # Calcular entropía independiente
            entropia_indep, redundancia_indep = self.calcular_entropia_independiente(datos)
            
            # Calcular entropía dependiente (orden 1)
            entropia_dep1, redundancia_dep1 = self.calcular_entropia_dependiente(datos, 1)
            
            # Calcular entropía dependiente (orden 2)
            entropia_dep2, redundancia_dep2 = self.calcular_entropia_dependiente(datos, 2)
            
            resultado = {
                'nombre': nombre,
                'extension': extension,
                'tamaño': tamaño,
                'entropia_independiente': entropia_indep,
                'redundancia_independiente': redundancia_indep,
                'entropia_dependiente_1': entropia_dep1,
                'redundancia_dependiente_1': redundancia_dep1,
                'entropia_dependiente_2': entropia_dep2,
                'redundancia_dependiente_2': redundancia_dep2
            }
            
            return resultado
            
        except Exception as e:
            print(f"Error al analizar {ruta_archivo}: {str(e)}")
            return None
    
    #Analiza todos los archivos en un directorio
    def analizar_directorio(self, directorio="."):
        
        extensiones_interesantes = ['.txt', '.exe', '.zip', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.doc', '.xls', '.bin', '.bmp']
        
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_completa):
                extension = os.path.splitext(archivo)[1].lower()
                if extension in extensiones_interesantes:
                    print(f"Analizando: {archivo}")
                    resultado = self.analizar_archivo(ruta_completa)
                    if resultado:
                        self.resultados[archivo] = resultado
    
    #Muestra los resultados de forma tabular
    def mostrar_resultados(self):
        

        if not self.resultados:
            print("No hay resultados para mostrar.")
            return
        
        print("\n" + "="*120)
        print("RESULTADOS DE ANÁLISIS DE ENTROPÍA Y REDUNDANCIA")
        print("="*120)
        print(f"{'Archivo':<20} {'Ext':<6} {'Tamaño':<10} {'Ent.Indep':<10} {'Red.Indep':<10} {'Ent.Dep1':<10} {'Red.Dep1':<10} {'Ent.Dep2':<10} {'Red.Dep2':<10}")
        print("-"*120)
        
        for nombre, datos in self.resultados.items():
            print(f"{nombre:<20} {datos['extension']:<6} {datos['tamaño']:<10} "
                  f"{datos['entropia_independiente']:<10.3f} {datos['redundancia_independiente']:<10.3f} "
                  f"{datos['entropia_dependiente_1']:<10.3f} {datos['redundancia_dependiente_1']:<10.3f} "
                  f"{datos['entropia_dependiente_2']:<10.3f} {datos['redundancia_dependiente_2']:<10.3f}")
   
    #Genera un reporte detallado
    def generar_reporte(self):
        if not self.resultados:
            print("No hay datos para generar reporte.")
            return
        
        print("\n" + "="*80)
        print("REPORTE DETALLADO DE ANÁLISIS DE ENTROPÍA")
        print("="*80)
        
        # Estadísticas generales
        total_archivos = len(self.resultados)
        tamanos = [datos['tamaño'] for datos in self.resultados.values()]
        entropias_indep = [datos['entropia_independiente'] for datos in self.resultados.values()]
        
        print(f"\nESTADÍSTICAS GENERALES:")
        print(f"Total de archivos analizados: {total_archivos}")
        print(f"Tamaño total: {sum(tamanos):,} bytes")
        print(f"Tamaño promedio: {sum(tamanos)/len(tamanos):,.0f} bytes")
        print(f"Entropía independiente promedio: {sum(entropias_indep)/len(entropias_indep):.3f} bits")
        
        # Análisis por tipo de archivo
        extensiones = {}
        for datos in self.resultados.values():
            ext = datos['extension']
            if ext not in extensiones:
                extensiones[ext] = []
            extensiones[ext].append(datos['entropia_independiente'])
        
        print(f"\nANÁLISIS POR TIPO DE ARCHIVO:")
        for ext, entropias in extensiones.items():
            promedio = sum(entropias) / len(entropias)
            print(f"{ext}: {len(entropias)} archivos, entropía promedio: {promedio:.3f} bits")
        
        # Archivos con mayor y menor entropía
        archivo_max_entropia = max(self.resultados.items(), 
                                 key=lambda x: x[1]['entropia_independiente'])
        archivo_min_entropia = min(self.resultados.items(), 
                                 key=lambda x: x[1]['entropia_independiente'])
        
        print(f"\nARCHIVOS EXTREMOS:")
        print(f"Mayor entropía: {archivo_max_entropia[0]} ({archivo_max_entropia[1]['entropia_independiente']:.3f} bits)")
        print(f"Menor entropía: {archivo_min_entropia[0]} ({archivo_min_entropia[1]['entropia_independiente']:.3f} bits)")
        
        # Comparación entre entropía independiente y dependiente
        diferencias = []
        for datos in self.resultados.values():
            diff = datos['entropia_independiente'] - datos['entropia_dependiente_1']
            diferencias.append(diff)
        
        print(f"\nCOMPARACIÓN ENTROPÍA INDEPENDIENTE vs DEPENDIENTE:")
        print(f"Diferencia promedio: {sum(diferencias)/len(diferencias):.3f} bits")
        print(f"Archivos con mayor diferencia: {sum(1 for d in diferencias if d > 1)}")
        print(f"Archivos con menor diferencia: {sum(1 for d in diferencias if d < 0.5)}")
        
        # Interpretación de resultados
        print(f"\nINTERPRETACIÓN:")
        print(f"• Archivos con entropía < 4 bits: Muy compresibles (texto, patrones repetitivos)")
        print(f"• Archivos con entropía > 6 bits: Difícil de comprimir (datos aleatorios, encriptados)")
        print(f"• Diferencia alta entre independiente y dependiente: Mucha estructura y patrones")
        print(f"• Diferencia baja: Datos más aleatorios")

#Función principal de la aplicación
if __name__ == "__main__":
    
    
    print("CALCULADORA DE ENTROPÍA Y REDUNDANCIA ")
    print("="*60)
    
    calc = CalculadoraEntropia()
    
    #Definimos un menu para la aplicación

    print("\nOpciones:")
    print("1. Analizar archivo específico")
    print("2. Analizar todos los archivos del directorio actual")
    print("3. Mostrar resultados")
    print("4. Generar reporte detallado")
    print("5. Salir")

    opcion = input("\nSeleccione una opción (1-5): ").strip()

    while opcion != "5":
        #Evaluamos la opción seleccionada y realizamos las acciones correspondientes
        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo: ").strip()
            if os.path.exists(archivo):
                print(f"Analizando: {archivo}")
                resultado = calc.analizar_archivo(archivo)
                if resultado:
                    calc.resultados[archivo] = resultado
                    print("✓ Análisis completado")
            else:
                print("✗ Archivo no encontrado")
        
        elif opcion == "2":
            print("Analizando archivos del directorio actual...")
            calc.analizar_directorio()
            print(f"✓ Se analizaron {len(calc.resultados)} archivos")
        
        elif opcion == "3":
            calc.mostrar_resultados()
        
        elif opcion == "4":
            calc.generar_reporte()
        
        else:
            print("Opción no válida. Intente de nuevo. \n")
            
        #Definimos el menu de opciones nuevamente para que el usuario pueda seleccionar una nueva opción o salir
        print("\nOpciones:")
        print("1. Analizar archivo específico")
        print("2. Analizar todos los archivos del directorio actual")
        print("3. Mostrar resultados")
        print("4. Generar reporte detallado")
        print("5. Salir")
        opcion = input("\nSeleccione una opción (1-5): ").strip()

