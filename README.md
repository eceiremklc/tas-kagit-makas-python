🎮 Taş, Kağıt, Makas Oyunu

Bu proje, klasik Taş, Kağıt, Makas oyununu Python dilinde terminal üzerinden oynanabilir hale getiren bir uygulamadır. Oyuncu, bilgisayara karşı oynar ve ilk iki eli kazanan oyunu kazanır.

🚀 Nasıl Çalışır?
Oyun Kuralları:

Oyuncu, "taş", "kağıt" veya "makas" seçeneklerinden birini seçer.
Taş, makası yener; makas, kağıdı yener; kağıt ise taşı yener.
İlk iki eli kazanan taraf oyunu kazanır.
Oyuncu "pes" yazarak oyunu sonlandırabilir.
Oyun Akışı:

Oyun başladığında, kurallar ve oyun akışı hakkında bilgi verilir.
Oyuncu bir seçim yapar, bilgisayar ise rastgele bir seçim yapar.
Etap sonuçları güncellenir ve skorlar ekrana yazdırılır.
Bir taraf 2 puana ulaştığında, kazanan ilan edilir.
Oyun sonunda oyuncuya tekrar oynamak isteyip istemediği sorulur.

📄 Kod Açıklamaları

karsilama_mesaji(): Oyuncuyu karşılayıp oyun kurallarını anlatır.
secenekleri_goster(): Oyuncuya seçim yapması için seçenekleri sunar.
skor_guncelle(): Oyuncu ve bilgisayar seçimlerini karşılaştırarak skoru günceller.
tekrar_oyna(): Oyuncuya ve bilgisayara tekrar oynayıp oynamayacaklarını sorar.
tas_kagit_makas_Ece_Irem_Kilic(): Oyunun ana fonksiyonudur. Oyun akışını yönetir ve oyunu başlatır.
