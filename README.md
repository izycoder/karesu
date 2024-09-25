![header](https://drive.google.com/uc?export=view&id=16qbmVvmnIyJ3rG36lUi_PEVnTCkLwt9X) 

## 🔗 LINK
[![aplikasi pws](https://img.shields.io/badge/CLICK_HERE-TAUTAN_APLIKASI_PWS-blue?labelColor=red)](http://fariz-muhammad31-karesu.pbp.cs.ui.ac.id/)

## LIST PERTANYAAN TUGAS ✏️

<details tugas1>
  <summary><b style="font-size:25px;">📕 TUGAS 1 - Menulis Esai</b></summary>

### Tulislah sebuah esai minimal 1000 kata yang mengandung poin-poin sebagai berikut.

#### - Pilihlah salah satu platform yang telah dijelaskan dalam materi Topik 01. Sebutkan nama platform yang Anda pilih.
#### - Sebutkan perangkat atau aplikasi yang tergolong dalam platform tersebut yang pernah Anda gunakan.
#### - Berikan contoh serangan siber yang dapat terjadi pada platform tersebut.
#### - Hal apa yang sudah Anda terapkan untuk memastikan perangkat atau aplikasi yang pernah Anda gunakan tersebut aman dari serangan siber?

🔗 Link Esai : https://drive.google.com/file/d/1JenZep8TqXSI5V7b5RL1rfqRfF2-PXtB/view?usp=sharing
</details>

<details tugas2>
  <summary><b style="font-size:25px;">📕 TUGAS 2 - Implementasi MVT pada Django</b></summary>
  
  ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya     sekadar mengikuti tutorial).

1. kita dapat membuat sebuah proyek Django baru dengan menginstall django terlebih dahulu beserta library dan package lainnya yang dibutuhkan dalam proses development. kemudian untuk membuat proyeknya kita dapat menggunakan perintah "django-admin startproject karesu ." dalam hal ini karesu adalah nama proyeknya. nantinya akan terbuat direktori baru sesuai dengan nama proyeknya. di posisi ini kita telah membuat proyek Django baru.
2. Untuk membuat aplikasi dengan nama main pada proyek kita dapat menggunakan perintah "python manage.py startapp main" setelah dijalankan akan membuat direktori baru dengan nama main. Direktori main berisi struktur awal aplikasi Django.
3. Untuk melakukan routing pada proyek agar dapat menjalankan aplikasi main kita dapat daftarkan aplikasi main ini ke dalam proyek dengan menambahkan 'main' di file settings.py dalam direktori proyek namaproyek dalam hal ini karesu di variabel INSTALLED_APPS. dengan ini kita telah mendaftarkan aplikasi main ke dalam proyek.
4. Untuk membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, dan description kita dapat merubah file models.py di dalam direktori proyek. dalam isi berkas kita dapat menambahkan class dengan nama Product yang berisi name dengan tipe charfield max_length = 255 (opsional panjangnya tetapi harus ada max length), price dengan tipe integerfield, dan description dengan tipe textfield.
5. Untuk membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kita dapat mengimport "from django.shortcuts import render" untuk mengimpor fungsi render dari modul django.shortcuts, fungsi render ini untuk menampilkan tampilan HTML dengan data yang diberikan. kemudian isi dari views.py bisa diisi dengan fungsi show_main yang menerima parameter request, Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. isi dari fungsi bisa diisi dengan context sebagai dictionary yang berisi data untuk dikirimkan ke tampilan. kemudian return dari fungsinya adalah "return render(request, "main.html", context)" yang fungsinya untuk me-render tampilan main.html dengan menggunakan fungsi render. render disini mengambil tiga argumen yaitu request, main.html, dan context. request adalah objek permintaan HTTP yang dikirim oleh pengguna. main.html adalah nama berkas template yang akan digunakan untuk me-render tampilan. context adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.
6. Untuk membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py kita dapat membuat file dengan nama urls.py di dalam aplikasi main dan mengkonfigurasinya. urls.py ini akan  bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main. kita dapat menambahkan main di variabel app_name untuk memberikan nama unik pada pola URL dalam aplikasi. kemudian kita akan menambahkan rute URL dalam urls.py untuk menghubungkannya ke tampilan main. kita harus merubah isi file urls.py yang terdapat di direktori proyek, berbeda dengan file yang tadi sudah kita rubah. di dalamnya kita tambahkan rute URL ke tampilan main di dalam variabel urlpatterns.
7. Untuk melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet kita dapat membuka https://pbp.cs.ui.ac.id/web/ dan mendaftar menggunakan sso ui. setelah itu kita dapat menambahkan proyek baru dengan nama yang diinginkan. setelah itu kita mendapatkan credentials dari pws yang harus disimpan. lalu kita harus menambahkan url deployment kita di settings.py dalam proyek pada ALLOWED_HOSTS. lalu kita Lakukan git add, commit, dan push perubahan ini ke repositori GitHub. kemudian dapat kita lakukan project command yang terdapat di pws. Ketika melakukan push ke PWS, akan ada window yang meminta username dan password dan gunakan credentials yang sebelumnya disimpan (bukan SSO UI). karena sebelumnya branch berubah jadi master kita rubah lagi menjadi main dengan perintah "git branch -M main". kita bisa melihat status proyek di website pws. status building artinya proyek masih dalam proses deployment , running artinya proyek sudah bisa diakses dengan URL deployment, dan failed apabila terdapat hal yang error. kita bisa menekan view project untuk menuju halaman proyek. Apabila kedepannya ada perubahan pada proyek Django yang ingin dipush ke PWS, kita perlu add dan commit ke github lalu menjalankan perintah "git push pws main:master"
8. terakhir untuk membuat berkas README.md kita cukup membuat file baru yang berisi text atau tulisan yang perlu kita tulis di dalamnya.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client akan menggunakan browser untuk mengakses URL dengan mengirimkan request ke server Django. kemudian terdapat URL routing, Django memeriksa urls.py dengan URL. jika URL benar dan cocok maka reqest akan diteruskan ke views.py. views.py berfungsi untuk menangani logika sesuai permintaan dan memanggil model dari database. selain itu, view juga menentukan template berkas HTML yang akan dikembalikan sebagai response. models.py bisa dibilang sebagai jembatan antara kode dan database. setelah data dari model diperoleh views.py, Django akan menggabungkannya dengan template berkas HTML yang sesuai. setelah HTML selesai dirender, maka Django mengirimkan response berisi berkas HTML dan browser akan menampilkan halaman yang berisi informasi yang diminta.

![gambar](https://drive.google.com/uc?export=view&id=1EwN3MYR-3_ngXpIUrqYSSbxwspOkxFyf) 

#### jadi ringkasan alurnya adalah
#### CLIENT(permintaan dari browser, membuka URL) -> urls.py(Django memeriksa urls.py dan mencocokannya) -> views.py(memanggil models.py  mengambil data dari databse) -> models.py(data diteruskan ke berkas HTML yang nanti dirender) -> berkas HTML(HTML yang sudah dirender akan dikembalikan ke client sebagai response)


### Jelaskan fungsi git dalam pengembangan perangkat lunak!

git sangat membantu pengembang perangkat lunak dalam hal kolaborasi. dengan git yang open source, git bisa dipakai oleh para pengembang untuk menyimpan proyeknya dan bisa dibuat menjadi backup karena git bisa mengembalikan ke versi yang sebelum terjadi error. selain itu, git juga merupakan platform yang fleksibel yang bisa dipakai untuk hosting. contohnya terdapat Gitlab , Github, dan masih banyak lagi. 

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, hal yang paling penting dalam pengembangan khususnya perangkat lunak adalah pemahaman dari perangkat lunak itu sendiri. sebelumnya kita telah mempelajari bahasa pemrograman Python dalam DDP-1 sehingga framework Django sendiri akan lebih mudah untuk dipahami dan digunakan karena menggunakan bahasa pemrograman Python. selain itu,  framework Django juga memiliki banyak kelebihan seperti menyederhanakan proses development yang sangat menghemat waktu. komunitas Django juga bisa dibilang besar dengan 23335 member di discord, hal ini sangat membantu jika terdapat error atau hal yang belum dipahami dalam proses development menggunakan framework Django.

### Mengapa model pada Django disebut sebagai ORM?

ORM atau Object-Relational Mapper adalah salah satu fitur Django yang memungkinkan developer untuk berinteraksi dengan database menggunakan objek python ketimbang menulis kueri SQL secara langsung. kita bisa analogikan dengan projek tugas ini yaitu ketika membuat model, model disini akan menjadi representasi struktur tabel dalam basis data yang nantinya digunakan untuk menyimpan dan mengelola data aplikasi. dalam django, model kita bisa berinteraksi untuk membuat, membaca, memperbarui, dan menghapus data dalam basis data dengan object python. kita juga bisa menggunakan shell django untuk berinteraksi. alih alih menulis kueri SQL langsung, dengan kemudahan ini model pada django disebut sebagai ORM.
</details>

<details tugas3>
  <summary><b style="font-size:25px;">📕 TUGAS 3 - Implementasi Form dan Data Delivery pada Django </b></summary>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

dalam pengembangan platform karena platform modern sering kali melibatkan interaksi antara beberapa sistem, seperti server dan klien (browser atau aplikasi mobile). Di sinilah data delivery menjadi penting karena memungkinkan transfer data yang efektif dan efisien antar sistem.

Saat pengguna melakukan aksi seperti submit form atau request data, klien perlu mengirimkan data ke server untuk diproses. Server kemudian memproses data tersebut dan mengirimkan respon kembali ke klien. Tanpa data delivery yang baik, platform tidak akan berfungsi dengan benar, karena pertukaran data yang efisien dan akurat menjadi kunci dari pengalaman pengguna yang baik.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya JSON lebih baik dibandingkan XML, hal ini juga yang membuat JSON lebih populer dibandingkan XML. 

<b>Kemudahan Penggunaan dan Sintaks</b><br>JSON menggunakan format yang lebih sederhana, yakni pasangan kunci-nilai, yang sangat mirip dengan struktur data yang umum di banyak bahasa pemrograman modern seperti Python (dictionary) atau JavaScript (object). Dengan sintaks yang lebih ringkas dan mudah dibaca, JSON memudahkan dalam memahami serta menulis data, terutama saat berinteraksi dengan API. Sebaliknya, XML menggunakan struktur seperti pohon yang lebih bertele-tele karena adanya tag pembuka dan penutup, membuat file lebih panjang dan sulit dibaca.

<b>Kecepatan Penguraian</b><br> JSON dapat diurai lebih cepat karena langsung menggunakan fungsi bawaan JavaScript, yang sangat efisien dalam banyak bahasa pemrograman. Ini penting bagi mahasiswa yang sering mengerjakan proyek yang membutuhkan transfer data cepat dan ringan, seperti pengembangan web atau aplikasi mobile. Sebaliknya, XML memerlukan parser khusus yang bisa memperlambat proses penguraian.

<b>Ukuran File</b><br> JSON cenderung menghasilkan ukuran file yang lebih kecil karena tidak memerlukan tag yang banyak seperti XML. Hal ini membuat proses transfer data lebih cepat.

<b>Keamanan</b><br> JSON lebih aman dibandingkan XML, terutama karena XML rentan terhadap serangan injeksi entitas eksternal (XXE) dan deklarasi tipe dokumen eksternal (DTD).

<b>Popularitas di Industri</b><br> Seiring dengan semakin banyaknya penggunaan API modern dan pengembangan berbasis web, JSON menjadi format yang lebih diminati. JSON lebih kompatibel dengan stack teknologi modern yang digunakan dalam pengembangan aplikasi.

Secara keseluruhan, JSON lebih populer karena kesederhanaannya, efisiensinya dalam penguraian dan transfer data, serta keamanannya yang lebih baik, menjadikannya pilihan utama dalam banyak skenario pengembangan aplikasi.


### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

fungsi dari method is_valid() pada form Django adalah untuk proses validasi data yang dimasukkan oleh pengguna. Method ini secara otomatis mengecek apakah data yang diinputkan sesuai dengan aturan yang telah ditentukan dalam form, seperti tipe data yang benar, panjang karakter yang tepat, atau format yang valid.

Alasan mengapa kita memerlukan is_valid() adalah untuk mencegah pengguna memasukkan data yang tidak sesuai dengan yang kita butuhkan, misalnya menghindari pengguna memasukkan huruf ke dalam field yang seharusnya diisi angka.

Dengan menggunakan method bawaan seperti is_valid(), kita bisa lebih fokus pada pengembangan fitur lain tanpa harus khawatir membuat sistem validasi yang rumit.


### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token (Cross-Site Request Forgery Token) berfungsi untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF), yang merupakan serangan di mana penyerang mencoba memanipulasi pengguna agar mengirimkan permintaan berbahaya tanpa disadari.

Jika kita tidak menambahkan csrf_token dalam form Django, aplikasi kita menjadi rentan terhadap serangan CSRF. Penyerang bisa memanfaatkan kelemahan ini dengan mengirimkan permintaan palsu atas nama pengguna tanpa sepengetahuan mereka, seperti melakukan perubahan data atau transaksi tanpa izin. Ini berbahaya, terutama pada aplikasi yang melibatkan informasi sensitif atau transaksi penting, misalnya aplikasi e-commerce atau sistem akademik.

csrf_token memberikan lapisan perlindungan tambahan dengan memastikan bahwa setiap permintaan yang dikirimkan ke server berasal dari sumber yang sah.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

<b>1. Membuat input form untuk menambahkan objek model pada app sebelumnya.</b><br>
kita dapat membuat input form dengan cara membuat berkas baru pada direktori main dengan nama berkas forms.py isi dari forms.py adalah 

    from django.forms import ModelForm
    from main.models import Product

    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description"]
disini 'model = product' sebagai definisi input form agar sesuai dengan atribut model product<br>
'fields = .. 'digunakan  sebagai definisi atribut model product yang akan digunakan untuk form

lalu kita bisa membuat fungsi create_product_entry yang menerima parameter request pada berkas views.py yang berada di direktori main.

pertama tama kita import module yang dibutuhkan sebagai berikut

    from django.shortcuts import render,redirect
    from main.forms import ProductForm
    from main.models import Product


lalu kita buat fungsi create_product_entry

    def create_product_entry(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)

'form = ProductForm...' digunakan untuk membuat ProductForm t berdasarkan input dari user.<br>
'form.is_valid()' digunakan untuk memvalidasi isi dari input<br> 
'form.save' digunakan untuk menyimpan hasil input form<br>
'return redirect...' akan mengembalikan url yang sesuai dengan fungsi show_main pada views.py

lalu kita bisa membuat berkas HTML baru dengan nama create_product_entry.html pada direktori main/templates. Isi create_mood_entry.html dengan kode


    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}

kemudian kita harus menambahkan urlpatterns pada urls.py yang akan mendifinisikan url serta menampilkan tampilan html. kita perlu menambahkan

    from main.views import ....., create_product_entry
    urlpatterns = [
        ...., 
        path('create-product-entry', create_product_entry name='create_product_entry'),

        ....
    ]


<b>2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. serta 
Membuat routing URL untuk masing-masing views yang telah ditambahkan</b><br>
untuk XML, kita pertama tama harus menambahkan import module pada views.py di direktori main yang sesuai yaitu 

    from django.http import HttpResponse
    from django.core import serializers

lalu kita bisa membuat fungsi dengan nama show_xml yang memuat sebuah variabel di dalam fungsi tersebut dan menyimpan hasil query dari seluruh data yang ada pada Product dengan return berupa HttpResponse dan parameter content_type="application/xml"

    def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

serializers disini untuk translate objek model menjadi format lain seperti dalam fungsi ini adalah XML.

lalu di urls.py pada direktori main kita import fungsi show_xml

    from main.views import ...,show_xml

dan tambahkan path url ke dalam url patterns

    ...
    path('xml/', show_xml, name='show_xml'),
    ...

kita bisa ulangi ini semua untuk JSON, XML by id, dan JSON by id 

dengan cara membuat fungsi show_json, show_xml_by_id, dan show_json_by_id dengan kode berikut

    def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

perbedaannya di xml by id dan json by id kita harus menambahkan variabel 

    data = Product.objects.filter(pk=id)

yang berfungsi menyimpan hasil query dari data dengan id tertentu yang ada pada Product.<br>
tidak lupa kita menambahkan import pada urls.py di main menjadi 

    from main.views import ...,show_xml,show_json show_xml_by_id,show_json_by_id

dan menambahkan url patterns menjadi

    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),

    ...


### Postman ScreenShot:
![json](https://drive.google.com/uc?export=view&id=1wNUb3h4X188o9lgDbGMS_C_kl8TO8LCe)
![xml](https://drive.google.com/uc?export=view&id=14oeDRAAY1TH4ktnJuCx1_zQPSEVgSxX4) 
![xmlid](https://drive.google.com/uc?export=view&id=1DWkDAIl73rW9mMPHdVAVH3hN192B7kG6) 
![jsonid](https://drive.google.com/uc?export=view&id=1T0YNG7NZ78Dvj2W3cwdrTiNXhAERINiv) 

</details>

<details tugas4>
  <summary><b style="font-size:25px;">📕 TUGAS 4 - Implementasi Autentikasi, Session, dan Cookies pada Django</b></summary>

### Apa perbedaan antara HttpResponseRedirect() dan redirect() Jelaskan cara kerja penghubungan model Product dengan User!
HttpResponseRedirect() untuk membuat respon redirect manual dengan menyebutkan URL tujuan secara lengkap dan ekspklisit sebagai argumen. <br>

Sedangkan, redirect bisa lebih fleksibel karena bisa menerima berbagai input, seperti nama view, URL, atau instance model, dan secara otomatis mengonversinya menjadi URL tujuan. Ini mengurangi kemungkinan kesalahan dan mempermudah pengelolaan pengalihan dalam aplikasi. <br> 

### cara menghubungkan model product dengan user sebagai berikut:

### 1. Import Model User
Pertama, kita perlu mengimpor model User dari django.contrib.auth.models, karena model ini sudah tersedia secara default di Django.
    
        from django.contrib.auth.models import User

### 2. Tambahkan ForeignKey pada Model Product
Selanjutnya, pada model Product, tambahkan field ForeignKey untuk membuat relasi antara Product dan User. Parameter <code> on_delete=models.CASCADE </code> memastikan bahwa jika pengguna dihapus, semua produk yang terhubung dengan pengguna tersebut juga akan dihapus. Buka <code>models.py</code> yang ada pada subdirektori <code>main</code> dan tambahkan kode berikut
    
    ...
    from django.contrib.auth.models import User
    ...

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
#### Penjelasan Kode:

<i>Potongan kode diatas berfungsi untuk menghubungkan satu product entry dengan satu user melalui sebuah relationship, dimana sebuah product entry pasti terasosiasikan dengan seorang user.</i>

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
authentication adalah proses verifikasi identitas pengguna yang sedang login sedangkan authorization adalah proses verifikasi izin akses pengguna yang sedang login. ketika pengguna login, pengguna menginput informasi dan mengirimnya ke server. 

django mengimplementasikan kedua konsep ini dengan cara memeriksa kredensial pengguna yang dikirimkan. Jika valid, Django menciptakan sesi yang menandakan bahwa pengguna sudah terautentikasi. Ini adalah bagian dari authentication (autentikasi), yaitu verifikasi identitas pengguna.

Setelah autentikasi berhasil, Django menggunakan authorization (otorisasi) untuk memeriksa apakah pengguna memiliki izin mengakses sumber daya tertentu. Django mengelola otorisasi menggunakan model izin berbasis grup atau level akses yang telah diatur. Jika pengguna tidak memiliki izin, mereka akan dilarang mengakses halaman atau tindakan yang dilindungi.

Untuk mengimplementasikan autentikasi dan otorisasi dalam kode, Django menyediakan berbagai fungsi bawaan. Untuk autentikasi, Django memiliki metode seperti <code>UserCreationForm</code>, <code>AuthenticationForm</code>, <code>authenticate()</code>, <code>login()</code>, dan <code>logout()</code>. Metode authenticate() digunakan untuk memverifikasi kredensial pengguna, sedangkan login() digunakan untuk memasukkan pengguna ke dalam sesi jika autentikasi berhasil. Fungsi logout() digunakan untuk mengeluarkan pengguna dari sesi.

Untuk otorisasi, Django menggunakan decorator seperti <code>@login_required</code> yang memastikan pengguna harus login terlebih dahulu sebelum mengakses halaman tertentu dalam views.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan sesi yang diidentifikasi melalui cookies. Saat pengguna login, Django membuat cookie yang berisi <code>session ID</code>. Cookie ini dikaitkan dengan data pengguna yang tersimpan di server, memungkinkan Django mengenali pengguna pada setiap permintaan berikutnya.

![cookiz](https://drive.google.com/uc?export=view&id=17CT7YZAtKHT0Sgm6Tuk8svUuVvRHWSts)

Cookies ini digunakan oleh Django untuk mengelola autentikasi dan menjaga sesi pengguna. Cookie <code>csrftoken</code> digunakan untuk melindungi dari serangan CSRF (Cross-Site Request Forgery), sementara sessionid digunakan untuk melacak sesi pengguna yang login, dan last_login menyimpan informasi tentang kapan pengguna terakhir login.

Tidak semua cookies aman digunakan. Beberapa cookies berisiko jika tidak dilindungi dengan benar. Cookies yang tidak diatur dengan flag Secure dan HttpOnly bisa diekspos pada serangan, seperti skrip jahat yang mencuri data cookies. Cookies yang dikirim tanpa enkripsi melalui koneksi HTTP juga rentan terhadap serangan man-in-the-middle. Oleh karena itu, penting untuk menggunakan praktik keamanan yang tepat, seperti mengaktifkan flag keamanan pada cookies dan menggunakan HTTPS untuk melindungi informasi sensitif.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Mengimplementasikan fungsi registrasi, login, dan logout
untuk mengimplementasikan fungsi registrasi kita dapat menambahkan fungsi <code>register</code>  pada <code>views.py</code>
    
    ...
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    
    ...
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

disini dengan <code>Form = UserCreationForm(request.POST)</code> kita membuat form untuk pendaftaran pengguna baru menggunakan data yang nanti diisi oleh pengguna. kemudian dengan <code>form.is_valid()</code> kita cek apakah data yang diisi sudah benar dan sesuai. kemudian dengan <code>form.save()</code> kita simpan datanya ke daatabase. pesan sukses akan dikirim kepada pengguna dan mengalihkan pengguna ke  halaman lain setelah selesai registrasi.

kemudian kita perlu membuat laman HTML pada direktori <code>main/templates</code> yang sesuai dengan nama <code>register.html</code> yang berisi

    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}

    <div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}

tidak lupa di <code>urls.py</code> kita import dan tambahkan path urlnya

    from main.views import register
    
    urlpatterns = [
        ...
        path('register/', register, name='register'),
    ]

Selanjutnya, untuk mengimplementasi login kita dapat menambahkan fungsi <code>fungsi_user</code> pada <code>views.py</code> seperti

    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login

    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

nah, sama seperti sebelumnya tentu kita juga perlu membuat page html yang sesuai dengan nama login.html pada direktori <code>main/templates</code> yang berisi

    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}

tak lupa kita tambahkan <code>urls.py</code> 

    from main.views import login_user

    urlpatterns = [
        ...
        path('login/', login_user, name='login'),
    ]

terakhir, untuk logout kita tambahkan fungsi <code>logout_user</code> pada <code>views.py</code>

    from django.contrib.auth import logout

    def logout_user(request):
        logout(request)
        return redirect('main:login')

kita bisa tambahkan button logout di <code>main.html</code> yang berada di direktori <code>main/templates</code>

    ...
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    </a>
    ...

tak lupa kita tambahkan kode di urls.py

    from main.views import logout_user

    urlpatterns = [
        ...
        path('logout/', logout_user, name='logout'),
    ]

#### untuk membuat dua akan pengguna dengan masing masing 3 data 
pengguna dapat terlebih dahulu daftar pada laman <code>http://127.0.0.1:8000/register/</code><br>
![register](https://drive.google.com/uc?export=view&id=1Zd1Me5Q_4JKZ4JtYNL24LJrK-pxpRpBA)

kemudian masing masing pengguna dapat mendaftarkan barangnya pada laman <code>http://127.0.0.1:8000/create-product-entry</code><br>
![productentry](https://drive.google.com/uc?export=view&id=1Zd1Me5Q_4JKZ4JtYNL24LJrK-pxpRpBA)

nantinya tampilan masing masing pengguna menjadi

#### tampilan pengguna 1
![pengguna1](https://drive.google.com/uc?export=view&id=1nuWz2fTpna8xPKbEw8EqFTikgaHLmTl-)
#### tampilan pengguna 2
![pengguna2](https://drive.google.com/uc?export=view&id=1tVTu5vvDgYEqJX1WQgcIvwYdjbOiyt0n)
#### menghubungkan product dengan user
untuk menghubungkan product dengan user, kita dapat menambahkan  <code>ForeignKey</code> Di dalam model <code>Product</code>, tambahkan <code>user = models.ForeignKey(User, on_delete=models.CASCADE)</code> untuk membuat hubungan antara entri product dan pengguna. Ini berarti setiap input produk akan terkait dengan pengguna tertentu, dan jika pengguna dihapus, semua entri produk miliknya juga akan dihapus. carana sebagai berikut

tambahkan di <code>models.py</code>

    from django.contrib.auth.models import User
    ....
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        .....

kemudian agar pengguna yang login bisa tahu bahwa dia sudah login, kita bisa menambahkan sebuah informasi nama siapa yang sedang login dengan cara 

    def show_main(request):
        product_entries = Product.objects.filter(user=request.user)
        
        context = {
            'nama_aplikasi' : 'karesu',
            'nama': request.user.username,
            ...
        }

#### detail informasi pengguna yang sedang logged in dengan cookies 
![cookiesimp](https://drive.google.com/uc?export=view&id=1voEJ9mcoTPvX4p7l1-J15Y_kuDnYTUx2)

</details>

<details tugas5>
  <summary><b style="font-size:25px;">📕 TUGAS 5 - TBA.</b></summary>
  TBA.
</details>

<br>
Fariz Muhammad Rayhansyah Ramadhan
<br>
2306203854