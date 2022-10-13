Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
-> asynchronous programming akan membuat program yang akan melakukan refresh/load data hanya sebagian dari halaman saja. Sedangkan synchronous programming tiap ada perubahan data mengharuskan melakukan refresh seluruh halaman.



 Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
 -> maksud dari paradigma tersebut adalah code program akan dijalankan jika ada event. contoh penerapan pada tugas ini adalah penerapan add todolist. jika button di klik (onclick) maka script program js akan dijalankan.



 Jelaskan penerapan asynchronous programming pada AJAX.
 -> Penerapan asynchronous programming pada AJAX ialah AJAX dapat mengambil data tanpa mengirim atau menerima (reload seluruh laman website) data dari server secara asynchronous. Dengan begitu, AJAX hanya akan mengirimkan request pada server dan kemudian dilanjutkan langsung untuk eksekusi tanpa menunggu balasan dari server terlebih dahulu.



 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 -> Membuat view baru untuk mengembalikan data task berbentuk json, kemudian membuat path di urls. lalu menggunakan ajax get untuk pengambilan data task di todolist.html. Lalu membuat ajax post, mengambil data dari form lalu mengirimnya ke database dlm bentuk model. setelah itu melakukan refresh untuk tampilan halaman, dengan cara memperbaharui data dengan fetch ajax get. 
