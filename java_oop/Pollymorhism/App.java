package Pollymorhism;

public class App {
    public static void main(String[] args) {
        Toyota toyota1 = new Toyota();
        toyota1.motor();
        toyota1.yakit();
        System.out.println("----------------------------------------");

        ToyotaBenzinli toyotaBenzinli1 = new ToyotaBenzinli();
        toyotaBenzinli1.motor();
        toyotaBenzinli1.yakit();
        toyotaBenzinli1.yakit(5.7);
        System.out.println("----------------------------------------");

        ToyotaDizel toyotaDizel1 = new ToyotaDizel();
        toyotaDizel1.motor();
        toyotaDizel1.yakit();
        toyotaDizel1.yakit("pembe");
        System.out.println("----------------------------------------");

        ToyotaElektirikli toyotaelektirkli1 = new ToyotaElektirikli();
        toyotaelektirkli1.motor();
        toyotaelektirkli1.yakit();
        System.out.println("----------------------------------------");

        CarSeller carseller1 = new CarSeller();
        carseller1.motor();
        carseller1.yakit("Q-V4V");
        carseller1.yakit(2022);
        carseller1.yakit(4.7);
        System.out.println("----------------------------------------");

        Toyota toyotaBenzinli2 = new ToyotaBenzinli();
        toyotaBenzinli2.motor();
        toyotaBenzinli2.yakit();
        toyotaBenzinli2.merhaba();
        System.out.println("----------------------------------------");

        Toyota toyotaDizel2 = new ToyotaDizel();
        toyotaDizel2.yakit();
        toyotaDizel2.motor();
        toyotaDizel2.merhaba();
        System.out.println("----------------------------------------");

        Toyota toyotaElektirikli2 = new ToyotaElektirikli();
        toyotaElektirikli2.motor();
        toyotaElektirikli2.yakit();
        toyotaElektirikli2.merhaba();

    }
}
