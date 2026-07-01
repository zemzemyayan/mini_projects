package Overriding;

public class Hayvanlar {
    protected boolean gorurMu;

    protected void ureme() {
        System.out.println("her hayvan ortak ozellik olarak ureme ozelligine sahiptir");
    }

    protected void beslenme() {
        System.out.println("her hayvan ortak ozellik olarak beslnme ozellgine sahiptir");
    }

    protected void hareket() {
        System.out.println("her hayvan ortak ozellik olarak hareket etme ozelligine sahiptir");
    }

    protected void solunum() {
        System.out.println("her hayvan ortak ozellik olarak solunum yapma ozelligine sahiptir");
    }

}
