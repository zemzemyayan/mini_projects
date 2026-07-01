import pandas as pd
import csv
import chardet
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import os

def get_file_name(file_path):
    return os.path.basename(file_path)


class CsvFiles:
    csv_files={
        "current_book_list":"C:\\Users\\HP\\Desktop\\python_2\\Student_Library_Management_System\\current_book_list.csv",

"borrow_list":"C:\\Users\\HP\\Desktop\\python_2\\Student_Library_Management_System\\borrow_list.csv",

"registered_students":"C:\\Users\\HP\\Desktop\\python_2\\Student_Library_Management_System\\registered_students.csv",

"return_books":"C:\\Users\\HP\\Desktop\\python_2\\Student_Library_Management_System\\return_books.csv",

"registered_books_list":"C:\\Users\\HP\\Desktop\\python_2\\Student_Library_Management_System\\registered_books_list.csv",

    }
    

class CSVManager:
   
    encodings={}
    def __init__(self,csv_files): #CSVManager nesneni bir csv_files listesi alır 
        self.csv_files=csv_files
        self.detect_encoding()

    # dosyaların karakter kodlamasını tahmin edecek olan fonksiyon:
    def detect_encoding(self):
        for file_path in self.csv_files:#csv dosyaları üzerinde geziniyoruz
            if file_path not in CSVManager.encodings:
                with open(file_path,'rb') as f:  # dosya ikili kodlama okuma modunda açıldı
                    result=chardet.detect(f.read()) # fonksiyon bir sözlük döner 
                    CSVManager.encodings[file_path]=result['encoding'] #result sözlüğünde ilgili dosyanın karakter kodlamsı

    #!read_csv
    def read_csv(self,file_path):
        if file_path in CSVManager.encodings: # dosya yolu encodings sözlüğünde mevcut sa 
            encoding=CSVManager.encodings[file_path] # dosyanın karakter kodlaması bilgisi alınır
            with open(file_path,'r',encoding=encoding,newline='') as f:
                reader=csv.reader(f)
                data=list(reader)
                return data
        else:
            print(f"{get_file_name(file_path)} dosyasına ait bir karakter kodlaması bulunamadı!")
            return None
        
    #!read_dict_csv
    def read_dict_csv(self,file_path):
        if file_path in CSVManager.encodings: # dosya yolu encodings sözlüğünde mevcut sa 
            encoding=CSVManager.encodings[file_path] # dosyanın karakter kodlaması bilgisi alınır
            with open(file_path,'r',encoding=encoding, newline='') as f:
                reader=csv.DictReader(f)
                data=list(reader)
                return data
        else:
            print(f"{get_file_name(file_path)} dosyasına ait bir karakter kodlaması bulunamadı!")
            return None
            
    #!write fonksiyonu
    def write_csv(self,file_path,data):
        if file_path in CSVManager.encodings:
            encoding=CSVManager.encodings[file_path] # dosyanın karakter kodlamasını aldık
            with open(file_path,'w',encoding=encoding,newline='') as f:
                writer=csv.writer(f)
                if isinstance(data[0],list): # eğer data birden fazla satır içeriyorsa
                    writer.writerows(data)
                else:
                    writer.writerow(data)
        else:
            print(f"{get_file_name(file_path)} dosyasına ait bir karakter kodlaması bulunamadı!")

    #!write_dict_csv fonksiyonu
    def write_dict_csv(self, file_path, data,file_name):
        if file_path in CSVManager.encodings:
            encoding = CSVManager.encodings[file_path]
            with open(file_path, 'w', encoding=encoding, newline='') as f:
                writer = csv.writer(f)
                # Başlıkları (header) yaz
                if file_name=="registered_students":
                    writer.writerow(["name","surname","student_no","record_date_time"])

                elif file_name=="return_books":
                    writer.writerow(["ISBN","student_no","return_date_time","is_delivery_date_time"])

                elif file_name=="borrow_list":
                    writer.writerow(["ISBN","student_no","borrowed_date_time","delivery_date_time"])

                elif file_name=="current_book_list":
                    writer.writerow(["book_name","author","ISBN"])

                elif file_name=="registered_books_list":
                    writer.writerow(["book_name","author","ISBN","record_date_time"])


                # Verileri yaz
                writer.writerows([list(d.values()) for d in data])
        else:
            print(f"{self.get_file_name(file_path)} dosyasına ait bir karakter kodlaması bulunamadı!")

    #!append fonksiyonu
    def append_csv(self, file_path, new_data):
        if file_path in CSVManager.encodings:
            encoding = CSVManager.encodings[file_path]

            # Dosyanın boş olup olmadığını kontrol ederiz
            is_empty = not self.read_dict_csv(file_path)
            
            # Verileri ekleriz
            with open(file_path, 'a', encoding=encoding, newline='') as f:
                writer = csv.writer(f)
                
                # Eğer dosya boşsa, başlıkları da ekleriz
                if is_empty and isinstance(new_data, list) and len(new_data) > 0 and isinstance(new_data[0], dict):
                    writer.writerow(new_data[0].keys())
                
                # Tek bir satır ekliyorsak writer.writerow kullanırız
                if isinstance(new_data, list) and isinstance(new_data[0], dict):
                    for data_row in new_data:
                        writer.writerow(list(data_row.values()))
                else:
                    writer.writerow(new_data)  # Tek bir liste ekliyorsak
        else:
            print(f"{self.get_file_name(file_path)} dosyasına ait bir karakter kodlaması bulunamadı!")



class Student:

    csv_manager=CSVManager(CsvFiles.csv_files.values())
    def __init__(self,name,surname,student_no):
        self.student_no=student_no
        self.name=name
        self.surname=surname

    # bir öğrencinin şimdiye kadar almış olduğu tüm kitapların listesini oluşturur
    def borrowed_books_list(self): 
        #return book listesinden öğrenci numararı student_no olan kitap isimlerini liste2 ye ekle
        read_return_list=Student.csv_manager.read_dict_csv(CsvFiles.csv_files["return_books"])
        list_ISBN2=[record["ISBN"] for record in read_return_list if record["student_no"]==self.student_no]
        read_book=Student.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        book_name_list2=[ record["book_name"] for record in read_book if  record["ISBN"] in list_ISBN2]
        return book_name_list2


    def show_info(self): # öğrencinin genel bilgilierini gösterir
        return f"name: {self.name} surname: {self.surname} student_no: {self.student_no} öğrenci skoru {len(self.borrowed_books_list())}: .."



class Book:

    csv_manager=CSVManager(CsvFiles.csv_files.values())
    def __init__(self,book_name,author,ISBN):
        self.book_name=book_name
        self.author=author
        self.ISBN=ISBN
    
    def get_skor_book(self): 
        #return book listesinden öğrenci numararı student_no olan kitap isimlerini liste2 ye ekle
        read_data=Book.csv_manager.read_dict_csv(CsvFiles.csv_files["return_books"])
        list_ISBN=[record["ISBN"] for record in read_data if record["ISBN"]==self.ISBN]
        return len(list_ISBN)
    

    def show_info(self):
        return f"""book name: {self.book_name} author: {self.author} isbn no: {self.ISBN} kitabın skoru: 
        {self.get_skor_book()} """
    
        

class StudentProcesses:

    csv_manager=CSVManager(CsvFiles.csv_files.values())
    #!add_student
    def add_student(self,student): #aldığı student nesnesini registered_student.csv dosyasına kaydeder
        data=[student.name,student.surname,student.student_no] 
        read_data=StudentProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        for record in read_data:
            if record["student_no"] == data[2]:
                print(f"{data[2]} numaralı öğrenci zaten kütüphaneye kayıtlıdır.")
                return
            
        StudentProcesses.csv_manager.append_csv(CsvFiles.csv_files['registered_students'],data)
        print(f"{data[2]} numaralı öğrenci başarıyla kaydedildi.")

    
    #!remove_student
    def remove_student(self,student_no): # Öğrenciyi kütüphaneden siler.
        read_data=StudentProcesses.csv_manager.read_dict_csv(CsvFiles.Config.csv_files['registered_students']) 
        state=False
        for record in read_data:
            if record["student_no"]==student_no:
                state=True
        
        if state:
            new_data_list=[record for record in read_data if record['student_no'] != student_no]
            StudentProcesses.csv_manager.write_dict_csv(CsvFiles.Config.csv_files['registered_students'],new_data_list,"registered_students")
            print(f"{student_no} numaralı öğrenci başarıyla silindi.")
        else:
            print(f"Silmeye çalıştığınız {student_no} numaralı öğrenci listede mevcut değil")

    #!list_all_student:
    def list_all_student(self):
        read_data=StudentProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        for record in read_data:
            print(record["name"]," ",record["surname"]," ",record["student_no"]," ", record["record_date_time"])
        

    #!update_student_information:
    def update_student_information(self,student_no):
        read_data=StudentProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        if not self.is_there_student(student_no):
            print("Bilgilerini güncellemek istediğiniz öğrenciye ait bir kayıt bulunamadı.")
            return

        name=input("isim giriniz: ")
        surname=input("soyisim giriniz: ")
        st_no=input("öğrenci numarası giriniz: ")
        for record in read_data:
            if record["student_no"]==student_no:
                record["name"]=name
                record["surname"]=surname
                record["student_no"]=st_no
                break
        StudentProcesses.csv_manager.write_dict_csv(CsvFiles.csv_files["registered_students"],read_data,"registered_students")
        print("Bilgileriniz başarıyla güncellendi..")


    #!is_there_student
    def is_there_student(self,student_no):
        read_data=StudentProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        student_no_list=[record["student_no"] for record in read_data ]
        for no in student_no_list:
            if student_no in no:
                return True
            else:
                return False




class StudentStatistics:

    csv_manager=CSVManager(CsvFiles.csv_files.values())
    #!en çok kitap alan öğrenciyi döner 
    def get_popular_student(self):
        #len(self.borrowed_books_list())
        read_data=StudentStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        student_list=[ Student(record["name"],record["surname"],record["student_no"]) for record in read_data]
        sorted_student_skor_list=sorted(student_list, key=lambda student: len(student.borrowed_books_list()),reverse=True)
        print("en çok kitap ödnünç alan öğrenci: ",sorted_student_skor_list[0].name,sorted_student_skor_list[0].surname," skor:",len(sorted_student_skor_list[0].borrowed_books_list()))
         

    #!get_number_of_student: tüm öğrenci sayısını döner   
    def get_number_of_student(self):
        read_data=StudentStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        return len(read_data)


    #!öğrencileri kayıt olma tarihine göre listeler
    def sorted_for_registered_date_time(self):
        read_data=StudentStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        sorted_read_data=sorted(read_data, key= lambda record: record["record_date_time"])
        print("Öğrencilerin kayıt edilme tarihine göre listelenmesi ")
        for record in sorted_read_data:
            print(record["name"]," ",record["surname"]," ",record["record_date_time"])



    # tüm öğrencilerin skorlarının bir ortalamsını döner böylece kaç öğrenci ortlama kitap alıyor 
    def get_average_for_student_skor(self):
        read_data=StudentStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
        student_list=[Student(record["name"],record["surname"],record["student_no"]) for record in read_data]
        sum=0
        for student in student_list:
            sum+=len(student.borrowed_books_list())
        return sum/len(student_list)




class BookProcesses:
     
    csv_manager=CSVManager(CsvFiles.csv_files.values())
     #!add_book
    def add_book(self,book,record_date_time):
        data=[book.book_name,book.author,book.ISBN] # eklencek kitap 
        BookProcesses.csv_manager.append_csv(CsvFiles.csv_files['registered_books_list'],data)
        #?kayıt edilidği tarihi kaydetmek için kodu yaz tarih bilgisini tarih nesnesine dönüştür

     #!remove_book
    def remove_book(self,isbn_no):
        read_data=BookProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files['registered_books_list']) 
        state=False
        for record in read_data:
            if record["ISBN"]==isbn_no:
                state=True

        if state:
            new_data_list=[record for record in read_data if record['ISBN'] != isbn_no]
            BookProcesses.csv_manager.write_dict_csv(CsvFiles.csv_files['registered_books_list'],new_data_list,"registered_books_list")
            print(f"{isbn_no} numaralı kitap listeden başarıyla silindi.")
        else:
            print(f"Silmeye çalıştığınız {isbn_no} numaralı kitap listede mevcut değil.")


    #!list_all_books
    def list_all_books(self): # Tüm kitapları yazar adı-> kitap adı şeklinde listeler 
        read_data=BookProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files['registered_books_list'])
        for record in read_data:
            print(f"author name: {record['author']} book name: {record['book_name']}")

    #!is_thre_book
    def is_there_book(self,isbn_no):
        read_data=BookProcesses.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        isbn_no_list=[record["ISBN"] for record in read_data ]
        for no in isbn_no_list:
            if isbn_no in no:
                return True
            else:
                return False



class  BookStatistics:

    csv_manager=CSVManager(CsvFiles.csv_files.values())
 
    #!en çok ödüç alınan kitbı döner
    def get_popular_book(self):
        read_data=BookStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        books_list=[Book(record["book_name"],record["author"],record["ISBN"])for record in read_data ]
        skor_list=sorted(books_list, key= lambda book: book.get_skor_book(),reverse=True)
        print("en çok ödünç alınan kitap:",skor_list[0].book_name," skor: ",skor_list[0].get_skor_book())


    #!registered_books listesini kitap ismi alfabetik sırasına göre listeler  author:book_name
    def sorted_for_book_name(self):
        read_data=BookStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        books_list=[Book(record["book_name"],record["author"],record["ISBN"])for record in read_data ]
        book_names=sorted(books_list,key= lambda book: book.book_name)
        print("Kitap isimlerinin alfabetik sıralamnsına göre kitap listesi")
        for book in book_names:
            print(book.author," -> ",book.book_name)


    #!registered_books listesini yazar adı alfabetik sırasına göre listeler  author:book_name
    def sorted_for_author_name(self):
        read_data=BookStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        books_list=[Book(record["book_name"],record["author"],record["ISBN"])for record in read_data ]
        book_author=sorted(books_list,key= lambda book: book.author)
        print("Yazar isimlerinin alfabetik sıralamnsına göre kitap listesi")
        for book in book_author:
            print(book.author," -> ",book.book_name)


    #!sorted_for_record_date_time kitapları kayıt edilme tarihine göre listeler
    def sorted_for_record_date_time(self):
        read_data=BookStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        sorted_read_data=sorted(read_data, key= lambda record: record["record_date_time"])
        print("Kitapların kayıt edilme tarihine göre listesi ")
        for record in sorted_read_data:
            print(record["book_name"]," ",record["ISBN"]," ",record["record_date_time"])
        


    #!sorted_book_for_book_skor kitapları kitap skoruna göre listeler
    def sorted_book_for_book_skor(self):
        read_data=BookStatistics.csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
        books_list=[Book(record["book_name"],record["author"],record["ISBN"])for record in read_data ]
        skor_list=sorted(books_list, key= lambda book: book.get_skor_book(),reverse=True)
        for record in skor_list:
            print(record.book_name," -> ",record.get_skor_book())



class LibraryBookStudentProcesses:
    #!borrow_book
    def borrow_book(self,book,student,borrowed_date_time): # öğrecinin bir kitap ödünç almasını sağlar
        csv_manager=CSVManager(CsvFiles.csv_files.values()) 
        date=DeliveryTrackingSystem()

        #öğrenci listeye kayitli mi
        def ogrenci_listeye_kayitlimi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
            number_list=[record["student_no"] for record in read_data]
            return student.student_no in number_list
        
        #kitap kütüphane bünyesinde varmı:
        def kitap_kutuphanede_varmi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
            book_isbn_list=[  record["ISBN"]  for record in read_data]
            borrow_book_name_list=[ record["book_name"] for record in read_data]
            borrow_author_list=[ record["author"] for record in read_data]
            return (book.ISBN in book_isbn_list )and (book.book_name in borrow_book_name_list)  and (book.author in borrow_author_list)
        
        #kitap ödünç alınalar listesinde mi
        def kitap_odunc_alinanlar_listesindemi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["borrow_list"])
            borrow_book_isbn_list=[ record["ISBN"] for record in read_data]
            return book.ISBN in borrow_book_isbn_list
        
        #öğrencinin aynı kitabı almaya hakkı varmı:
        def ogrencini_kitabi_almaya_hakki_varmi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["return_books"])
            count=1
            for record in read_data:
                if record["ISBN"]==book.ISBN and record["student_no"]==student.student_no:
                    count+=1

            return count<=3

        #kitabın ödünç alınacağı tarih aynı öğrencinin aynı kitabı en son iade ettiği tarihten önce olamaz


        if not ogrenci_listeye_kayitlimi():
            print("öğrenci listeye kayıtlı değil")
            answer=input("Listeye kaydınızı oluşturmak istermisiniz :")
            if answer=="evet":
                lbs=StudentProcesses()
                lbs.add_student(student)
                return
        
        if not kitap_kutuphanede_varmi():
            print("Kitap Kütüphanede mevcut değildir.")
            return

        if kitap_odunc_alinanlar_listesindemi():
            print("Kitap daha önceden ödünç alınmış. Lütfen daha sonra tekrar gelin")
            return
                
        if not ogrencini_kitabi_almaya_hakki_varmi():
            print(f"""{student.name} \"{book.book_name}\" Kitabını alma hakkın kalmadı. En erken {date.earliest_borrowing_date(student.student_no,book.ISBN)} tarihinde tekrar alabilirsin.""")
            return

        # koşullar sağlandığı takdirde:
        # öğrencinin kalan hakkını hesapla
        def remain_right():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["return_books"])
            count=0
            for record in read_data:
                if record['ISBN']==book.ISBN and record['student_no']==student.student_no:
                    count+=1
            return 3-count


        print(f"""{student.name} \"{book.book_name}\" Kitabını tekar almak için {remain_right()} hakkın kaldı""")
        print(f"""{student.name} teslim aldığın kitabı {date.book_return_date(borrowed_date_time)} tarihinde geri iade etmelisin """)


        # ödünç alınan kitabı borrow_list e ekle
        borrowdate=datetime.strptime(borrowed_date_time,'%d-%m-%Y').date()
        data=[book.ISBN,student.student_no,borrowdate.strftime('%d-%m-%Y'),date.book_return_date(borrowed_date_time)] # eklencek kitap 
        csv_manager.append_csv(CsvFiles.csv_files['borrow_list'],data)




     # current_book_list den ödünç alınan kitabı sil
        read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["current_book_list"])
        new_data=[ record for record in read_data if record["ISBN"] != book.ISBN]
        csv_manager.write_dict_csv(CsvFiles.csv_files["current_book_list"],new_data,"current_book_list")


    #!return book
    def return_book(self,book,student,return_date_time):

        csv_manager=CSVManager(CsvFiles.csv_files.values())
        #kitap kütüphanede varmı
        def kitap_kutuphanede_varmi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["registered_books_list"])
            book_isbn_list=[  record["ISBN"]  for record in read_data]
            borrow_book_name_list=[ record["book_name"] for record in read_data]
            borrow_author_list=[ record["author"] for record in read_data]
            return ( book.ISBN in book_isbn_list) and( book.book_name in borrow_book_name_list) and ( book.author in borrow_author_list)
        
        #kitap ödünç alınanlar listesinde mi 
        def kitap_odunc_alinalar_listesinde_varmi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["borrow_list"])
            book_isbn_list=[  record["ISBN"]  for record in read_data]
            borrow_student_no_list=[ record["student_no"] for record in read_data]
            return (book.ISBN in book_isbn_list ) and ( student.student_no in borrow_student_no_list )
        
        #öğrenci listeye kayıtlı mı
        def ogrenci_listeye_kayitlimi():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files["registered_students"])
            number_list=[record["student_no"] for record in read_data]
            return student.student_no in number_list
        
        #teslim tarihi ödünç alma tariihnden öncemi kontrolü
        def delivery_date_is_not_logical():
            read_borrow_list=csv_manager.read_dict_csv(CsvFiles.csv_files["borrow_list"])
            for record in read_borrow_list:
                if record["ISBN"]==book.ISBN and record["student_no"]==student.student_no:
                    borrowed_date=datetime.strptime(record["borrowed_date_time"],'%d-%m-%Y').date()
            returdate=datetime.strptime(return_date_time,'%d-%m-%Y').date()
            
            return returdate.strftime('%d-%m-%Y')  < borrowed_date.strftime('%d-%m-%Y') 


        if not kitap_odunc_alinalar_listesinde_varmi():
            print("Daha önceden kütüphaneden ödünç alınmamış bir kitabı iade edemezsiniz!")
            return

        if not kitap_kutuphanede_varmi():
            print("İade etmeye çalıştığınız kitap kütüphanemizde mevcut değildir.")
            return

        if not ogrenci_listeye_kayitlimi():
            print(f"{student.student_no} numarasına ait kayıt bulunamadı")
            answer=input("Listeye kaydınızı oluşturmak istermisiniz :")
            if answer=="evet":
                lbs=StudentProcesses()
                lbs.add_student(student)
            return
           
        if delivery_date_is_not_logical():
            print("iade etme tarihi ödünç alma tarihinden önce olamaz !")
            return
            
        
        
        #öğrencinin teslim etmesi gerek tarih ile teslim ettiği tarih uyşuyormu:
        def is_delivery_date_time():
            read_data=csv_manager.read_dict_csv(CsvFiles.csv_files['borrow_list']) 
            for record in read_data:
                if record["ISBN"]==book.ISBN:
                    date=record["delivery_date_time"]
            returdate=datetime.strptime(return_date_time,'%d-%m-%Y').date()
            return returdate.strftime('%d-%m-%Y') <= date


        #kitap önce return_books listesine kaydet 
        returdate=datetime.strptime(return_date_time,'%d-%m-%Y').date()
        data=[book.ISBN,student.student_no,returdate.strftime('%d-%m-%Y'),is_delivery_date_time()]    
        csv_manager.append_csv(CsvFiles.csv_files["return_books"],data)

        #sonra kitabı borrow listten sil
        read_data=csv_manager.read_dict_csv(CsvFiles.csv_files['borrow_list']) 
        new_data_list=[record for record in read_data if record['ISBN'] != book.ISBN]
        csv_manager.write_dict_csv(CsvFiles.csv_files['borrow_list'],new_data_list,"borrow_list")

        #son olarak kitap teslim edildği için current_book_list e ekle
        data=[book.book_name,book.author,book.ISBN]    
        csv_manager.append_csv(CsvFiles.csv_files["current_book_list"],data)

        print("Kitap iade işlemi başarılı")   
        print("iyi günler..")
                     



class DeliveryTrackingSystem:

    """
    -> öğrencinin aldığı kitabı iade etmesi gereken tarih
    -> iade süresi 10 gün gecikirse 1 ceza 20 gün gecikirse 2 ceza 30 gün gecikirse kayıt silinme
    -> her kitabın iade edilmesi gereken tarih
    -> Belirli bir öğrencinin geç teslim ettiği kitapları kontrol eder ve ceza hesaplar.

    """
    csv_manager=CSVManager(CsvFiles.csv_files.values())
    #!gecikme sürelerine bağlı ceza tipleri
    def gecikme_bagli_olarak_ceza_turu(self):
        pass

    #!bir ögrencinin geç teslim ettiği kitaplar
    def gec_teslim_edilen_kayitlar_listesi(self):
        #öğrenci bir kitabı aldığı zaman teslim etmesi gereken tarihi teslim edilmesi gerek tarih listesine ekle
        pass


    
    #!öğrencinin aldığı kitabı iade etmesi gereken tarih
    # öğrencinin kitabı aldığı tarih parametre olarak alınıcak ve 30 gün artısı return edilicek
    def book_return_date(self,borrowed_date):
        day, month, year = map(int, borrowed_date.split('-'))
        date = datetime(year, month, day)
        new_date = date + relativedelta(months=1)

        new_day = new_date.day
        new_month = new_date.month
        new_year = new_date.year

        # Gün ve ay değerlerini iki basamağa tamamla
        new_day_str = f"{new_day:02d}"
        new_month_str = f"{new_month:02d}"

        # Tarih formatını oluştur
        formatted_date = f"{new_day_str}-{new_month_str}-{new_year}"

        return formatted_date
    
    #!earliest_borrowing_date
    def earliest_borrowing_date(self,student_no,isbn_no):
        read_data=DeliveryTrackingSystem.csv_manager.read_dict_csv(CsvFiles.csv_files["return_books"])
        date_list=[record["return_date_time"] for record in read_data if student_no==record["student_no"] and isbn_no==record["ISBN"]]
        date=date_list[-1]
        return self.book_return_date(date)

         

#!StudentProcesses nesnesi oluşturma
student_processesp=StudentProcesses()                                        

#!StudentStatistics nesnesi oluşturma
student_istatisitc=StudentStatistics()


#!BookProcesses nesnesi oluşturma
book_processes=BookProcesses()

#!LibraryBookStatistics nesnesi oluşturma 
book_statistic=BookStatistics() 

#!öğrenci nesnesi oluşturma
s1=Student("Tuna Can","Asdca","200678")
s2=Student("Guzide","Alaca","232371")
s3=Student("Hakan","Aweca","234438")
s4=Student("Fatih","Konakli","454667")
s5=Student("Halime","Demir","345678")

#!book nesnesi oluşturma 
b1=Book("The Cat in the Hat","Dr. Seuss","978-1-317-80275-8")
b2=Book("Where the Crawdads Sing","Delia Owens","978-1-359-16196-5")
b3=Book("The Naked Ape","Desmond Morris","978-0-395-17632-7")
b4=Book("Charlie and the Chocolate Factory","Roald Dahl","978-1-174-61082-8")
b5=Book("The Secret","Rhonda Byrne","978-2-512-33897-7")
b6=Book("Uncle Styopa ","Sergey Mikhalkov","978-0-722-55764-4")
b7=Book("The Godfather","Mario Puzo","978-0-542-59134-4")
b8=Book("Love Story","Erich Segal","978-4-812-53766-9")
b9=Book("Catching Fire","Suzanne Collins","978-4-327-61629-6")
b10=Book("Mockingjay","Suzanne Collins","978-1-485-79508-1")

#!LibraryBookStudentProcesses nesneni oluşturma ödünç alma ve iade etme işlemleri
lbsp=LibraryBookStudentProcesses()





#---------------StudentProcesses class metodları ve kullanımı-------------

#!registered_students listesine öğrenci ekleme
#ls.add_student(s1)

#!registered_students listesinden öğrenci silme
#ls.remove_student(s1.student_no)      



#----------------LibraryBookStatistics class metodları ve kullanımı-----------
#!list_books -> tüm kitaplar(total_list) yazar adı:kitap adı şeklinde listeler
#bs.list_books()


#!get_books_for_book_name-> kitap isbnNo dan kitap ile ilgili özellikler
#bs.get_books_for_book_isbNo("isbn")

#!sort_for_book_name -> tüm kitap isimlerini alfabetik sıraya göre listler  author:book_name
#bs.sorted_for_book_name()

#!sort_for_author_name-> tüm yazar isimlerini alfabetik sıraya göre listeler author:book_name 
#bs.sorted_for_author_name()

#!get_grade_book-> kitap isbn_no suna göre kitabın puanını(ödünç alınma sayısını) döner
#bs.get_grade_book("isbn_no")


#!kitapları kayıt tarihine göre listeler
#bs.sorted_for_record_date_time()


#----------------DeliveryTrackingSystem class metdoları ve kullanımı----------



#----------------BookProcesses class metodları ve kullanımı-------------------------
#!add_book metodu -> total_list listesine kitap ekle
#lb.add_book(b1)                   

#!remove_book ->  total_list ten kitap sil 
#lb.remove_book("978-6-916-53439-0")


#-----------------LibraryBookStudentProcesses class metodları ve kullaınımı------------------
#!borrow_book -> öğrenci  kitap ödünç alır
#1.durum : kayıtlı bir öğrenci kayıtlı bir kitap alsın
#s1=Student("","","")
#b1=Book("Harry Potter and the Goblet of Fire","J. K. Rowling","978-3-113-74634-5")
#lb.borrow_book(b1,s1,"03-06-2024")


#lbsp.return_book(b1,s,"06-10-2024")
#lbsp.return_book(b2,s,"06-11-2024")
#lbsp.return_book(b3,s,"06-12-2024")

#2.durum: kayıtlı olamayan bir  öğrenci mevcut bir kitap alsın
#s1=Student("","","")
#b1=Book("Harry Potter and the Goblet of Fire","J. K. Rowling","978-3-113-74634-5")
#lb.borrow_book(b1,s1,"03-06-2024")

#3.durum: kayıtlı bir öğrenci kayıtlı olamyan bir kitap alsın 
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.borrow_book(b1,s1,"03-06-2024")

#4.durum: kayıtlı olmayan bir öğrenci kayıtlı olmayan bir kitap alsın 
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.borrow_book(b1,s1,"03-06-2024")


#!return_book-> kitap iade eder
#1.durum: kayıtlı bir öğrenci kayıtlı bir kitabı iade etsin
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.return_book(b1,s1,"03-06-2024")

#2.durum: kayıtlı bir öğrenci kayıtlı olmayan bir kitabı iade etsin
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.return_book(b1,s1,"03-06-2024")

#3.durum: kayıtlı bir öğrenci return_book listesinden bir kitabı iade etsin
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.return_book(b1,s1,"03-06-2024")

#4.durum: kayıtlı bir öğrenci borrow_list listesinden bir kitap iade etsin
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.return_book(b1,s1,"03-06-2024")

#5.durum: kayıtlı bir öğrenci borrow_listte olmayıp current_book_liste olan yani daha önce ödünç alınmamış bir kitabı iade etmeye çalışsın
#s1=Student("","","")
#b1=Book("","","978-3-113-705")
#lb.return_book(b1,s1,"03-06-2024")









