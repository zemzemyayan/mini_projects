package Linkd_List_ogrenci_kayit_uygulamasi;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        int secim = -1;
        OgrenciListe liste1 = new OgrenciListe();
        Scanner sc = new Scanner(System.in);

        while (secim != 0) {
            System.out.println();
            System.out.println("Bilgisayar bolumune ogrenci kayit uygulmasi ");
            System.out.println("1- yeni kayit");
            System.out.println("2- kayit sil");
            System.out.println("3- kayitlari listele");
            System.out.println("4- en basarili ogrenci ");
            System.out.println("0- cikis");
            System.out.println();
            System.out.println();
            System.out.println("seciminiz-> ");
            secim = sc.nextInt();

            if (secim == 1) {
                liste1.OgrenciEkle();
            } else if (secim == 2) {
                liste1.Ogrencisil();
            } else if (secim == 3) {
                liste1.listele();

            } else if (secim == 4) {
                liste1.enBasariliOgrenci();
            } else if (secim == 0) {
                System.out.println("program sonlandirildi");
            } else {
                System.out.println("hatali giris yaptiniz 1-4 ");
            }

        }

        sc.close();

    }
}
