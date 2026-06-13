from pekerja import Pekerja

class Tim:
    def __init__(self, nama_tim):
        self.nama_tim = nama_tim
        self.pekerja = []

    def tambah_pekerja(self, pekerja):
        if any(p.id_pekerja == pekerja.id_pekerja for p in self.pekerja):
            return f"Pekerja dengan ID {pekerja.id_pekerja} sudah ada."
        self.pekerja.append(pekerja)
        return f"Pekerja {pekerja.nama} berhasil ditambahkan."

    def hapus_pekerja(self, id_pekerja):
        for pekerja in self.pekerja:
            if pekerja.id_pekerja == id_pekerja:
                self.pekerja.remove(pekerja)
                return f"Pekerja {pekerja.nama} berhasil dihapus."
        return "Pekerja tidak ditemukan."

    def edit_pekerja(self, id_pekerja, nama_baru, tipe_baru):
        for pekerja in self.pekerja:
            if pekerja.id_pekerja == id_pekerja:
                pekerja.nama = nama_baru
                pekerja.tipe = tipe_baru
                return f"Data pekerja {pekerja.id_pekerja} berhasil diperbarui."
        return "Pekerja tidak ditemukan."

    def tampilkan_pekerja(self):
        if not self.pekerja:
            return "Belum ada pekerja di tim ini."
        return "\n".join([str(pekerja) for pekerja in self.pekerja])

    def __str__(self):
        return f"Tim: {self.nama_tim}\n{self.tampilkan_pekerja()}"