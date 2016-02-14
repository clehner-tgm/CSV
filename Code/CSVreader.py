import csv

__author__ = 'Cindy Lehner'
__date__ = '24-01-2016'
__version__ = '1'

"""
    Eine Klasse, die ein CSV-File (mit unterschiedlichem Dialekt) in den Hauptspeicher einlesen,
    ein CSV-File (mit unterschiedlichem Dialekt) an vorhandene Daten im Hauptspeicher anhaengen und
    eingelesene Daten in einem CSV-File (mit unterschiedlichen Dialekte) ausgeben kann.
"""


class CSVreader():

    sn = " "

    """
        filename ist der Name des zu bearbeitenden CSV-Files
    """
    def __init__(self, filename=None):
        self.filename = filename #Festlegen des Filenamens


    def csv_read(self):
        """
            Eine Methode zum Lesen von CSV-Dateien
        """
        with open(self.filename) as file:
            sn = csv.Sniffer() #Initialisieren des Sniffers
            sn.preferred = [";"]

            #Das try und except wurde im Unterricht besprochen und ich habe es so uebernommen
            try:
                dialect = sn.sniff(file.read(1024)) #durch das Sniffen erkennt der Sniffer meistens um welchen Dialekt es sich handelt
            except csv.Error:
                if file.endswith("csv"): #bei einer Fehlermeldung wird der Delimiter manuell gesetzt
                    delimiter = ";" #Setzen des "Seperators"
                else:
                    delimiter = "\t" #Setzen des "Seperators"
                    file.seek(0)
                    reader = csv.reader(file,delimiter=delimiter)
                    dialect = reader.dialect

            file.seek(0) #damit das File wieder an den Anfang zurueckspringt

            reader = csv.reader(file, dialect) #Reader wird festgelegt mit File und dem Dialekt

            text = []
            rownum = 0
            for row in reader:
                if rownum == 0:
                    header = row #Header bestimmen
                else:
                    colnum = 0
                    for col in row:
                        text.append(row) #Anhaengen der Werte an text
                        colnum += 1
                rownum += 1

            file.close() #Schliessen des Files

        return text.copy() #Zurueckgeben des Textes



    def csv_write(self, pfadname, delimiter):
        """
        Eine Methode zum Schreiben von CSV-Dateien
        """
        ifile  = open(self.filename) #Oeffnen des vorhandenen Files
        sn = csv.Sniffer()
        dialect = sn.sniff(ifile.read(1024))
        reader = csv.reader(ifile, dialect)

        ofile  = open(pfadname, "w") #Oeffnen des Files, in welches hineingeschrieben werden soll
        writer = csv.writer(ofile, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_ALL) #Setzen des Writers

        for row in reader:
            writer.writerow(row) #Schreiben in das File

        #Schliessen der beiden Dateien
        ifile.close()
        ofile.close()



if __name__ == "__main__":
    """
    Definition der Main, Aufrufen der Read und Write Methoden
    """
    csv = CSVreader("WahlKopie.csv") #Angeben der Datei
    read = csv.csv_read() #Lesen der Datei
    csv.csv_write("WahlNeu.csv", '\t') #Schreiben in ein neues File
    #print (read) #Ausgeben des Eingelesenen

