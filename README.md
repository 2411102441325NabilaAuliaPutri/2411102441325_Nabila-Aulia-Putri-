# Modul Pertemuan 11 – Refactoring SOLID

## Studi Kasus
Validasi Peminjaman Buku Perpustakaan

## Tujuan
Menerapkan prinsip SRP, OCP, dan DIP
pada kode validasi peminjaman buku.

## Before Refactor
- Menggunakan satu class besar (God Class)
- Semua aturan validasi ditulis langsung
- Sulit dikembangkan

## After Refactor
- Aturan dipisahkan ke class masing-masing
- Menggunakan abstraksi (BorrowRule)
- Class utama tidak bergantung pada aturan konkret

## Prinsip SOLID yang Digunakan
- SRP (Single Responsibility Principle)
- OCP (Open Closed Principle)
- DIP (Dependency Inversion Principle)
