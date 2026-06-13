class Pekerja:
    def __init__(self, id_pekerja, nama, tipe):
        self.id_pekerja = id_pekerja
        self.nama = nama
        self.tipe = tipe

    def __str__(self):
        return f"[{self.tipe}] [ID: {self.id_pekerja}] {self.nama}"
