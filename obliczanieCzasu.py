import pandas as pd

def czasMin(x):
  #przeliczenie czasu z HH:MM na minuty
  # -> int
  godziny = x[1].split(":")
  minuty = int(godziny[0])*60 + int(godziny[1])

  return minuty

# dane
dane = [[12345, "10:15"], [23451, "10:20"], [12345, "10:30"], [12345, "10:50"] ,[34512, "10:30"], [12345, "11:00"], [23451, "11:40"], [34512, "11:45"], [34512, '12:00'], [34512, '12:10']]

def obecnosc(dane, czasZajec, prog):

  # sortowanie danych wzgledem pierwszej kolumny
  dane = sorted(dane,key=lambda dane:dane[0])

  
  suma = 0
  i = 0
  lista = []
  poprzedni = dane[0][0]
  lista = []


  while i < len(dane)-1:

    """
    print("i:")
    print(i)

    print(dane[i])
    print(dane[i+1])

    print("czas:")
    print(czasMin(dane[i+1]))
    print(czasMin(dane[i]))

    print("obecnosc")
    print(czasMin(dane[i+1])-czasMin(dane[i]))
    """

    if (dane[i][0] == poprzedni):
      suma = suma + czasMin(dane[i+1])-czasMin(dane[i])

      if (i == len(dane) - 2):
        #print("ok")
        lista.append(suma)

      

    else:
      lista.append(suma)

      poprzedni = dane[i][0]
      suma = 0
      suma = suma + czasMin(dane[i+1])-czasMin(dane[i])

      if (i == len(dane) - 2):
        #print("ok")
        lista.append(suma)

    i = i + 2



  osoby = []
  osoby = list(osoby)
  ####################
  #sortowanie osoby
  osoby.sort()
  i = 0

  while i < len(dane):
    #print(dane[i])
    osoby.append(dane[i][0])
    i = i + 1

  osoby = set(osoby)

  #print(osoby)
  #print(lista)

  import pandas as pd 
  

 

  lista = [round(el / czasZajec, 2) for el in lista]
  df = pd.DataFrame(list(zip(osoby, lista)), columns =['osoba', 'czas [%]'])

  print(df.iloc[0][1])
  q = 0
  while q < len(lista):
    print(df.iloc[q][1])
    q= q+1
  
  #if df['czas'][i] > warunek
  
  print(df)

obecnosc(dane, 90, 0.7)
