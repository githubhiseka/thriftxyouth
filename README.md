# Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

Buatlah virtual environment terlebih dahulu dengan me-run `python -m venv env` lalu aktifkan virtual environment-nya dengan `env\Scripts\activate`. Tergantung permintaan proyeknya, langkah berikutnya biasanya adalah untuk mengunduh package Django melalui `pip install django`. Apabila semua itu sudah berhasil dilakukan, maka bisa membuat proyek Django dengan me-run `django-admin startproject [nama_project]`.

Untuk membuat aplikasi baru dengan nama main, cukup run `python manage.py startapp main`. Langkah krusial selanjutnya adalah untuk menambahkan nama aplikasi tersebut ke dalam dictionary INSTALLED_APPS yang terletak pada settings.py agar aplikasi main bisa terdaftar pada proyek Django.

Routing proyek dapat dilakukan dengan "meng-include" nama aplikasi ke dalam dictionary urlpatterns pada urls.py tingkat proyek. Untuk "meng-include", harus dilakukan import admin, path, dan include masing-masing. Tampilan urlpatterns akan berbentuk seperti berikut.
`urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]`

Membuat model pada aplikasi main cukup mirip dengan membuat constructor untuk sebuah class yang meng-inherit models.Model. Atribut yang akan digunakan adalah name, price, dan description dengan tipe data masing-masing. Cara penulisannya terlampir di bawah.
`class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  description = models.TextField()`
Belum selesai sampai situ, setelah membuat/merubah model, sewajibnya melakukan model migration dengan `python manage.py makemigrations` diikuti dengan `python manage.py migrate`. Langkah terakhir ini dapat dianalogikan dengan git commit dan git push, namun untuk model aplikasi.

skip

Routing aplikasi tidak jauh beda dengan routing proyek. Cukup dengan membuat berkas urls.py pada direktori main, lalu isi berkas tersebut dengan dictionary urlpatterns yang akhirnya akan merujuk kepada fungsi yang menampilkan antarmuka sesuai keinginan, yang telah ter-define pada views.py

panjang
