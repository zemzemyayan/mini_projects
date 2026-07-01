package Linkd_List_ogrenci_kayit_uygulamasi;

import java.util.Scanner;

public class OgrenciListe {

    Ogrencidugum head = null;
    Ogrencidugum tail = null;
    Ogrencidugum temp1 = null;
    // ogrenci listesi için ogrenci olusturmak gerekir dolayısıyla ogrenciye ait
    // bilgileri
    // tutacak olan değişkenler gerekir numara ad soyad..vs
    // eklenecek olan her ogrencinin asagıdaki bilgilere sahip olması gerekir
    int numara;
    String Ad;
    String Soyad;
    int vize;
    int fin;
    Scanner sc = new Scanner(System.in);

    public void OgrenciEkle() {

        // eklenecek ogrencinin bilgilerini kullanıcıdan alalım:
        System.out.println("eklemek istediginiz ogrencinin bilgilerini giriniz: ");
        System.out.print("numara-> ");
        numara = sc.nextInt();
        sc.nextLine();
        System.out.print("Ad-> ");
        Ad = sc.nextLine();
        System.out.print("SoyAd-> ");
        Soyad = sc.nextLine();
        System.out.print("Vize notu-> ");
        vize = sc.nextInt();
        System.out.print("Final notu-> ");
        fin = sc.nextInt();
        // girilen ogrenci bilgileriyle yeniOgr ogrenci olusturuldu:
        Ogrencidugum yeniOgr = new Ogrencidugum(numara, Ad, Soyad, vize, fin);
        if (head == null) {
            head = yeniOgr;
            tail = yeniOgr;
            System.out.println(yeniOgr.numara + " numarali ogrenci listeye eklendi ");
        } else {
            yeniOgr.sonraki = head;
            head = yeniOgr;
            System.out.println(yeniOgr.numara + " numarali ogrenci listeye eklendi ");
        }
    }

    public void Ogrencisil() {

        if (head == null) {
            System.out.println("listede ogrenci yoktur!!");
        } else {
            // silinecek olan ogrenci numarasıyla spesifik bir bilgi verilmesi şartı ile
            // silinebilir
            System.out.println("silmek istediginiz ogrencinin numarasini giriniz: ");
            int numara = sc.nextInt();
            // 1.durum silmek istenilen ogrenci listedeki ilk ve tek ogrenciyse
            if (head.numara == numara & head.sonraki == null) {
                head = null;
                tail = null;
                // 2.durum silmek istedginiz ogrenci listedeki ilk ogrenciyse
            } else if (head.numara == numara & head != null) {
                head = head.sonraki;
                System.out.println(numara + "numarali ogrenci silindi ");
            } else {
                Ogrencidugum temp = head;
                Ogrencidugum temp2 = head;
                // silmek istenilen ogrenci listenin herhangi bir yerindeyse
                while (temp.sonraki != null) {

                    if (temp.numara == numara) {
                        temp2.sonraki = temp.sonraki;
                        System.out.println(numara + "numarali ogrenci silindi ");
                    }
                    temp = temp.sonraki;
                }
                // ya da silmek istenilen ogrenci son ogrenciyse ki while dan sonra temp son
                // dugumde
                if (temp.numara == numara) {
                    temp2.sonraki = null;
                    tail = temp2;

                }

            }
        }

    }

    public void listele() {
        if (head == null) {
            System.out.println("listede ogrenci yoktur!");
        } else {
            Ogrencidugum temp = head;
            while (temp != null) {
                temp.OgrenciBilgileri();
                temp = temp.sonraki;
            }
        }
    }

    public void enBasariliOgrenci() {
        if (head == null) {
            System.out.println("listede ogrenci yok!");
        } else {
            Ogrencidugum temp = head;
            double enbuyuk_ortalama = temp.ortalama;
            while (temp != null) {
                if (enbuyuk_ortalama < temp.ortalama) {
                    enbuyuk_ortalama = temp.ortalama;
                    // listedeki ad soyad numara bilgilerini temsil eden değişkenlere
                    // en basarili ogrencinin ad soyad numara bilgilerini vericez
                    numara = temp.numara;
                    Ad = temp.Ad;
                    Soyad = temp.Soyad;
                    vize = temp.vize;
                    fin = temp.fin;

                }
                temp = temp.sonraki;
            }
            System.out.println("en basarili ogrenciye ait bilgiler ");
            System.out.println("Ad-> " + Ad);
            System.out.println("Soad-> " + Soyad);
            System.out.println("vize notu -> " + vize);
            System.out.println("final notu -> " + fin);

        }
    }

}
