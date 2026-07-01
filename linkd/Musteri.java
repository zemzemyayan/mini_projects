package CiftBagliDL_Musteri_Kayit_Uygulamasi;

public class Musteri {

    int id;
    String Ad;
    String Soyad;
    String tel;
    String adres;
    String urunBilgisi;

    Musteri onceki = null;
    Musteri sonraki = null;

    public Musteri(int id, String ad, String soyad, String tel, String adres, String urunad) {
        this.id = id;
        this.Ad = ad;
        this.Soyad = soyad;
        this.tel = tel;
        this.adres = adres;
        this.urunBilgisi = urunad;

        this.sonraki = null;
        this.onceki = null;
    }

    public void MusteriBilgileri() {
        System.out.println(this.id + " numarali musteriye ait bilgiler: ");
        System.out.println("Ad: " + this.Ad);
        System.out.println("Soyad: " + this.Soyad);
        System.out.println("telefon: " + this.tel);
        System.out.println("Adres: " + this.adres);
        System.out.println("Urun ismi: " + this.urunBilgisi);
    }

}
