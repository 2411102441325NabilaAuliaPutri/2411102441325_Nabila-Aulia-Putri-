from dataclasses import dataclass


@dataclass
class BorrowData:
    """
    Model sederhana untuk data peminjaman buku perpustakaan.
    """
    member_name: str
    books_borrowed: int
    membership_active: bool


class BorrowValidatorManager:
    """
    God Class: Menangani semua jenis validasi peminjaman sekaligus.
    Melanggar SRP, OCP, dan DIP.
    """

    def validate(self, data: BorrowData) -> bool:
        print(f"Memulai validasi peminjaman untuk anggota: {data.member_name}")

        # Validasi jumlah buku (hardcoded) -> pelanggaran SRP & OCP
        if data.books_borrowed > 3:
            print("❌ Jumlah buku yang dipinjam melebihi batas (maksimal 3 buku).")
            return False

        # Validasi status anggota (hardcoded) -> pelanggaran SRP & OCP
        if not data.membership_active:
            print("❌ Status keanggotaan tidak aktif.")
            return False

        # Jika ke depan ada aturan baru (misalnya denda, keterlambatan, dll),
        # maka akan ditambahkan if/elif di sini lagi
        # -> method akan semakin panjang dan sulit dirawat (code smell)

        print("✅ Semua validasi berhasil. Peminjaman disetujui.")
        return True


if __name__ == "__main__":
    print("=== SEBELUM REFACTOR (God Class) ===")

    vm = BorrowValidatorManager()

    # 1. Data valid
    andi = BorrowData(
        member_name="Andi",
        books_borrowed=2,
        membership_active=True
    )
    print("\n>>> Test kasus 1: Data valid")
    vm.validate(andi)

    # 2. Jumlah buku melebihi batas
    budi = BorrowData(
        member_name="Budi",
        books_borrowed=5,
        membership_active=True
    )
    print("\n>>> Test kasus 2: Jumlah buku melebihi batas")
    vm.validate(budi)

    # 3. Status anggota tidak aktif
    cici = BorrowData(
        member_name="Cici",
        books_borrowed=1,
        membership_active=False
    )
    print("\n>>> Test kasus 3: Status anggota tidak aktif")
    vm.validate(cici)
