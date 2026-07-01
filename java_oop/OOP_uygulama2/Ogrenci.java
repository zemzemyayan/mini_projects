package OOP_uygulama2;

import java.util.ArrayList;

// shift + alt + o
public class Ogrenci {

    private String isim;
    private String soyIsim;
    private String dogumYil;
    // private int numara;
    private ArrayList<String> dersler;

    public Ogrenci() {

    }

    public Ogrenci(String _isim, String _soyIsım, String _dogumYil, ArrayList<String> _dersler) {
        this.isim = _isim;
        this.soyIsim = _soyIsım;
        this.dogumYil = _dogumYil;
        // this.numara = _okulNo;
        this.dersler = _dersler;

    }

    public String bilgilerGoruntule() {
        return "isim->  " + this.isim + "  soyisim->  " + this.soyIsim + "  dogumyil->  " + this.dogumYil
                + "  dersler->"
                + this.dersler;
    }

}
