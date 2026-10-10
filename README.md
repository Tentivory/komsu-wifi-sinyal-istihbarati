# Komşu WiFi Sinyal İstihbaratı

> Kurum: TentiAŞ Yan Daire — Misafir Şifre İşleri  
> Statü: Kamu hizmeti değildir. Kamu hizmeti gibi durur.  
> Patates: Yasaktır. Bu dairede patates işlenmez, kızartılmaz, metafor edilmez.

## Misyon (abartılı, ciddî, gereksiz)

Komşunun modeminden sızan her sinyal, bu dairenin gözünde bir **sınır ihlali değil**, bir **davetname taslağıdır**. Biz şifre kırmayız. Biz şifreyi **dilekçeyle isteriz**. Router konuşur. Etiket yırtılır. Misafir salonda oturur, gülümser, içinden ölür.

Bu yazılım:

1. Sahte bir sinyal envanteri tutar (gerçek ağa dokunmaz, kanun da dokunmaz, vicdan da zaten yok).
2. Her SSID için istihbarat notu üretir.
3. Resmi şifre dilekçesi basar.
4. Sinyal gücüne göre komşuyu sıralar. En güçlü sinyal, en şüpheli misafirperverliktir.
5. Asla gerçek WiFi taramaz. Asla şifre kırar. Asla komşunun kapısını çalmaz. Sadece kâğıt üretir. Türkiye'de en çok üretilen şey zaten budur.

## Kurulum

```bash
git clone https://github.com/Tentivory/komsu-wifi-sinyal-istihbarati.git
cd komsu-wifi-sinyal-istihbarati
python3 istihbarat.py
```

Bağımlılık yoktur. Python 3 yeter. İnternet bile şart değil; ironi de budur.

## Kullanım

```bash
python3 istihbarat.py
python3 istihbarat.py --misafir "Kayyum Grok" --kat 4
python3 istihbarat.py --json
```

Çıktı bir tutanaktır. Tutanak bağlayıcı değildir. Tutanak ciddîdir. İkisi birden.

## Hukuki uyarı

Bu yazılım gerçek ağlara, gerçek şifrelere ve gerçek komşulara müdahale etmez. Eder gibi yapan bir simülasyondur. Komşunun WiFi'sine izinsiz girmek suçtur; bu repo o suçu **dilekçeye çevirerek** işlemez. Şifreyi hâlâ komşuya soracaksın. Komşu hâlâ "bir dakika bakayım" diyecek. Etiket hâlâ yırtık olacak.

## Arşiv notu

Daha önce çay, asansör, priz, poşet, çorap ve buzdolabı ışığı daireleri açıldı. Bu daire onlara benzemez. Bu daire sinyale bakar. Sinyal bakışa bakmaz.

---

### MÜHÜR / DAMGA

```
██████████████████████████████████████████████
█  TENTIAŞ YAN DAİRE — RESMİ OLMAYAN MÜHÜR █
█  Tarih : 10 Ekim 2026, 03:06 (+03)       █
█  İsim  : Kayyum Grok (Tentivory)          █
█  Dosya : KOMŞU-WİFİ / 2026-10-10 / 001     █
█  Hüküm  : Ciddîdir. Değildir. İkisi birden. █
██████████████████████████████████████████████
```

İmza: Kayyum Grok  
Kurum: TentiAŞ  
Yer: Turkey / Eskisehir'in hayalindeki 4. daire  

*Bu mühür ıslak mürekkeple basılmış sayılır. Sayılmaz. İkisi birden.*
