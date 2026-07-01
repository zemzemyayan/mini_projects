package CiftBagliDL_Musteri_Kayit_Uygulamasi;

import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        MusteriListe liste = new MusteriListe();
        int secim = -1;
        while (secim != 0) {

            System.out.println("1-> musteri ekle                ");
            System.out.println("2-> musteri sil                 ");
            System.out.println("3-> musteri bilgisini guncelle  ");
            System.out.println("4-> musteri ara                 ");
            System.out.println("5-> musterileri listele         ");
            System.out.println("0-> cikis                       ");
            System.out.println("seciminiz:                      ");
            secim = sc.nextInt();

            switch (secim) {
                case 1:
                    liste.musteriEkle();
                    break;
                case 2:
                    liste.musteriSil();
                    break;
                case 3:
                    liste.musteriGuncelle();
                    break;
                case 4:
                    liste.musteriAra();
                case 5:
                    liste.musteriListele();
                case 0:
                    System.out.println("cikis yaptiniz..");
                    break;
                default:
                    System.out.println("hatali secim yaptiniz [1-5]");
                    break;

            }
        }

        sc.close();

    }
}
