import java.io.*;

class myException extends Exception {
  public myException(String str) {
    // Calling constructor of parent Exception
    super(str);
  }
}

public class File {

  // function to check if person is eligible to vote or not

  // main method
  public static void main(String args[]) {
    try {

      throw new myException("Hello Akshay File Not Found");
    } catch (myException e) {
      System.out.println(e.getMessage());
    }
    System.out.println("rest of the code...");
  }
}