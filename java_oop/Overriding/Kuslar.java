package Overriding;

public class Kuslar extends Hayvanlar {

    protected boolean gagasiVarMi;
    protected boolean kanadiVarMi;

    protected void ureme() {
        System.out.println("kuslar yumurtlayarak ureme yapar");
    }

    protected void solunum() {
        System.out.println("kuslar akciger solunumı yaparlar ");
    }

}
