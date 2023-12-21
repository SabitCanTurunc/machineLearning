import dataExtraction
import jsonToExcel
import organizingFeatures
import oneHotEncoding

# veri çekme - json olarak kaydetme
#dataExtraction.dataExtraction()

#verisetini düzenle
organizingFeatures.organize()

# verileri excel dosyasına dönüştür
jsonToExcel.jsonToExcel()

#one-hot encode
oneHotEncoding.oneHotEncode()


