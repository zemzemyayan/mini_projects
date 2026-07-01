package Pollymorhism;

//import java.util.ArrayList;

public class ToyotaDizel extends Toyota {

    public void motor() {
        System.out.println("ToyotaDizel motor() metodu  ");
    }

    public void yakit() {
        System.out.println(" ToyotaDizel yakit() metodu ");
    }

    public void yakit(String _renk) {
        System.out.println("ToyotaDizel parametreli yakit(String renk) metodu");
        // ArrayList<String> mevcutRenkler = new ArrayList<String>();
        // mevcutRenkler.add("kırmızı");
        // mevcutRenkler.add("gri");
        // mevcutRenkler.add("beyaz");
        // mevcutRenkler.add("siyah");
        // mevcutRenkler.add("mavi");
        // mevcutRenkler.add("yeşil");

        // boolean state = true;
        // for (int i = 0; i < mevcutRenkler.size(); i++) {
        // state = mevcutRenkler.contains(_renk);
        // if (state) {
        // System.out.println("istenilen renkte toyota dizel mevcuttur ");
        // } else {
        // System.out.println("istenilen renkten toyota dizel araç mevcut degil");
        // }
        // }

    }
}
