# 🔐 Güvenlik Politikası (SECURITY.md)

Bu proje, kullanıcı verilerinin güvenliğini ön planda tutar ve aşağıdaki güvenlik ilkelerine göre geliştirilmiştir.

---

## 🧱 Güvenlik Temelleri

- Parola verileri *asla düz metin* olarak saklanmaz.
- *bcrypt, Argon2* gibi güçlü hash algoritmaları kullanılır.
- Tüm parolalara benzersiz *salt* değeri eklenir.
- Hassas bilgilerin sızmasını önlemek için env dosyaları .gitignore altında tutulur.
- Giriş denemeleri sınırlanarak brute-force saldırılarına karşı koruma sağlanır.

---

## 🔍 Açıklar ve Güvenlik Bildirimi

Eğer bu projede bir güvenlik açığı keşfederseniz, lütfen aşağıdaki adımları izleyerek bizimle iletişime geçin:

1. Açığı detaylı olarak açıklayın.
2. Geriye dönük veri sızıntısı riskini belirtin.
3. [E-posta: your_email@domain.com] adresine özel olarak bildirin (GitHub Issues üzerinden değil!).

> *Not*: Güvenlik açıklarını sorumlu bir şekilde bildirenlere teşekkür edilir.

---

## 🛠️ Kullanıcı Güvenliği İçin Öneriler

- Projeyi canlı ortamda kullanacaksanız *HTTPS* zorunludur.
- Tüm kullanıcı girişleri için *2FA/MFA* tavsiye edilir.
- Kullanıcı parolaları minimum 12 karakter olmalı ve karmaşık olmalıdır.

---

## 🔁 Sürüm Takibi ve Yama Politikası

- Tüm güvenlik düzeltmeleri PATCH güncellemeleriyle yapılır (örn. v1.0.1).
- Kritik açıklar mümkün olan en kısa sürede kapatılır.
