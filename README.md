Q1: 
    Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp).

A: 
    What happens is that, hero1 will instantiate with its assigned value first (100). Then, after hero1.hp is set to 500, "print(hero1.hp)" will return the updated value (500).

===

Q2:
    Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

A:
    This is important because it passes a reference to the actual object, allowing the method to access both the opponent's properties and its methods directly.

===

Q3:
    Error apa yang muncul saat kamu mencoba melihat info Eudora(eudora.info())?
    Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?

A:
    [AttributeError: 'Mage' object has no attribute 'name']
    
    Passing "Eudora" as an argument only sends the string to Mage.__init__(), but it doesn't automatically create self.name. Without super().__init__(), the parent class constructor never runs to assign self.name = name, so the attribute is never initialized on the object.

===

Q4.1: Percobaan Hacking
    Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan temannya mengapa Python masih mengizinkan akses ini (konsep Name Mangling) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik.

A:  
    Python allows this because double underscores (__) trigger Name Mangling (_Hero__hp), which is intended to avoid subclass attributes colliding with each other rather than strict access security. Python relies on developer discipline rather than compiler rules.
    
    However, accessing variables directly is bad practice because it violates encapsulation and it bypasses data validation setters. 

Q4.2: Uji Validasi
    Hapus logika if dan elif di dalam method set_hp, sehingga isinya hanya self.__hp = nilai_baru.
    Kemudian lakukan hero1.set_hp(-100).
    Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method Setter sangat penting untuk menjaga integritas data dalam game!

A:
    Calling hero1.set_hp(-100) updates hero1.__hp directly to -100 because the validation guard was removed.

    Setter methods are crucial for maintaining data integrity because they enforce game rules and keep object attributes in a valid state.

===

Q5.1: Melanggar Kontrak
    Pada class Hero, hapus (atau jadikan komentar #) seluruh blok method def serang(self, target):. Jalankan programnya.
    Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti pesan error Can't instantiate abstract class Hero with abstract method...?

A:
    [Can't instantiate abstract class Hero without an implementation for abstract method 'attack']

    Because the abstract method is required to be implemented. With it missing, Python refuses to create the object, protecting the program from crashing later when something tries to call a method that doesn't exist in the Hero class itself.

Q5.2: Mencetak Cetakan
    Coba aktifkan baris kode unit = GameUnit(). 
    Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek? Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

A: 
    If Python allowed you to write unit = GameUnit() and you later called unit.attack(), Python would panic because there is no actual code written for it. Blocking instantiation prevents this exact crash. It only acts as a blueprint for its child classes, where they're the ones instantiated.

===

Q6.1: Uji Skalabilitas
    Tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class baru bernama Healer(Hero). Isi method serang milik Healer dengan: print(f"{self.name} tidak menyerang, tapi menyembuhkan teman!"). Masukkan objek Healer ke dalam list pasukan.
    Pertanyaan: Apakah program berjalan lancar?
    Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer ketika harus mengupdate game dengan karakter baru di masa depan?

A:
    Yes, the program runs smoothly. The benefit of polymorphism is that it allows developers to introduce new classes, characters, or items using a template without modifying existing code.This minimizes maintenance and makes scaling a game effortless.

Q6.2: Konsistensi Penamaan 
    Ubah nama method serang pada class Archer menjadi tembak_panah. Jalankan program. Pertanyaan: Apa yang terjadi? Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan berbagai Child Class harus persis sama?

A:
    The method isn't recognized and doesn't print out. Because it doesn't match the "blueprint class" provided by the parent.