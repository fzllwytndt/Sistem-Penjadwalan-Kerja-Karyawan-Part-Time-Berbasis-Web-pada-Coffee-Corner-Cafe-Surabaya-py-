class JadwalKerja:
    def __init__(self, id_pekerja, tugas, hari_kerja, jam_masuk, jam_keluar):
        self.id_pekerja = id_pekerja
        self.tugas = tugas
        self.hari_kerja = hari_kerja
        self.jam_masuk = jam_masuk
        self.jam_keluar = jam_keluar

    def update_jadwal(self, tugas_baru, hari_kerja_baru, jam_masuk_baru, jam_keluar_baru):
        self.tugas = tugas_baru
        self.hari_kerja = hari_kerja_baru
        self.jam_masuk = jam_masuk_baru
        self.jam_keluar = jam_keluar_baru

    def __str__(self):
        return f"Tugas: {self.tugas} - Hari: {self.hari_kerja} - Jam: {self.jam_masuk} - {self.jam_keluar}"
