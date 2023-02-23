class Main {
    public static void main(String[] args) {
        String s = "PRA12Ga782d45601$3";
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                sum += (s.charAt(i) - '0');
            }
        }
        System.out.println(sum);
    }
}