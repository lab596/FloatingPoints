import java.util.Scanner;
import java.util.ArrayList;
class Main {
  public static void main(String[] args) {
    System.out.println("Input either a base 10 or base 2 number to convert between them:");
    Scanner sc = new Scanner(System.in);
    int inp = sc.nextInt();
    String j = "" + inp;
    boolean larger = false;
    String fin = "";
    ArrayList<String> nums = new ArrayList<>();
    int a = 9;
    for(int q=a;q>2;q--){
      nums.add(""+a);
      a--;
    }
    
    for(int i = 0; i<j.length();i++){
      for(int y=0;y<nums.size();y++){
        if(j.substring(i,i+1).equals(nums.get(y))){
          fin = base_convert (""+inp, 10, 2);
          larger = true;
        }
      }
    }
    if(larger==false){
      fin = base_convert (""+inp, 2, 10);
    }
    System.out.print(fin);
  }
  public static String base_convert(String num, int source, int destination){
      return Integer.toString(Integer.parseInt(num, source), destination);
   }
}
