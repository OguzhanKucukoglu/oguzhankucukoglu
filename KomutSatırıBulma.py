def komutSatiriBul(metin):
    komutSatiriSayisi = 0

    while "#" in metin or "//" in metin or "/*" in metin or "**" in metin:
        if "#" in metin:
            komutSatiriSayisi+=1
            metin = metin.split("#", 1)[1]
        if "//" in metin:
            komutSatiriSayisi+=1
            metin = metin.split("//", 1)[1]
        if "/*" in metin:
            komutSatiriSayisi+=1
            metin = metin.split("/*", 1)[1]
        if "**" in metin:
            komutSatiriSayisi+=1
            metin = metin.split("**", 1)[1]
    return komutSatiriSayisi

kullaniciMetni = input("metin: ")

komutSatiriSayisi = komutSatiriBul(kullaniciMetni)

print("Komut Satırı Sayısı: ", komutSatiriSayisi)