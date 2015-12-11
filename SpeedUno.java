// This program is a score card for tracking points in Speed Uno
import java.io.IOException;
import java.util.Scanner;

class newPlayer {
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
        int i;
        for (i < numofplayers; i = 0; i++) {
            System.out.println("Test");
        }
    }
}