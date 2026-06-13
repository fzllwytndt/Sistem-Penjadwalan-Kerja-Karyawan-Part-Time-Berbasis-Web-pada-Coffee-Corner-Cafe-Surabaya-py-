class Lemburan:
    def __init__(self):
        self.lembur_list = []

    def tambah_lembur(self, id_pekerja, nama_pekerja, tanggal, hari, jam_mulai, jam_selesai):
        if any(l['ID Pekerja'] == id_pekerja and l['Tanggal'] == tanggal and l['Jam Mulai'] == jam_mulai for l in self.lembur_list):
            return f"Lemburan untuk {nama_pekerja} pada {hari}, {tanggal} sudah ada."
        if jam_mulai >= jam_selesai:
            return "Jam mulai lembur tidak boleh lebih besar atau sama dengan jam selesai lembur."
        lembur = {
            "ID Pekerja": id_pekerja,
            "Nama Pekerja": nama_pekerja,
            "Tanggal": tanggal,
            "Hari": hari,
            "Jam Mulai": jam_mulai,
            "Jam Selesai": jam_selesai
        }
        self.lembur_list.append(lembur)
        return f"Lemburan untuk {nama_pekerja} pada {hari}, {tanggal} berhasil ditambahkan."

    def tampilkan_lembur(self):
        if not self.lembur_list:
            return "Belum ada data lemburan."
        return "\n".join([f"{l['Nama Pekerja']} - {l['Hari']}, {l['Tanggal']} ({l['Jam Mulai']} - {l['Jam Selesai']})" for l in self.lembur_list])

    def cari_lembur(self, id_pekerja):
        lembur_pekerja = [l for l in self.lembur_list if l['ID Pekerja'] == id_pekerja]
        if not lembur_pekerja:
            return f"Tidak ada data lemburan untuk ID Pekerja {id_pekerja}."
        return "\n".join([f"{l['Nama Pekerja']} - {l['Hari']}, {l['Tanggal']} ({l['Jam Mulai']} - {l['Jam Selesai']})" for l in lembur_pekerja])

    def hapus_lembur(self, id_pekerja, tanggal):
        lembur_dihapus = [l for l in self.lembur_list if l['ID Pekerja'] == id_pekerja and l['Tanggal'] == tanggal]
        if not lembur_dihapus:
            return f"Tidak ada data lemburan untuk ID Pekerja {id_pekerja} pada tanggal {tanggal}."
        self.lembur_list = [l for l in self.lembur_list if not (l['ID Pekerja'] == id_pekerja and l['Tanggal'] == tanggal)]
        return f"{len(lembur_dihapus)} lemburan berhasil dihapus untuk ID Pekerja {id_pekerja} pada tanggal {tanggal}."

    def update_lembur(self, id_pekerja, tanggal, jam_mulai_baru, jam_selesai_baru):
        for lembur in self.lembur_list:
            if lembur['ID Pekerja'] == id_pekerja and lembur['Tanggal'] == tanggal:
                if jam_mulai_baru >= jam_selesai_baru:
                    return "Jam mulai lembur tidak boleh lebih besar atau sama dengan jam selesai lembur."
                lembur['Jam Mulai'] = jam_mulai_baru
                lembur['Jam Selesai'] = jam_selesai_baru
                return f"Lemburan untuk ID Pekerja {id_pekerja} pada tanggal {tanggal} berhasil diperbarui."
        return f"Tidak ada data lemburan untuk ID Pekerja {id_pekerja} pada tanggal {tanggal}."