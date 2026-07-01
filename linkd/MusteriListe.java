package CiftBagliDL_Musteri_Kayit_Uygulamasi;

import java.util.Scanner;

public class MusteriListe {

    Scanner sc = new Scanner(System.in);

    Musteri head = null;
    Musteri tail = null;

    int id;
    String Ad;
    String Soyad;
    String tel;
    String adres;
    String urunBilgisi;

    public void musteriEkle() {
        System.out.println("eklenecek musteri bilgilerini giriniz: ");
        System.out.println("id numarasi: ");
        id = sc.nextInt();
        sc.nextLine();
        System.out.println("Ad         : ");
        Ad = sc.nextLine();
        System.out.println("Soyad      : ");
        Soyad = sc.nextLine();
        System.out.println("telefon    : ");
        tel = sc.nextLine();
        System.out.println("adres      : ");
        adres = sc.nextLine();
        System.out.println("urun ismi  :  ");
        urunBilgisi = sc.nextLine();

        Musteri yeni = new Musteri(id, Ad, Soyad, tel, adres, urunBilgisi);
        if (head == null) {
            head = yeni;
            tail = yeni;
            System.out.println("liste olsuturuldu ilk musteri listeye eklendi..");
        } else {
            yeni.sonraki = head;
            head.onceki = yeni;
            head = yeni;
            System.out.println(id + "numarali musteri listeye eklendi..");
        }

    }

    public void musteriSil() {

        boolean state = false;
        if (head == null) {
            System.out.println("liste bostur!");
        } else {
            System.out.println("silinecek olan musterinin id numarasini giriniz: ");
            id = sc.nextInt();
            sc.nextLine();
            // 1.durum silinicek musteri listedeki tek (dolayısıyla ilk) musteri ise
            if (head.sonraki == null & head.id == id) {
                head = null;
                tail = null;
                System.out.println(id + " numarali musteri listeden silindi..");
                state = true;
            }
            // 2.durum listede birden fazla musteri var ve ilk musteriyi silmek istersek
            else if (head.sonraki != null & head.id == id) {
                head = head.sonraki;
                head.onceki = null;
                System.out.println(id + " numarali musteri listeden silindi..");
                state = true;

            }
            // 3.durum silinecek musteri listenin sonundaki musteri ise
            else if (tail.id == id) {
                tail = tail.onceki;
                tail.sonraki = null;
                System.out.println(id + " numarali musteri listeden silindi..");
                state = true;
            }
            // 4.durum aradan musteri silmek istersek
            else {
                Musteri temp = head;
                while (temp != null) {
                    if (temp.id == id) {
                        temp.sonraki.onceki = temp.onceki;
                        temp.onceki.sonraki = temp.sonraki;
                        System.out.println(id + " numarali musteri listeden silindi..");
                        state = true;
                        break;
                    }
                    temp = temp.sonraki;
                }
            }
            if (state == false) {
                System.out.println(id + " numarali musteri listede yoktur!");
            }

        }

    }

    public void musteriGuncelle() {

        boolean state = false;
        if (head == null) {
            System.out.println("liste bostur! ");
        } else {
            System.out.println("Guncellenecek olan musterinin id numarasi :");
            id = sc.nextInt();
            sc.nextLine();
            Musteri temp = head;
            while (temp != null) {
                if (temp.id == id) {
                    temp.MusteriBilgileri();
                    System.out.println("Urun bilgisini Guncelle :");
                    temp.urunBilgisi = sc.nextLine();
                    System.out.println("urun bilgisi guncellendi ");
                    state = true;
                    break;
                }
                temp = temp.sonraki;
            }
        }
        if (state == false) {
            System.out.println(id + " numarali musteri listede yoktur ");
        }
    }

    public void musteriAra() {

        boolean state = false;
        if (head == null) {
            System.out.println("liste bostur! ");
        } else {
            System.out.println("Aradiginiz musteriye ait id numarasi: ");
            id = sc.nextInt();
            sc.nextLine();

            Musteri temp = head;
            while (temp != null) {
                if (temp.id == id) {
                    temp.MusteriBilgileri();
                    state = true;
                    break;
                }
                temp = temp.sonraki;
            }

        }

        if (state == false) {
            System.out.println(id + " numarali musteri listede yoktur!");
        }
    }

    public void musteriListele() {

        if (head == null) {
            System.out.println("liste bostur!");
        } else {
            Musteri temp = tail;
            while (temp != null) {
                temp.MusteriBilgileri();
                temp = temp.onceki;
            }
        }
    }

}
