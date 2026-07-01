package OOP_uygulama1;

public class App {

    public static void main(String[] args) {
        Ogrenci ogr_1 = new Ogrenci();

        ogr_1.setIsimVer("zemzem");
        ogr_1.setSoyAdVer("yayan");
        ogr_1.setOkulNoVer("404715");
        ogr_1.setYasVer("22");
        System.out.println("ogrenci bilgileri : ");
        System.out.println("isim :" + ogr_1.getIsım());
        System.out.println("soyisim:" + ogr_1.getSoyIsım());
        System.out.println("okulno:" + ogr_1.getIsım());
        System.out.println("yas:" + ogr_1.getYas());
    }

}
