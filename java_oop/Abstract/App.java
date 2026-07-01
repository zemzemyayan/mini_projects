package Abstract;

public class App {
    public static void main(String[] args) {

        Toyota toyota1 = new Toyota();
        Mercedes mercedes1 = new Mercedes();
        toyota1.motorBeygirGucu();
        toyota1.benzinTuketimMiktari();
        toyota1.motorhacmi();
        toyota1.degisenRenk();

        mercedes1.benzinTuketimMiktari();
        mercedes1.motorBeygirGucu();
        mercedes1.motorhacmi();
        mercedes1.akilliKoltuk();

    }
}
