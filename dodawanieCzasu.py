import mysql.connector    
mydb = mysql.connector.connect(host=' ',user=' ', passwd=' ', database=' ')
print(mydb)

mc = mydb.cursor()

# "INSERT INTO obecnosc1 (index, godzina) VALUES (%s, %s)"
polecenie = ("INSERT INTO obecnosc1 (imie, dataw, godzina) VALUES (%s, %s, %s)")

import pandas as pd

def czasMin(x):
  #przeliczenie czasu z HH:MM na minuty
  # -> int
  godziny = x[1].split(":")
  minuty = int(godziny[0])*60 + int(godziny[1])

  return minuty

# dane
dane = [[12345, "10:15"], [23451, "10:20"], [12345, "10:30"], [12345, "10:50"] ,[34512, "10:30"], [12345, "11:00"], [23451, "11:40"], [34512, "11:45"], [34512, '12:00'], [34512, '12:10']]

def obecnosc(dane, czasZajec):
  # funkcja przyjmuje 2 arg

  # dane - lista o wymiarach w x 2 (ilosc wierszy x ilosc kolumn)
  # przykladowy wiersz to 
  # [int,   str]
  # [numer_Index, godzina_Wejscia]
  # [12345, "10:15"]
  
  # czasZajec - pojedyncza wartosc int, ktora zawiera czas trwania pojedynczych zajec wyrazony w minutach
  # przykladowy czasZajec to 
  # 90

  # funkcja po przyjeciu arg oblicza laczny czas obecnosc kazdej osoby na danych zajeciach
  # nastepnie tworzy df, ktory zawiera kazda osobe i czas jej obecnosci na zajeciach podzielony przez czasZajec
  # 
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
    # dodawanie obliczonych czasow dla poszczegolnych osob do bazy danych 
    # df.iloc[q][0] to index danej osoby
    # df.iloc[q][1] to procentowa obencosc (czas_danej_osoby/czasZajec)
    
    # mc.execute(polecenie, (str(df.iloc[q][0]),str(df.iloc[q][1])))
    mc.execute(polecenie, (str(df.iloc[q][0]),str(df.iloc[q][1]),'pusto'))

    mydb.commit()
    #print(df.iloc[q][1])
    q= q+1

  
  print(df)






# polecenie do pobrania danych z danej tab
mc.execute("SELECT * FROM obecnosc1")

#mc.execute("show tables")
mr = mc.fetchall()

print("nareszcie dziala\n")

wpisy = []
wp = [[]]

for r in mr:
  # pobranie danych z wpisow z danego wykladu
  # <index> <godzina>
  # 12345 "10:30"
  # dodanie tych danych do listy wp
  wp.append([r[0],r[1]])

print(wp)

# przekazanie listy pobranej z bazy danych do funkcji do obliczania sumy czasu na zajeciach
# 
# obecnosc(dane, 90)

