class Main {
    public static void main(String[] args) {
        String s = "PRA12Ga782d45601$3";
        int res_1 = method_1(s);
        int res_2 = method_2(s);
        System.out.println(res_2);
    }
    /*This method is for treating values as a single digit*/
    static int method_1(String s){
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') { //check it it a number or not
                sum += (s.charAt(i) - '0'); //sum the digits by converting (char) -> (int)
            }
        }
        return sum;
    }
    /*This method is for consecutive values as a digit*/
    static int method_2(String s){
        int ans = 0;
        int val = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!Character.isDigit(s.charAt(i))) { // check if it is a number or not
                // insert <val> into <ans> and then empty val for the next number
                ans += val;
                val = 0;
            }else{
                val = val * 10 + (s.charAt(i) - '0');
            }
        }
        return ans + val;
    }
}
