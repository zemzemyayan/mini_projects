package Linkd_List_ogrenci_kayit_uygulamasi;

public class Ogrencidugum {
    int numara;
    String Ad;
    String Soyad;
    int vize;
    int fin;
    double ortalama;
    String durum;
    Ogrencidugum sonraki;

    public Ogrencidugum(int numara, String ad, String soyad, int vize, int fin) {
        this.numara = numara;
        this.Ad = ad;
        this.Soyad = soyad;
        this.vize = vize;
        this.fin = fin;

        ortalama = vize * 0.4 + fin * 0.6;
        if (ortalama >= 50) {
            this.durum = "gecti";
        } else {
            this.durum = "kaldi";
        }

        this.sonraki = null;
    }

    public void OgrenciBilgileri() {
        System.out.println("---------------------------------------");
        System.out.println(this.numara + " numarali ogernciye ait bilgiler: ");
        System.out.println("Ad -> " + this.Ad);
        System.out.println("Soyad -> " + this.Soyad);
        System.out.println("Gecme durumu -> " + this.durum);
        System.out.println("---------------------------------------");

    }

}
