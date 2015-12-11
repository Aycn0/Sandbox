class test{
    public static void main (String args[])
    throws java.io.IOException {
        System.out.println("pick a number: ");
        int num = System.in.read();
        int i;
        for (i = num; i < 10; i++) {
            System.out.println(i);
        }
    }
}