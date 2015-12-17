// This program is a score card for tracking points in Speed Uno
import java.util.*;

class Player {
    public Player(String playerName) {
    String name = playerName;
    int playerScore;
    }
}

class SpeedUno {
    public static void main (String args[]) {
        
        // This determines how many players there are via user input.
        Scanner user_input = new Scanner(System.in);
        System.out.println("How many players are there?");
        int numofplayers = user_input.nextInt();
        System.out.println("There are " + numofplayers + " players.");
        
        // This creates the list for player storage
        ArrayList<Player> playerList = new ArrayList<Player>();
        
        // Gets player names from user.
        for (int i = 1; i <= numofplayers; i++) {
            System.out.println("What is Player " + i + "'s name?");
            String name = user_input.next();
            System.out.println("Player " + i + ": " + name);
            playerList.add(new Player(name));
            System.out.println(" ");
        }
    }
}