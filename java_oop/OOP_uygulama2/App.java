package OOP_uygulama2;

import java.util.ArrayList;

public class App {

    public static void main(String[] args) {
        ArrayList<String> dersler = new ArrayList<>();
        dersler.add("matematik");
        dersler.add("kimya");
        dersler.add("fiizk");
        dersler.add("biyoloji");
        Ogrenci ogr1 = new Ogrenci("zemzem", "yayan", "2001", dersler);

        System.out.println(ogr1.bilgilerGoruntule());

    }

}
