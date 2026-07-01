package KisilikTesti;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws FileNotFoundException {

        int sayac = 1;
        File f = new File("C:\\Users\\HP\\Desktop\\java\\KisilikTesti\\Sorular");
        Scanner scFile = new Scanner(f);
        Scanner scCevap = new Scanner(System.in);
        String isim;
        System.out.println("merhaba isminiz nedir :");
        isim = scCevap.nextLine();
        // hasNext dosaydan okunacak veri oldugu sürece
        while (scFile.hasNext()) {
            String str = scFile.nextLine();
            System.out.println(str);
            System.out.println(sayac + ".soruya karsilik cevabiniz :");
            String cevap = scCevap.nextLine();
            System.out.println();
            harfIndexNumarasi(cevap, isim);
            System.out.println();
            sayac++;
        }

    }

    public static void harfIndexNumarasi(String cevap, String isim) {
        char[] alfabe = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                'u', 'v', 'y', 'z' };
        boolean[] indexCharry = new boolean[alfabe.length];
        for (int i = 0; i < indexCharry.length; i++) {
            indexCharry[i] = false;
        }

        ArrayList<Integer> indexList = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i < cevap.length(); i++) {
            for (int k = 0; k < alfabe.length; k++) {
                if (cevap.charAt(i) == alfabe[k]) {
                    indexList.add(i);
                }
            }
        }

        boolean state = false;
        for (int i = 0; i < indexList.size(); i++) {
            int random = rand.nextInt(1, alfabe.length);
            if (indexList.get(i) == random) {
                indexCharry[i] = true;
                state = true;
            }
        }

        if (state) {
            System.out.println("sevgili " + isim
                    + " bu soruya karsilik verdigin cevabin arasindan bazi harfler özel harfler bu harflerin alfabedeki rakamsal karsiligi söyle : ");
        }
        for (int i = 0; i < indexCharry.length; i++) {
            if (indexCharry[i] == true) {
                System.out.println(i + " rakami ve " + alfabe[i] + " harfi ");
            }
        }

    }

}
