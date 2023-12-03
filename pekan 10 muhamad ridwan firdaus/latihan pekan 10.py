#1 
def lulus_saja(hasil_akhir): 
    lulus = [] 
    for siswa in hasil_akhir: 
        if siswa['nilai'] > 65: 
            lulus.append(siswa['nama']) 
    return lulus 
 
hasil_akhir = [ 
    {'nama':'Reza', 'nilai':70}, 
    {'nama':'Ciut', 'nilai':63}, 
    {'nama':'Dian', 'nilai':80}, 
    {'nama':'Badu', 'nilai':40} 
] 
 
print(lulus_saja(hasil_akhir)) 
#2 
 
def balikan(buah2an): 
    balik = [] 
    for buah in buah2an: 
        balik.insert(0, buah) 
    return balik 
 
print(balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])) 
#3 
 
def duplikasi(buah2an): 
    duplikat = [] 
    for buah in buah2an: 
        duplikat.append(buah) 
        duplikat.append(buah) 
    return duplikat 
 
print(duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])) 
 
#4 
def fungsi(kalimat): 
    vokal = 'aiueoAIUEO' 
    hasil = '' 
    for huruf in kalimat: 
        if huruf not in vokal: 
            hasil += huruf 
    return hasil 
 
print(fungsi('Nurul Fikri'))