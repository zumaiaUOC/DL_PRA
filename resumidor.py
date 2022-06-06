#!/usr/bin/env python
# coding: utf-8

# # Summarizer with Python and NLTK (Resumidor con Python y NLTK)

# In[1]:


# Importa los metodos a trabajar desde NLTK:

# stopwords = palabras reservadas.
from nltk.corpus import stopwords

# word_tokenize = valorizador de palabras.
# sent_tokenize = valorizador de oraciones.
from nltk.tokenize import word_tokenize, sent_tokenize


# In[2]:


# Descarga de metodos debido a que stopwords y tokenize
#   no se podían usar sin ellos.
import nltk
nltk.download('stopwords')
nltk.download('punkt')


# In[3]:


# Se crean 2 arreglos y 1 variable:

# arreglo 1) - SW - configura el método de entrada o idioma en el que se 
                    # van a trabajar las palabras en el metodo words de stopwords, en este caso, Español.
SW = set(stopwords.words("spanish"))

# text para definir el texto a resumir.

text = input("Introduce el texto : \n")

'''
text = """El secreto de Edgar Allan Poe es la previa organización metódica de sus elementos a fin de producir efectos. Haciendo una lectura tamizada de la obra, se develan aquellos elementos patrones que, casualmente, emplea para su misión de expresar una porción del terreno de la melancolía y el horror diabólico. Poe escribe sus relatos teniendo en mente un simple efecto propenso a estallar en terror o pasión durante el momento final de la historia. Sostiene que en la totalidad de la composición no debe haber palabras que tiendan, directa o indirectamente, a deducir el efecto que el autor se ha propuesto. Lo asombroso es que un amante de la casualidad haya preparado sistemáticamente los elementos que se deben integrar en el relato, como si hubiese sido dotado del don para controlar el destino: azares de la expresión. Así es como sorprende, manipula el campo de lo inesperado, sobresalta al lector y en la apuesta final saca el as de la manga y gana la jugada astutamente. Los detalles funcionan como sostenes del relato hasta que la última oración narra el efecto preciso: el más planeado por el autor y el menos pensado para el lector. En Edgar Poe no es la inventiva lo que deslumbra sino la capacidad de incertidumbre de las situaciones, la aproximación a lo temido por desconocido, a la muerte. Maestro de la desesperación que parece hallar en la muerte el corte al sufrimiento de sus personajes, de su propio dolor. Tomando las palabras del poeta y dramaturgo David H. Lawrence: « Las mejores producciones de Poe no son relatos. Son algo más. Son descripciones del alma humana, retorciéndose en las convulsiones de la ruptura»"""
'''

# arreglo 2) - words - almacena el texto en el método word_tokenize para 
                        # previamente darle valor.
words = word_tokenize(text)


# In[4]:


# Se crea un diccionario para crear una tabla de frecuencias de las palabras.
freqTable = dict()

# Con un for se recorre el texto y se almacena en la tabla.
for word in words:
    word = word.lower() # setea las palabras en minúscula y las almacena en word.
    if word in SW: 
        continue # Si la palabra se encuentra en SW, continua con el ciclo.
    if word in freqTable: # Si la palabra ya se encuentra en la tabla frecuencia,
        freqTable[word] += 1 # Suma 1 a la posición donde se encuentra la palabra.
    else:
        freqTable[word] = 1 # Sino, la palabra en la TF va a ser igual a 1.


# In[5]:


#Muestra la tabla de frecuencias de cada palabra.
freqTable


# In[6]:


# Crea una variable y un diccionario.

# Variable sentences para almacenar las oraciones a valorizar del texto.
sentences = sent_tokenize(text)

# Diccionario sentenceValue para almacenar los valores de las oraciones.
sentenceValue = dict()


# In[7]:


#Se crea un ciclo for para recorrer las oraciones que se encuentran en el texto.
for sentence in sentences:
    # Se crea un segundo for para recorrer los items que se encuentran el la TF.
    for word, freq in freqTable.items():
        if word in sentence.lower(): # Si la palabra se encuentra en las oraciones (en minuscula)
            if sentence in sentenceValue: # Y si la oración está en el diccionario de las oraciones a valorizar.
                sentenceValue[sentence] += freq # Entonces sume 1 al número de frecuencia en la posición de la oración del sV.
            else:
                sentenceValue[sentence] = freq # Sino, que el valor de la posición de la oración sea igual a la frecuencia.


# In[8]:


#Muestra las oraciones ya valorizadas con su respectivo puntaje.
sentenceValue


# In[9]:


# Se crea una variable donde se almacena la suma de los valores.
sumValues = 0

# Se crea un ciclo for para evaluar la oración dentro del Diccionario de las oraciones valorizadas.
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence] # Se suma 1 al valor de la Oración en su respectiva posición
    
# Valor promedio de una oración desde un texto original
average = int(sumValues/ len(sentenceValue)) # Divide la suma de valores en la total de oraciones valorizadas.


# In[10]:


# Se crea una variable para almacenar el resumen a imprimir.
summary = ''

# Se crea un for para recorrer las oraciones almacenadas
for sentence in sentences:
    
    #Donde si, la oración está las oraciones Valorizadas y la posición de la oración es mayor que 1.2 veces el promedio:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        
        # El resumen va a agregar un espacio más la oración que aprobó la condición.
        summary += " " + sentence 


# In[11]:



# Se imprime el resumen.
print ("\n\n\tEl resumen es: ")
print(summary)


# In[ ]:




