# Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

Buatlah virtual environment terlebih dahulu dengan me-run `python -m venv env` lalu aktifkan virtual environment-nya dengan `env\Scripts\activate`. Tergantung permintaan proyeknya, langkah berikutnya biasanya adalah untuk mengunduh package Django dan dependencies-nya melalui `pip install ...`. Apabila semua itu sudah berhasil dilakukan, maka bisa membuat proyek Django dengan me-run `django-admin startproject [nama_project]`.

Untuk membuat aplikasi baru dengan nama `main`, cukup run `python manage.py startapp main`. Langkah krusial selanjutnya adalah untuk menambahkan nama aplikasi tersebut ke dalam dictionary `INSTALLED_APPS` yang terletak pada `settings.py` agar aplikasi `main` bisa terdaftar pada proyek Django.

Routing proyek dapat dilakukan dengan "meng-include" nama aplikasi ke dalam dictionary `urlpatterns` pada `urls.py` tingkat proyek. Untuk "meng-include", harus dilakukan `import admin`, `path`, dan `include` masing-masing. Tampilan `urlpatterns` akan berbentuk seperti berikut.
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

Membuat model pada aplikasi `main` cukup mirip dengan membuat constructor untuk sebuah class yang meng-inherit `models.Model`. Atribut yang akan digunakan adalah `name`, `price`, dan `description` dengan tipe data masing-masing. Cara penulisannya terlampir di bawah.
```
class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  description = models.TextField()
```
Belum selesai sampai situ, setelah membuat/merubah model, sewajibnya melakukan model migration dengan `python manage.py makemigrations` diikuti dengan `python manage.py migrate`. Langkah terakhir ini dapat dianalogikan dengan `git commit` dan `git push`, namun untuk model aplikasi.

Singkat saja, fungsi pada `views.py` dapat ditulis seperti berikut.
```
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'THRIFTxYouth',
        'name': 'Abhiseka Susanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```
Fungsi harus menerima parameter `request` untuk memproses permintaan client, lalu diisi dengan dictionary `context` yang berisi beberapa variabel yang ingin di-pass ke tampilan antarmuka pada template. Tahap terakhirnya adalah me-render permintaan client dengan mem-passing variabel pada `context` ke dalam template `main.html`.

Routing aplikasi tidak jauh beda dengan routing proyek. Cukup dengan membuat berkas `urls.py` pada direktori `main`, lalu isi berkas tersebut dengan dictionary `urlpatterns` yang akhirnya akan merujuk kepada fungsi yang menampilkan antarmuka sesuai keinginan, yang telah terdefinisi pada `views.py`

Untuk melakukan deployment aplikasi ke PWS, tambahkan proyek ke dalam PWS terlebih dahulu. Nantinya, akan diberikan credentials dan link yang akan dibutuhkan untuk mengakses proyek Django yang telah dibuat melalui url deployment PWS` (<username-sso>-<namaproyek>.pbp.cs.ui.ac.id)`. Sebelum melanjutkan ke langkah berikutnya, lakukan 4 mantras of git (pull, add, commit, push) terlebih dahulu untuk mengsinkronkan perubahan ke repository. Kemudian, run `git remote add <link proyek dari PWS>` untuk menghubungkan lokal dengan PWS. Setup terakhir yang perlu dilakukan adalah melakukan push ke PWS dengan mengganti nama branch menjadi `master` dengan `git branch -M master` lalu di push melalui `git push pws master` untuk menampilkan perubahan pada proyek ke url PWS. Setelahnya, hanya perlu mengubah nama branch-nya kembali ke `main` dengan `git branch -M main`. Selamat! Web Django sudah bisa diakses.
