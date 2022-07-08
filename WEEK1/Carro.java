public class Carro extends Veiculo {
    private int cilindrada;
    private boolean airbag;

    public String toString() {
        return "... Fabricado em " + getAnoDeFabricacao() + " com " + cilindrada + " cilindradas!";
    }

    Carro (int ano, String modelo, String marca, int cilindrada) {
        super (ano, modelo, marca);
        this.cilindrada = cilindrada;
    }

    // tornar classe executável
    // método da linha de comando
    public static void main( String ars[]) {
        Carro fordBigode = new Carro(1910, "bigode", "Ford", 2900);
        System.out.println("O veiculo criado foi " + fordBigode + " .");
    }
}
