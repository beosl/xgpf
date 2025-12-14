import requests
import json

# --- Kullanıcıdan alınan ve analiz edilen bilgiler ---

# GitHub README'ye göre önerilen API uç noktası
API_URL = "https://api.chatanywhere.tech/v1/chat/completions"

# Sizin sağladığınız API Anahtarı
API_KEY = "sk-jiv0fLyrXtWIxjLpRiqpBAV5OR1WLYtwMIkaEwh9JYbrK4K3"

# --- İstek Bilgileri ---

HEADERS = {
    "Content-Type": "application/json",
    # Kimlik doğrulama başlığı (Authorization Header)
    "Authorization": f"Bearer {API_KEY}"
}

# Gönderilecek JSON verisi (Payload)
# gpt-3.5-turbo modeli ve Ziçços karakteri için test mesajı
PAYLOAD = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Ziçços, hava bugün çok güzel değil mi?"}
    ],
    "temperature": 0.8
}

# --- API Çağrısını Gerçekleştirme ---

print("API çağrısı yapılıyor...")
try:
    response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD)
    
    # HTTP Durum Kodunu Yazdır
    print(f"\n--- HTTP Durum Kodu: {response.status_code} ---")

    # Yanıt içeriğini JSON olarak yazdır
    if response.status_code == 200:
        response_json = response.json()
        print("\n--- BAŞARILI YANIT (TAM JSON ÇIKTISI) ---")
        # JSON yanıtını düzenli formatta yazdır
        print(json.dumps(response_json, indent=4, ensure_ascii=False))

        # Modelin Cevabını (Content) Yazdır
        try:
            cevap = response_json['choices'][0]['message']['content'].strip()
            print("\n--- ÇEKİLEN CEVAP ---")
            print(cevap)
        except (KeyError, IndexError):
            print("\nUYARI: Yanıt 200 OK olmasına rağmen beklenen 'choices' yapısı bulunamadı veya 'content' boş.")
            
    else:
        # Hata Durumu (4xx, 5xx)
        print("\n--- HATA YANITI ---")
        print(response.text)
        
except requests.exceptions.RequestException as e:
    print(f"\nİSTEK HATASI: {e}")

