import dataExtraction
import jsonToExcel
import features

# veri çekme - json olarak kaydetme

dataExtraction.dataExtraction()

features.features()
# verileri excel dosyasına dönüştürme

jsonToExcel.jsonToExcel()
