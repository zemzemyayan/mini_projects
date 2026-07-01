package Projects;

import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        /*
         * 
         * Çin zodyağı hesaplanırken kişinin doğum yılının 12 ile bölümünde kalana göre
         * bulunur.
         * 
         * Doğum Tarihi %12 = 0 ➜ Maymun
         * 
         * Doğum Tarihi %12 = 1 ➜ Horoz
         * 
         * Doğum Tarihi %12 = 2 ➜ Köpek
         * 
         * Doğum Tarihi %12 = 3 ➜ Domuz
         * 
         * Doğum Tarihi %12 = 4 ➜ Fare
         * 
         * Doğum Tarihi %12 = 5 ➜ Öküz
         * 
         * Doğum Tarihi %12 = 6 ➜ Kaplan
         * 
         * Doğum Tarihi %12 = 7 ➜ Tavşan
         * 
         * Doğum Tarihi %12 = 8 ➜ Ejderha
         * 
         * Doğum Tarihi %12 = 9 ➜ Yılan
         * 
         * Doğum Tarihi %12 = 10 ➜ At
         * 
         * Doğum Tarihi %12 = 11 ➜ Koyun
         * 
         * 
         * 
         * 
         */

        Scanner scanner = new Scanner(System.in);

        System.out.print("Yılı girin: ");
        int year = scanner.nextInt();

        boolean state = false;

        if (year % 4 == 0) {
            if (year % 100 != 0 || year % 400 == 0) {
                state = true;
            }
        }

        if (state) {
            System.out.println(year + " bir artık yıldır.");
        } else {
            System.out.println(year + " bir artık yıl değildir.");
        }

        scanner.close();

    }

}
