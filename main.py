import dataExtraction
import jsonToExcel
import organizingFeatures

# veri çekme - json olarak kaydetme

dataExtraction.dataExtraction()

organizingFeatures.abbreviator()
organizingFeatures.last_words('updated_data.json')
# verileri excel dosyasına dönüştürme

jsonToExcel.jsonToExcel()
