from sistem import SistemPenjadwalan
from tim import Tim
from pekerja import Pekerja
from lemburan import Lemburan
try:
    from tabulate import tabulate
except ImportError:
    def tabulate(data, headers=None, tablefmt=None):
        # Simple fallback formatter returning a plain-text table string
        rows = []
        if headers:
            rows.append(list(headers))
        rows.extend(data)
        if not rows:
            return ""
        cols = len(rows[0])
        widths = [0] * cols
        for r in rows:
            for i, cell in enumerate(r):
                widths[i] = max(widths[i], len(str(cell)))
        sep = " | "
        lines = []
        if headers:
            hdr = sep.join(str(c).ljust(widths[i]) for i, c in enumerate(headers))
            lines.append(hdr)
            lines.append('-+-'.join('-' * w for w in widths))
            for r in data:
                lines.append(sep.join(str(c).ljust(widths[i]) for i, c in enumerate(r)))
        else:
            for r in data:
                lines.append(sep.join(str(c).ljust(widths[i]) for i, c in enumerate(r)))
        return "\n".join(lines)
from datetime import datetime

def hitung_durasi(jam_mulai, jam_selesai):
    fmt = '%H:%M'
    tdelta = datetime.strptime(jam_selesai, fmt) - datetime.strptime(jam_mulai, fmt)
    return tdelta

def validasi_waktu(waktu):
    try:
        datetime.strptime(waktu, '%H:%M')
        return True
    except ValueError:
        return False

def validasi_tanggal(tanggal):
    try:
        date = datetime.strptime(tanggal, '%Y-%m-%d')
        if date.year == datetime.now().year:
            return True
        else:
            return False
    except ValueError:
        return False

def validasi_nama(nama):
    return isinstance(nama, str) and nama.isalpha()

def main():
    sistem = SistemPenjadwalan()
    lemburan = Lemburan()

    while True:
        print("\n=== Sistem Penjadwalan Kerja Karyawan Part Time Berbasis Web pada Coffee Corner Cafe Surabaya ===")
        print("1. Tambah Tim")
        print("2. Tambah Pekerja ke Tim")
        print("3. Tambah Jadwal Kerja")
        print("4. Lemburan")
        print("5. Lihat Semua Tim")
        print("6. Lihat Semua Jadwal")
        print("7. Lihat Data Lemburan")
        print("8. Keluar")
        pilihan = input("Pilih menu (1-8): ").strip()

        if pilihan == "1":
            nama_tim = input("Masukkan nama tim: ").strip()
            tim = Tim(nama_tim)
            hasil = sistem.tambah_tim(tim)
            print(hasil)

        elif pilihan == "2":
            nama_tim = input("Masukkan nama tim: ").strip()
            tim = sistem.cari_tim(nama_tim)
            if tim:
                id_pekerja = input("Masukkan ID pekerja: ").strip()
                nama_pekerja = input("Masukkan nama pekerja: ").strip()
                if validasi_nama(nama_pekerja):
                    tipe_pekerja = input("Tipe Pekerja (Full-Time/Part-Time/Kontrak): ").strip()
                    pekerja = Pekerja(id_pekerja, nama_pekerja, tipe_pekerja)
                    hasil = tim.tambah_pekerja(pekerja)
                    print(hasil)
                else:
                    print("Nama pekerja harus berupa huruf dan tidak boleh berupa angka.")
            else:
                print("Tim tidak ditemukan.")

        elif pilihan == "3":
            id_pekerja = input("Masukkan ID pekerja: ").strip()
            tugas = input("Masukkan tugas: ").strip()
            hari_kerja = input("Masukkan hari kerja (contoh: Senin): ").strip()
            jam_masuk = input("Masukkan jam masuk (hh:mm): ").strip()
            jam_keluar = input("Masukkan jam keluar (hh:mm): ").strip()
            if validasi_waktu(jam_masuk) and validasi_waktu(jam_keluar):
                hasil = sistem.tambah_jadwal(id_pekerja, tugas, hari_kerja, jam_masuk, jam_keluar)
                print(hasil)
            else:
                print("Format waktu tidak valid. Gunakan format hh:mm.")

        elif pilihan == "4":
            while True:
                print("\n=== Menu Lemburan ===")
                print("1. Tambah Lemburan")
                print("2. Cari Lemburan")
                print("3. Hapus Lemburan")
                print("4. Update Lemburan")
                print("5. Lihat Data Lemburan")
                print("6. Kembali ke Menu Utama")
                pilihan_lembur = input("Pilih menu (1-6): ").strip()

                if pilihan_lembur == "1":
                    id_pekerja = input("Masukkan ID pekerja: ").strip()
                    nama_pekerja = input("Masukkan nama pekerja: ").strip()
                    tanggal = input("Masukkan tanggal lembur (yyyy-mm-dd): ").strip()
                    hari = input("Masukkan hari lembur (contoh: Senin): ").strip()
                    jam_mulai = input("Masukkan jam mulai lembur (hh:mm): ").strip()
                    jam_selesai = input("Masukkan jam selesai lembur (hh:mm): ").strip()

                    # Debugging print statements
                    print(f"Nama Pekerja: {nama_pekerja}, Validasi Nama: {validasi_nama(nama_pekerja)}")
                    print(f"Tanggal: {tanggal}, Validasi Tanggal: {validasi_tanggal(tanggal)}")
                    print(f"Jam Mulai: {jam_mulai}, Validasi Waktu Mulai: {validasi_waktu(jam_mulai)}")
                    print(f"Jam Selesai: {jam_selesai}, Validasi Waktu Selesai: {validasi_waktu(jam_selesai)}")

                    if validasi_nama(nama_pekerja) and validasi_tanggal(tanggal) and validasi_waktu(jam_mulai) and validasi_waktu(jam_selesai):
                        pekerja = sistem.cari_pekerja(id_pekerja)
                        if pekerja:
                            hasil = lemburan.tambah_lembur(id_pekerja, nama_pekerja, tanggal, hari, jam_mulai, jam_selesai)
                            print(hasil)
                        else:
                            print("Karyawan tidak ditemukan.")
                    else:
                        print("Format nama, tanggal, atau waktu tidak valid. Nama harus berupa huruf, tanggal harus sesuai dengan tahun sekarang, dan gunakan format yyyy-mm-dd untuk tanggal dan hh:mm untuk waktu.")

                elif pilihan_lembur == "2":
                    id_pekerja = input("Masukkan ID pekerja: ").strip()
                    hasil = lemburan.cari_lembur(id_pekerja)
                    print(hasil)

                elif pilihan_lembur == "3":
                    id_pekerja = input("Masukkan ID pekerja: ").strip()
                    tanggal = input("Masukkan tanggal lembur (yyyy-mm-dd): ").strip()
                    if validasi_tanggal(tanggal):
                        hasil = lemburan.hapus_lembur(id_pekerja, tanggal)
                        print(hasil)
                    else:
                        print("Format tanggal tidak valid. Gunakan format yyyy-mm-dd.")

                elif pilihan_lembur == "4":
                    id_pekerja = input("Masukkan ID pekerja: ").strip()
                    tanggal = input("Masukkan tanggal lembur (yyyy-mm-dd): ").strip()
                    jam_mulai_baru = input("Masukkan jam mulai lembur baru (hh:mm): ").strip()
                    jam_selesai_baru = input("Masukkan jam selesai lembur baru (hh:mm): ").strip()
                    if validasi_tanggal(tanggal) and validasi_waktu(jam_mulai_baru) and validasi_waktu(jam_selesai_baru):
                        hasil = lemburan.update_lembur(id_pekerja, tanggal, jam_mulai_baru, jam_selesai_baru)
                        print(hasil)
                    else:
                        print("Format tanggal atau waktu tidak valid. Gunakan format yyyy-mm-dd untuk tanggal dan hh:mm untuk waktu.")

                elif pilihan_lembur == "5":
                    if not lemburan.lembur_list:
                        print("Belum ada data lemburan.")
                    else:
                        data = []
                        total_jam_lembur = 0
                        for lembur in lemburan.lembur_list:
                            durasi = hitung_durasi(lembur["Jam Mulai"], lembur["Jam Selesai"])
                            total_jam_lembur += durasi.total_seconds() / 3600
                            data.append([lembur["Nama Pekerja"], lembur["Tanggal"], lembur["Hari"], lembur["Jam Mulai"], lembur["Jam Selesai"], str(durasi)])
                        print(tabulate(data, headers=["Nama Pekerja", "Tanggal", "Hari", "Jam Mulai", "Jam Selesai", "Durasi"], tablefmt="grid"))
                        print(f"Total Jam Lembur: {total_jam_lembur:.2f} jam")

                elif pilihan_lembur == "6":
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")

        elif pilihan == "5":
            while True:
                print("\n=== Menu Lihat Semua Tim ===")
                print("1. Lihat Semua Tim")
                print("2. Cari Tim Berdasarkan Nama")
                print("3. Cari Pekerja Berdasarkan Tipe")
                print("4. Kembali ke Menu Utama")
                pilihan_tim = input("Pilih menu (1-4): ").strip()

                if pilihan_tim == "1":
                    if not sistem.tim_list:
                        print("Belum ada tim yang terdaftar.")
                    else:
                        data = []
                        for tim in sistem.tim_list:
                            for pekerja in tim.pekerja:
                                data.append([tim.nama_tim, pekerja.id_pekerja, pekerja.nama, pekerja.tipe])
                        print(tabulate(data, headers=["Nama Tim", "ID Pekerja", "Nama Pekerja", "Tipe Pekerja"], tablefmt="grid"))

                elif pilihan_tim == "2":
                    nama_tim = input("Masukkan nama tim: ").strip()
                    tim = sistem.cari_tim(nama_tim)
                    if tim:
                        data = []
                        for pekerja in tim.pekerja:
                            data.append([tim.nama_tim, pekerja.id_pekerja, pekerja.nama, pekerja.tipe])
                        print(tabulate(data, headers=["Nama Tim", "ID Pekerja", "Nama Pekerja", "Tipe Pekerja"], tablefmt="grid"))
                    else:
                        print("Tim tidak ditemukan.")

                elif pilihan_tim == "3":
                    tipe_pekerja = input("Masukkan tipe pekerja (Full-Time/Part-Time/Kontrak): ").strip()
                    data = []
                    for tim in sistem.tim_list:
                        for pekerja in tim.pekerja:
                            if pekerja.tipe.lower() == tipe_pekerja.lower():
                                data.append([tim.nama_tim, pekerja.id_pekerja, pekerja.nama, pekerja.tipe])
                    if data:
                        print(tabulate(data, headers=["Nama Tim", "ID Pekerja", "Nama Pekerja", "Tipe Pekerja"], tablefmt="grid"))
                    else:
                        print("Tidak ada pekerja dengan tipe tersebut.")

                elif pilihan_tim == "4":
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")

        elif pilihan == "6":
            if not sistem.jadwal_list:
                print("Belum ada jadwal kerja.")
            else:
                data = []
                for jadwal in sistem.jadwal_list:
                    pekerja = sistem.cari_pekerja(jadwal.id_pekerja)
                    if pekerja:
                        data.append([pekerja.nama, jadwal.tugas, jadwal.hari_kerja, jadwal.jam_masuk, jadwal.jam_keluar])
                print(tabulate(data, headers=["Nama Pekerja", "Tugas", "Hari Kerja", "Jam Masuk", "Jam Keluar"], tablefmt="grid"))

        elif pilihan == "7":
            if not lemburan.lembur_list:
                print("Belum ada data lemburan.")
            else:
                data = []
                total_jam_lembur = 0
                for lembur in lemburan.lembur_list:
                    durasi = hitung_durasi(lembur["Jam Mulai"], lembur["Jam Selesai"])
                    total_jam_lembur += durasi.total_seconds() / 3600
                    data.append([lembur["Nama Pekerja"], lembur["Tanggal"], lembur["Hari"], lembur["Jam Mulai"], lembur["Jam Selesai"], str(durasi)])
                print(tabulate(data, headers=["Nama Pekerja", "Tanggal", "Hari", "Jam Mulai", "Jam Selesai", "Durasi"], tablefmt="grid"))
                print(f"Total Jam Lembur: {total_jam_lembur:.2f} jam")

        elif pilihan == "8":
            print("Keluar dari sistem.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()