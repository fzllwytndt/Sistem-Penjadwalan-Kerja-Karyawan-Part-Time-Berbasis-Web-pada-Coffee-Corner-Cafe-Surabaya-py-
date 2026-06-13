from tim import Tim
from pekerja import Pekerja
from jadwal import JadwalKerja

class SistemPenjadwalan:
    def __init__(self):
        self.tim_list = []
        self.jadwal_list = []
        self.pekerja_dict = {}

    def tambah_tim(self, tim):
        if any(t.nama_tim == tim.nama_tim for t in self.tim_list):
            return f"Tim dengan nama {tim.nama_tim} sudah ada."
        self.tim_list.append(tim)
        return f"Tim {tim.nama_tim} berhasil ditambahkan."

    def hapus_tim(self, nama_tim):
        for tim in self.tim_list:
            if tim.nama_tim == nama_tim:
                self.tim_list.remove(tim)
                return f"Tim {nama_tim} berhasil dihapus."
        return "Tim tidak ditemukan."

    def cari_tim(self, nama_tim):
        for tim in self.tim_list:
            if tim.nama_tim == nama_tim:
                return tim
        return None

    def cari_pekerja(self, id_pekerja):
        return self.pekerja_dict.get(id_pekerja)

    def tambah_jadwal(self, id_pekerja, tugas, hari_kerja, jam_masuk, jam_keluar):
        pekerja = self.cari_pekerja(id_pekerja)
        if pekerja:
            jadwal_baru = JadwalKerja(id_pekerja, tugas, hari_kerja, jam_masuk, jam_keluar)
            self.jadwal_list.append(jadwal_baru)
            return f"Jadwal untuk {pekerja.nama} berhasil ditambahkan."
        else:
            return "Pekerja dengan ID tersebut tidak ditemukan."

    def hapus_jadwal(self, id_pekerja):
        jadwal_dihapus = [jadwal for jadwal in self.jadwal_list if jadwal.id_pekerja == id_pekerja]
        if jadwal_dihapus:
            self.jadwal_list = [jadwal for jadwal in self.jadwal_list if jadwal.id_pekerja != id_pekerja]
            return f"{len(jadwal_dihapus)} jadwal berhasil dihapus untuk ID {id_pekerja}."
        return "Jadwal tidak ditemukan untuk pekerja tersebut."

    def update_jadwal(self, id_pekerja, tugas_baru, hari_kerja_baru, jam_masuk_baru, jam_keluar_baru):
        for jadwal in self.jadwal_list:
            if jadwal.id_pekerja == id_pekerja:
                jadwal.update_jadwal(tugas_baru, hari_kerja_baru, jam_masuk_baru, jam_keluar_baru)
                return f"Jadwal untuk ID {id_pekerja} berhasil diperbarui."
        return "Jadwal tidak ditemukan."

    def tampilkan_jadwal(self, id_pekerja=None):
        if id_pekerja:
            pekerja = self.cari_pekerja(id_pekerja)
            if pekerja:
                jadwal = [jadwal for jadwal in self.jadwal_list if jadwal.id_pekerja == id_pekerja]
                if jadwal:
                    hasil = f"Jadwal untuk {pekerja.nama}:\n"
                    hasil += "\n".join([str(j) for j in jadwal])
                    return hasil
                else:
                    return f"Tidak ada jadwal untuk {pekerja.nama}."
            else:
                return "Pekerja dengan ID tersebut tidak ditemukan."
        else:
            if not self.jadwal_list:
                return "Belum ada jadwal kerja."
            hasil = "Semua Jadwal Kerja:\n"
            hasil += "\n".join([str(j) for j in self.jadwal_list])
            return hasil