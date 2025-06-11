Aşağıdaki Python uygulaması:

Parola alır

Hashler (bcrypt ile)

Doğrulama yapar

Kullanıcı dostu bir menü ile çalışır


import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def main():
    print("🔐 Parola Güvenliği Uygulamasına Hoş Geldiniz\n")
    print("1. Parola Hashle")
    print("2. Parola Doğrula")
    print("3. Çıkış")

    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == "1":
        password = input("Hashlenecek parolayı girin: ")
        hashed = hash_password(password)
        print("✅ Hashlenmiş Parola:", hashed)

    elif choice == "2":
        password = input("Parolayı girin: ")
        hashed_input = input("Hashlenmiş parolayı girin: ")

        if verify_password(password, hashed_input):
            print("✅ Parola DOĞRU.")
        else:
            print("❌ Parola YANLIŞ.")

    elif choice == "3":
        print("Çıkılıyor... 👋")
        exit()

    else:
        print("❗ Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

if _name_ == "_main_":
    while True:
        main()
        print("\n")


---

🧪 Test Etmek İçin

1. Terminali aç:

pip install -r requirements.txt
python app.py


2. Menüden:

(1) Hash oluştur

(2) Doğruluğu kontrol et
# Kodlamalari buraya yapicaz.
