<div align="center">

# LAPORAN PRAKTIKUM
## ARSITEKTUR MONOLITH vs MICROSERVICES DENGAN FLASK PYTHON

### Disusun Oleh:
Nama : FAJRI AYU  
NIM : 2024903430049  
Kelas : TRKJ

### Program Studi Teknologi Rekayasa Komputer Jaringan
### Jurusan Teknologi Informasi dan Komputer
### Politeknik Negeri Lhokseumawe
### 2026

</div>

---

## Daftar Isi

- [Tujuan Praktikum](#tujuan-praktikum)
- [Dasar Teori](#dasar-teori)
- [Alat dan Bahan](#alat-dan-bahan)
- [Struktur Project](#struktur-project)
- [Implementasi Monolith](#implementasi-monolith)
- [Implementasi Microservices](#implementasi-microservices)
- [Pengujian](#pengujian)
- [Fault Isolation](#fault-isolation)
- [Kesimpulan](#kesimpulan)
- [Laporan Lengkap](#laporan-lengkap)

---

## Tujuan Praktikum

Praktikum ini bertujuan untuk:

- Memahami konsep dasar arsitektur Monolith dan Microservices.
- Membangun backend sederhana menggunakan Flask Python.
- Membuat dan menguji endpoint HTTP.
- Memahami komunikasi antar-service menggunakan HTTP/API.
- Menganalisis perilaku sistem ketika salah satu service mengalami gangguan.

---

## Dasar Teori

### Monolith

Arsitektur Monolith merupakan pendekatan di mana beberapa fitur aplikasi berada dalam satu codebase dan berjalan dalam satu proses aplikasi.

Pada praktikum ini fitur buku dan pesanan dibuat dalam satu aplikasi Flask menggunakan file:

`monolith_app.py`

Aplikasi berjalan pada port:

`5000`

### Microservices

Pada arsitektur Microservices, aplikasi dibagi menjadi beberapa service yang dapat berjalan secara terpisah.

Pada praktikum ini terdapat:

- **Book Service** → port 5001
- **Order Service** → port 5002

Order Service berkomunikasi dengan Book Service melalui HTTP request.

---

## Alat dan Bahan

- Laptop/PC
- Windows
- Python
- Flask
- Requests
- Visual Studio Code
- Git
- GitHub
- PowerShell

---

## Struktur Project

```text
Monolith-Microservices/
│
├── monolith_app.py
├── book_service.py
└── order_service.py
