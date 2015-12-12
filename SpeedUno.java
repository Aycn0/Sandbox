// This program is a score card for tracking points in Speed Uno
import java.util.Scanner;

public class Player {
    String playerName;
    int playerScore;
}

class SpeedUno {
    public static void main (String args[]) {
        
        // This determines how many players there are via user input.
        Scanner reader = new Scanner(System.in);
        System.out.println("How many players are there?");
        int numofplayers = reader.nextInt();
        System.out.println("There are " + numofplayers + " players.");
        
        // Gets player names from user.
        for (int i = 0; i < numofplayers; i++) {
            System.out.println("What is player " + i + "'s name?");
            Player reader.next() = new Player();
        }
    }
}