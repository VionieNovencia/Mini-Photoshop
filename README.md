# Mini-Photoshop

web-app yang dapat digunakan untuk mengedit gambar

# Requirements

1. python versi 3.10.0
2. numpy versi 1.21.3 digunakan untuk mempermudah mengolah array
3. Flask versi 1.1.2
4. PIL versi 8.4.0 digunakan untuk mempermudah mengolah citra

# Cara menggunakan program

1. Clone repositori ini
2. Masuk ke folder frontend dengan cara mengetikkan `cd frontend` pada terminal
3. jalankan `flask run`
4. masukkan link `http://127.0.0.1:5000/` pada browser anda
5. Upload gambar yang ingin diedit
6. Silakan pilih fitur yang anda inginkan untuk mengedit gambar anda

# Fitur

1. undo
   Untuk mengembalikan gambar menjadi gambar sebelum fitur terakhir digunakan pada gambar. Setiap gambar yang di-apply fitur akan disave dengan index tertentu. Fitur ini akan mengambil gambar dengan index kurang 1 dari gambar sekarang. Jika tidak ada gambar sebelumnya, maka akan dikembalikan None
2. redo
   Untuk mengembalikan gambar menjadi gambar sesudah fitur terakhir digunakan pada gambar(biasanya undo). Setiap gambar yang di-apply fitur akan disave dengan index tertentu. Fitur ini akan mengambil gambar dengan index tambah 1 dari gambar sekarang. Jika tidak ada gambar sesudahnya, maka akan dikembalikan None
3. negative
   fitur ini akan mengembalikan versi kebalikan dari gambar. Fitur ini bekerja dengan mengembalikan nilai tiap pixel gambar berdasarkan fungsi f(x,y)' = 255 - f(x,y).

4. grayscale
   fitur ini akan mengembalikan foto dengan nuansa hitam putih. Fitur ini bekerja dengan mengembalikan nilai tiap pixel gambar berdasarkan fungsi f(y) = 0.229*r + 0.587*g + 0.114\*b, dimana r,g,b adalah red, green, blue dan y adalah nilai versi grayscalenya.

5. complement
   fitur ini mengubah tiap pixel pada gambar menjadi kebalikan dari pixelnya. Fitur ini bekerja dengan berdasarkan fungsi f(x)' = ~x

6. rotate90ccw
   fitur ini merotasi gambar sebanyak 90 derajat berlawanan arah jarum jam. Fitur ini bekerja dengan mengubah letak tiap pixel pada gambar awal sebanyak 90 derakat ke arah kiri, atau sesuai dengan fungsi f(y,x)' = f(x,h-y-1), h adalah height pada gambar

7. rotate90cw
   fitur ini kebalikan dari fitur rotate90ccw. Fitur ini bekerja dengan berdasarkan fungsi f(y,x)' = f(w-x-1,y), w adalah width dari gambar.

8. flip horizontal
   fitur ini mengembalikan gambar yang sudah dicerminkan terhadap sumbu-x. Fitur ini bekerja dengan fungsi f(x,y)' = f(w-x-1,y), dengan w adalah width gambar

9. flip vertikal
   fitur ini mengembalikan gambar yang sidah dicerminkan terhadap sumbu-y. Fitur ini bekerja dengan fungsi f(x,y)' = f(x,h-y-1), dengan h adalah height gambar

10 zoom in
fitur ini mengembalikan gambar yang sudah diperbesar menjadi dua kali semula. Cara kerjanya, mula-mula disiapkan gambar kosong dengan ukuran panjang dan lebar dua kali semula. Setiap empat pixel yang berdekatan pada gambar kosong, diisi dengan satu pixel dari gambar semula

11. zoom out
    kebalikan dari zoom out, gambar ini diperkecil menjadi setengah dari gambar semula.

12. brightening
    fitur ini mengembalikan gambar menjadi lebih terang dari sebelumnya. Fitur ini bekerja dengan menambahkan 50 pada tiap pixel pada gambar.

13. contrast stretching
    fitur ini mengembalikan gambar yang sudah diperjelas warnanya. cara kerjanya, lebih jelas dapat dilihat pada referensi

14. log transformation
    melakukan transformasi pada gambar dengan rumus s = c log (1+r), s adalah intensitas keluaran, r adalah intensitas pada pixel, dan c adalah konstanta. Konstanta c didapatkan dengan rumus 255/(log(1+m)), dengan m adalah nilai maksimum pixel pada gambar

15. power transformation
    melakukan transformasi gambar dengan rumus s = cr^gamma, dengan gamma = 2

16. gaussian blue
    fitur ini menghaluskan gambar sehingga tampak seperti efek blurring. fitur ini membuat sebuah matrix yang berfungsi sebagai filter. Penjelasan lebih rinci dapat dilihat pada referensi

17. gaussian sharpening
    sama seperti gaussian blur, bedanya pada fitur ini matrix filter yang digunkana berbeda

18. gaussian noise
    fitur ini menghasilkan gambar yang sudah diberi efek seperti taburan pasir. Cara kerjanya, setiap pixel pada gambar ditambahkan dengan angka random dengan rentang -50 sampai dengan 50.

19. download
    fitur ini akan menyimpan gambar pada folder test dengan akhiran "After"

20. reset
    fitur ini akan mengembalikan gambar semula. Cara kerjanya adalah dengan menampilkan gambar awal yang sebelumnya sudah disimpan

# Referensi

https://informatika.stei.itb.ac.id/~rinaldi.munir/Citra/2021-2022/citra21-22.htm
https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/
https://www.pixelstech.net/article/1353768112-Gaussian-Blur-Algorithm
https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33
