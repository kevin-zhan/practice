import java.util.ArrayList;

/**
 * Created by kevin on 16/4/27.
 */
public class Practice1 {
    public int factorial(int n) {
        // Happy coding :-)
        if (n <= 12 && n >= 0){
            int result = 1;
            for(int i = 1;i<n;i++){
                result *= i;
            }
            return result;
        }
        throw new IllegalArgumentException();
    }

    public static int sortDesc(final int num) {
        //Your code
        int[] array = new int[10];
        for (int i=0;i<array.length;i++){
            array[i] = 0;
        }
        for (int i=1;i<=num;i*=10){
            int index = num/i%10;
            array[index]++;
        }
        int result = 0;
        int temp = 1;
        for (int i=0;i<array.length;i++){
            for (int j=0;j<array[i];j++){
                result += i*temp;
                temp *= 10;
            }
        }
        return result;
    }
    public static void main(String[] a){
        //System.out.println(sortDesc(12345664));
        System.out.println(sortDesc(11547));

    }
}
