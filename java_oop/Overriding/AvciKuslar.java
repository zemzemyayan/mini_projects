package Overriding;

public class AvciKuslar extends Kuslar {
    protected boolean keskinGagaVarmi;
    protected boolean ayakPerdesiVarMi;
    protected boolean pencesiVarMi;

    protected void hareket() {
        System.out.println("avci kuslar yuksek irtifada genis kanat ozellikleri sayesinde hareket ederler ");
    }

    protected void beslenme() {
        System.out.println("avcı kuslar et ile beslenirler");
    }
}
