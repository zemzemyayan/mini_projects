package OOP_uygulama1;

public class Ogrenci {
    // ogrenci classı olıştu
    // get set constructur metodlarını yaz
    private String isim;
    private String soyAd;
    private String okulNo;
    private String yas;
    public static int deger;

    // set metodalrı :
    public void setIsimVer(String _isim) {
        this.isim = _isim;
    }

    public void setSoyAdVer(String _soyAd) {
        this.soyAd = _soyAd;
    }

    public void setOkulNoVer(String _okulNo) {
        this.okulNo = _okulNo;
    }

    public void setYasVer(String _yas) {
        this.yas = _yas;
    }

    // get metodları .

    public String getIsım() {
        return this.isim;
    }

    public String getSoyIsım() {
        return this.soyAd;
    }

    public String getOkulNo() {
        return this.okulNo;
    }

    public String getYas() {
        return this.yas;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString();
    }

}
