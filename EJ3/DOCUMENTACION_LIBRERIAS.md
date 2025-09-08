# Documentación de Librerías - Ejercicio 3 Entropía

## Descripción del Ejercicio
Este ejercicio implementa una calculadora de entropía y redundancia para análisis de archivos. Utiliza conceptos de teoría de la información para medir la aleatoriedad y compresibilidad de diferentes tipos de archivos.

## Archivos del Ejercicio
- `Calc_Entropia.py` - Calculadora completa de entropía y redundancia

## Librerías Utilizadas

### 1. `os` (Librería Estándar de Python)
**Archivos donde se usa:** `Calc_Entropia.py`

**Propósito:**
- Interfaz para interactuar con el sistema operativo
- Operaciones de archivos y directorios

**Funciones específicas utilizadas:**
- `os.path.basename(path)` - Extrae el nombre del archivo de una ruta completa
- `os.path.splitext(filename)` - Separa el nombre del archivo de su extensión
- `os.listdir(directory)` - Lista archivos y directorios en un directorio
- `os.path.join(path1, path2)` - Une rutas de forma segura entre sistemas operativos
- `os.path.isfile(path)` - Verifica si la ruta corresponde a un archivo
- `os.path.exists(path)` - Verifica si un archivo o directorio existe

**Uso en el contexto:**
- Navegación y análisis de archivos en directorios
- Extracción de metadatos de archivos (nombre, extensión)
- Construcción de rutas de archivos de forma multiplataforma
- Validación de existencia de archivos antes del análisis

### 2. `math` (Librería Estándar de Python)
**Archivos donde se usa:** `Calc_Entropia.py`

**Propósito:**
- Funciones matemáticas básicas y avanzadas

**Funciones específicas utilizadas:**
- `math.log2(x)` - Logaritmo en base 2 (fundamental para cálculos de entropía)

**Uso en el contexto:**
- Cálculo de entropía usando la fórmula: H(X) = -Σ p(x) * log₂(p(x))
- Conversión de probabilidades a bits de información
- Cálculo de entropía condicional para análisis de dependencias

**Fórmula de entropía implementada:**
```
H(X) = -Σ p(xi) * log₂(p(xi))
```
Donde p(xi) es la probabilidad del símbolo xi.

### 3. `collections.Counter` (Librería Estándar de Python)
**Archivos donde se usa:** `Calc_Entropia.py`

**Propósito:**
- Contador de elementos en colecciones
- Herramienta especializada para conteo de frecuencias

**Funciones específicas utilizadas:**
- `Counter(iterable)` - Crea un contador de elementos
- `Counter.items()` - Acceso a elementos y sus frecuencias
- `Counter[element]` - Acceso directo a la frecuencia de un elemento

**Uso en el contexto:**
- Conteo de frecuencias de bytes en archivos
- Análisis de n-gramas para entropía dependiente
- Cálculo de probabilidades para cada símbolo
- Análisis de patrones en secuencias de datos

## Algoritmos Implementados

### 1. Entropía Independiente
**Descripción:** Calcula la entropía asumiendo que cada byte es independiente.

**Proceso:**
1. Contar frecuencia de cada byte (0-255)
2. Calcular probabilidad de cada byte
3. Aplicar fórmula de entropía: H = -Σ p(x) * log₂(p(x))
4. Calcular redundancia: R = 8 - H (para bytes de 8 bits)

### 2. Entropía Dependiente (Orden 1 y 2)
**Descripción:** Calcula entropía considerando dependencias entre símbolos consecutivos.

**Proceso:**
1. Crear n-gramas de orden especificado
2. Contar frecuencias de n-gramas
3. Para cada n-grama, analizar símbolos siguientes
4. Calcular entropía condicional
5. Promediar entropías condicionales ponderadas por probabilidad

### 3. Análisis de Archivos
**Tipos de archivo analizados:**
- `.txt` - Archivos de texto
- `.exe` - Ejecutables
- `.zip` - Archivos comprimidos
- `.pdf` - Documentos PDF
- `.jpg`, `.png` - Imágenes
- `.mp3`, `.mp4` - Multimedia
- `.doc`, `.xls` - Documentos de oficina
- `.bin`, `.bmp` - Archivos binarios

## Dependencias del Sistema
- **Python 3.x** - Versión mínima recomendada: 3.6+
- **Sistema operativo** - Compatible con Windows, Linux y macOS

## Instalación
Todas las librerías utilizadas son parte de la librería estándar de Python, por lo que **no se requiere instalación adicional**.

## Ejemplo de Uso
```python
# Ejecutar la calculadora de entropía
python Calc_Entropia.py
```

## Interpretación de Resultados

### Rangos de Entropía
- **< 4 bits**: Archivos muy compresibles (texto, patrones repetitivos)
- **4-6 bits**: Archivos moderadamente compresibles
- **> 6 bits**: Archivos difíciles de comprimir (datos aleatorios, encriptados)

### Análisis de Redundancia
- **Alta redundancia**: Mucha información repetitiva, fácil de comprimir
- **Baja redundancia**: Datos más aleatorios, difícil de comprimir

### Comparación Independiente vs Dependiente
- **Gran diferencia**: Mucha estructura y patrones en los datos
- **Poca diferencia**: Datos más aleatorios, menos estructura

## Características del Sistema

### Menú Interactivo
1. **Analizar archivo específico** - Análisis individual
2. **Analizar directorio** - Análisis masivo
3. **Mostrar resultados** - Vista tabular
4. **Generar reporte** - Análisis estadístico detallado
5. **Salir** - Terminar programa

### Reportes Generados
- **Estadísticas generales**: Total de archivos, tamaños, entropía promedio
- **Análisis por tipo**: Entropía promedio por extensión
- **Archivos extremos**: Mayor y menor entropía
- **Comparaciones**: Independiente vs dependiente
- **Interpretación**: Guías para entender los resultados

## Notas Técnicas
- La entropía máxima para bytes es 8 bits (datos completamente aleatorios)
- Los n-gramas permiten detectar patrones y dependencias
- El análisis de orden 2 considera dependencias de 2 símbolos consecutivos
- Los resultados ayudan a predecir la compresibilidad de archivos


