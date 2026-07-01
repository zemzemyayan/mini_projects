package Abstract;

public abstract class Arabalar {
    /*
     * abstract bir araba class’ı oluşturalım ve içine her arabada olması gereken
     * fonksiyonları, //!abstract metod olarak ekleyelim(ki arabalar classını extend
     * edicek her classta bu metodlar ZORUNLU overriding edilmiş olsun ).
     * Ayrıca diğer alt sınıflar
     * için zorunlu kılmak istediğimiz daha farklı fonksiyonlar da varsa, bunları
     * abstract olmayacak şekilde ekleyelim. Ve daha sonra bu metotlardan
     * istediğimizi alt
     * class’larda override ederek kullanalım.
     * //! abstract olarak tanımlanan metodların bir bodysi yoktur bodyleri
     * ovveriding edilen classlarda class ihitiyacına göre doldurulacaktır
     * 
     */

    // mesela her arabda olması gereken ozellikler neler olabilir :
    // hiz motorhacmi vites motorBeygirGucu bu metodlar abstarct metod olarak
    // eklenecek

    // ilgili araba ne kadar benzinle gider
    public abstract void benzinTuketimMiktari();

    // ilgii arabanın motorhacmi ne kadar
    public abstract void motorhacmi();

    // ilgli arabanın motor beygir gucu ne kadar
    public abstract void motorBeygirGucu();

    // ilgili araba ne kadar hıza ulaşabilir
    public abstract void hiz();

    // istediğim araçta olmasını isteycegim abstarct olmayan bazı metodlar yani bazı
    // opsiyonlar
    // opsiyonlar belli araçlar uzerine gelen metodlardır
    // otomatikTanıma akıllıkoltuk değişebilirenek

    public void otomatikTanima() {
        System.out.println("aracta dış dunyayı otomatik tanıma opsiyonu mevcuttur .");
    }

    public void akilliKoltuk() {
        System.out.println("aracta oturuşunuza göre ayarlanabilir akıllı koltuk opsiyonu mevcuttur ");
    }

    public void degisenRenk() {
        System.out.println("aracta hava efektine göre renk değiştirebilme opsiyonu mevcuttur ");
    }

}
