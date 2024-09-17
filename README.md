# Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

Buatlah virtual environment terlebih dahulu dengan me-run `python -m venv env` lalu aktifkan virtual environment-nya dengan `env\Scripts\activate`. Tergantung permintaan proyeknya, langkah berikutnya biasanya adalah untuk mengunduh package Django dan dependencies-nya melalui `pip install [options]`. Apabila semua itu sudah berhasil dilakukan, maka bisa membuat proyek Django dengan me-run `django-admin startproject [nama_project]`.

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

Untuk melakukan deployment aplikasi ke PWS, tambahkan proyek ke dalam PWS terlebih dahulu. Nantinya, akan diberikan credentials dan link yang akan dibutuhkan untuk mengakses proyek Django yang telah dibuat melalui url deployment PWS` (<username-sso>-<namaproyek>.pbp.cs.ui.ac.id)`. Sebelum melanjutkan ke langkah berikutnya, lakukan 4 mantras of git (pull, add, commit, push) terlebih dahulu untuk mengsinkronkan perubahan ke repository. Kemudian, run `git remote add <link proyek dari PWS>` untuk menghubungkan lokal dengan PWS. Setup terakhir yang perlu dilakukan adalah melakukan push ke PWS dengan mengganti nama branch menjadi `master` dengan `git branch -M master` lalu di push melalui `git push pws master` untuk menampilkan perubahan pada proyek ke url PWS. Setelahnya, hanya perlu mengubah nama branch-nya kembali ke `main` dengan `git branch -M main`. Agar web bisa diakses melalui url yang telah dibuat, perlu ditambahkan `ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS kamu>"]` pada `ALLOWED_HOSTS` di `settings.py`. Selamat! Web Django sudah bisa diakses.


### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

**Jawab:**

![Django Concept](bagan.png)


### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

**Jawab:**

Git berperan sebagai "manager" kode yang dapat melacak dan menyimpan semua perubahan yang terjadi di dalam file, sehingga mampu untuk balik ke versi sebelum-sebelumnyanya. Git juga memungkinkan kolaborasi antar developer yang serba bisa sehingga menjadi alat yang canggih untuk kerja tim.


### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

**Jawab:**

Menurut saya, django cocok untuk beginner utamanya karena Django merupakan framework yang berbasis Python, yang dianggap banyak orang adalah bahasa pemrograman yang paling noob-friendly.


### 5. Mengapa model pada Django disebut sebagai ORM?

**Jawab:**

Model Django dapat disebut sebagai Object Relational Mapping karena `models.py` melacak dan menyimpan banyak objek dengan atributnya masing-masing sehingga bekerja mirip seperti Object Oriented Programming, bedanya model-model ini berperan sebagai database yang dapat mengirim datanya ke `views.py` untuk menampilkan hal-hal sesuai keinginan developer.


# Tugas 3


### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**Jawab:**

Data delivery penting bagi suatu web platform karena hampir semua aplikasi memerlukan pengiriman dan penerimaan data, seperti jumlah saldo pada e-commerce, login credential suatu aplikasi pelayanan, dan banyak lagi. Dalam sudut pandang user, kita ingin web yang mudah diakses, cepat, responsif, dan optimal tanpa memandang lokasi ataupun gawai yang digunakan. Developer juga harus mampu mendapatkan kepercayaan user pada segi keamanan data karena tak ada yang ingin data pribadinya terekspos ke penyerang-penyerang.

---

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

**Jawab:**

Saya pribadi lebih menyukai format JSON karena sintaks-nya yang lebih mudah dibaca, apalagi berangkat dengan pengalaman menggunakan bahasa pemrograman Java. Namun, memang terdapat beberapa fakta yang menyebabkan JSON lebih sering digunakan oleh kalangan programmer daripada XML. Dari segi sintaks, memang betul JSON lebih mudah dibaca karena penggunaannya lebih singkat dan tidak memerlukan end-tag. Dari segi yang lebih teknis, JSON memungkinkan developer untuk menyimpan apapun dalam suatu array, yang tidak dapat dilakukan pada XML. Karena sintaks-nya yang lebih efisien, JSON juga relatif lebih "ringan" daripada XML yang memerlukan struktur kompleks, menyebabkan ukuran file yang lebih besar. Salah satu perbedaan terbesarnya terletak di parsing pada kedua representasi data. XML harus di-parse menggunakan XML parser, yang dapat memperlambat dan membuat proses relatif lebih rumit. Sementara itu, parsing di JSON cukup menggunakan function standar JavaScript. Ditambah dengan sintaks dan perbedaan ukuran file-nya, JSON biasanya lebih cepat dan efisien.

---

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

**Jawab:**

blbalbalbal

---

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**Jawab:**

halohalo

---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

gini loh
