package Projects;

import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        /*
         * Sıcaklık 5'dan küçük ise "Kayak" yapmayı öner.
         * Sıcaklık 5 ve 15 arasında ise "Sinema" etkinliğini öner.
         * Sıcaklık 15 ve 25 arasında ise "Piknik" etkinliğini öner.
         * Sıcaklık 25'ten büyük ise "Yüzme" etkinliğini öner.
         */
        Scanner sc = new Scanner(System.in);

        System.out.println("1.sayi giriniz:");
        int deger1 = sc.nextInt();
        System.out.println("2.sayi giriniz:");
        int deger2 = sc.nextInt();
        System.out.println("3.sayi giriniz:");
        int deger3 = sc.nextInt();
        int enbuyuk1 = 0;
        int enbuyuk2 = 0;
        int enbuyuk3 = 0;
        if (deger1 > deger2 && deger1 > deger3) {
            enbuyuk1 = deger1;
            if (deger2 > deger3) {
                enbuyuk2 = deger2;
                enbuyuk3 = deger3;
            } else if (deger3 > deger2) {
                enbuyuk2 = deger3;
                enbuyuk3 = deger2;
            }
        } else if (deger2 > deger1 && deger2 > deger3) {
            enbuyuk1 = deger2;
            if (deger1 > deger3) {
                enbuyuk2 = deger1;
                enbuyuk3 = deger3;
            } else if (deger3 > deger1) {
                enbuyuk2 = deger3;
                enbuyuk3 = deger1;
            }
        } else if (deger3 > deger2 && deger3 > deger1) {
            enbuyuk1 = deger3;
            if (deger1 > deger2) {
                enbuyuk2 = deger1;
                enbuyuk3 = deger2;
            } else if (deger2 > deger1) {
                enbuyuk2 = deger2;
                enbuyuk3 = deger1;
            }
        }

        System.out.println("siralama: " + " " + enbuyuk1 + " " + enbuyuk2 + " " + enbuyuk3);

        sc.close();
    }
}
