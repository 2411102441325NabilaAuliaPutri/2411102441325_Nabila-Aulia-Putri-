from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List


# =====================================
# MODEL DATA (HANYA MENYIMPAN DATA)
# =====================================

@dataclass
class BorrowData:
    """
    Model data peminjaman buku perpustakaan.
    """
    member_name: str
    books_borrowed: int
    membership_active: bool


# =====================================
# ABSTRAKSI (DIP)
# =====================================

class BorrowRule(ABC):
    """
    Kontrak / aturan umum untuk validasi peminjaman.
    """
    @abstractmethod
    def validate(self, data: BorrowData) -> bool:
        pass


# =====================================
# ATURAN VALIDASI (SRP)
# =====================================

class BookLimitRule(BorrowRule):
    """
    Validasi jumlah buku yang dipinjam.
    """
    def validate(self, data: BorrowData) -> bool:
        if data.books_borrowed > 3:
            print("❌ Jumlah buku melebihi batas (maksimal 3 buku).")
            return False
        return True


class MembershipStatusRule(BorrowRule):
    """
    Validasi status keanggotaan.
    """
    def validate(self, data: BorrowData) -> bool:
        if not data.membership_active:
            print("❌ Status keanggotaan tidak aktif.")
            return False
        return True


# =====================================
# CLASS UTAMA (DIP + OCP)
# =====================================

class BorrowService:
    """
    Menjalankan semua aturan peminjaman buku.
    """
    def __init__(self, rules: List[BorrowRule]):
        self.rules = rules

    def process(self, data: BorrowData) -> bool:
        print(f"\nMemulai validasi peminjaman untuk anggota: {data.member_name}")

        for rule in self.rules:
            if not rule.validate(data):
                print("❌ Peminjaman ditolak.")
                return False

        print("✅ Semua validasi berhasil. Peminjaman disetujui.")
        return True


# =====================================
# MAIN PROGRAM (BUKTI OCP)
# =====================================

if __name__ == "__main__":
    print("=== SESUDAH REFACTOR (SOLID) ===")

    # Daftar aturan (bisa ditambah tanpa ubah BorrowService)
    rules = [
        BookLimitRule(),
        MembershipStatusRule()
    ]

    service = BorrowService(rules)

    # 1. Data valid
    andi = BorrowData(
        member_name="Andi",
        books_borrowed=2,
        membership_active=True
    )
    service.process(andi)

    # 2. Jumlah buku melebihi batas
    budi = BorrowData(
        member_name="Budi",
        books_borrowed=5,
        membership_active=True
    )
    service.process(budi)

    # 3. Status anggota tidak aktif
    cici = BorrowData(
        member_name="Cici",
        books_borrowed=1,
        membership_active=False
    )
    service.process(cici)
