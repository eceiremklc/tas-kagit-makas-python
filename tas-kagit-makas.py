import random

def karsilama_mesaji():
    # oyuncuyu karşılayıp oyun kurallarını anlatan fonksiyon
    print("🎮 Hoş Geldin! 🎮")
    print("🎉 Haydi Benimle Taş, Kağıt, Makas Oyna! 🎉")
    print("\n📜 Oyun Kuralları:")
    print("1. Taş, Kağıt veya Makas seçeneklerinden birini seçmelisin.")
    print("2. Taş, makası yener; makas, kağıdı yener; kağıt ise taşı yener.")
    print("3. İlk iki eli kazanan oyunu kazanır.")
    print("4. Pes etmek istersen 'pes' yazabilirsin.")
    print("5. Oyunu kazandıktan sonra bir el daha oynamak istersen tekrar 'evet' diyebilirsin.")
    print("İyi şanslar! 🍀\n")

def secenekleri_goster():
    # Oyuncuya seçim yapması için mesaj gösteren fonksiyon
    print("🪨 📄 ✂️  Seçim yap: taş, kağıt, makas ya da pes.")

def skor_guncelle(kullanici_secimi, bilgisayar_secimi, kosullar):
    # Etabı kimin kazandığını belirleyen ve skoru güncelleyen fonksiyon
    if kullanici_secimi == bilgisayar_secimi:
        print("🤝 Berabere!")
        return 0, 0
    elif kosullar[kullanici_secimi] == bilgisayar_secimi:
        print("🎉 Sen Kazandın! 🎉")
        return 1, 0
    else:
        print("💻 Bilgisayar Kazandı!")
        return 0, 1

def tekrar_oyna():
    # Oyuncuya ve bilgisayara tekrar oynayıp oynamayacağını soran fonksiyon
    tekrar_messages = ['Bir el daha oynamak ister misin?',
                      'Bir karşılaşmaya daha var mısın?',
                      'Bir şans daha?',
                      'Yeni oyuna başlayalım mı?']
    tekrar_mesaj = random.choice(tekrar_messages)
    
    # Kullanıcı cevabını al
    while True:
        print(f"{tekrar_mesaj} (evet/hayır)")
        kullanici_cevabi = input("Cevabın: ").lower()
        if kullanici_cevabi in ['evet', 'hayır']:
            break
        else:
            print("⚠️ Geçersiz bir cevap.")
    
    # Bilgisayar cevabını rastgele belirle
    bilgisayarin_cevabi = random.choice(['evet', 'hayır'])
    print(f"💻 Bilgisayarın cevabı: {bilgisayarin_cevabi}")
    
    # Eğer her iki taraf da evet dediyse oyuna devam et
    if kullanici_cevabi == "evet" and bilgisayarin_cevabi == "evet":
        return True
    return False

def tas_kagit_makas_Ece_Irem_Kilic():
    # ana fonksiyon
    karsilama_mesaji()  # Karşılama mesajını göster
    oyun = 1  # Oyun sayacını başlat
    
    while True:
        oyuncu_skoru = 0
        bilgisayar_skoru = 0
        secenekler = ['taş', 'kağıt', 'makas']
        kosullar = {'taş': 'makas', 'makas': 'kağıt', 'kağıt': 'taş'}
        etap = 1  # Etap sayacını başlat
        
        # Oyuncu veya bilgisayar 2 puan alıncaya kadar devam eden döngü
        while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
            print(f"\n*** Oyun: {oyun} Etap: {etap}***")
            print(f"Skor: Oyuncu {oyuncu_skoru} - {bilgisayar_skoru} Bilgisayar")
            secenekleri_goster()
            
            # Kullanıcının seçimini al
            kullanici_secimi = input("Senin seçimin: ").lower()
            if kullanici_secimi == "pes":
                print("Oyun Bitti! 🛑")
                return
            elif kullanici_secimi not in secenekler:
                print("⚠️ Geçersiz seçim.")
                continue
            
            # Bilgisayarın seçimini rastgele belirle
            bilgisayar_secimi = random.choice(secenekler)
            print(f"💻 Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            # Skorları güncelle
            oyuncu_puani, bilgisayar_puani = skor_guncelle(kullanici_secimi, bilgisayar_secimi, kosullar)
            oyuncu_skoru += oyuncu_puani
            bilgisayar_skoru += bilgisayar_puani
            etap += 1
            
            # Oyun sonlandırma kontrolü
            if oyuncu_skoru == 2:
                print(f"\n🎉 Tebrikler! Oyunu Kazandın! Nihai Skor: Oyuncu {oyuncu_skoru} - {bilgisayar_skoru} Bilgisayar 🎉")
                break
            elif bilgisayar_skoru == 2:
                print(f"\n💻 Bilgisayar Oyunu Kazandı! Nihai Skor: Oyuncu {oyuncu_skoru} - {bilgisayar_skoru} Bilgisayar 💻")
                break
        
        # Tekrar oynama sorusu
        if not tekrar_oyna():
            print("Oyun sona erdi. Tekrar görüşmek üzere! 👋")
            break
            
        oyun += 1  # Oyun sayacını artır

# Oyunu başlat
if __name__ == "__main__":
    tas_kagit_makas_Ece_Irem_Kilic()
