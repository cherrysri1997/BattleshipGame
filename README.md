# BattleshipGame


## Assumptions made in this game are as follows:
  * The game will not begin without the two players entering their name
  * The game will not begin without the two players setting their fleet on their boards
  * Before beginning the game to choose a player to begin firing, a tossing system is used, which is ODD/EVEN (like in childhood). The first player to enter gets the chance to choose ODD/EVEN and then both the users are asked to choose an integer between 1 and 10, inclusive. And based on the sum of the inputs, the player to begin firing is decided.
  * As the Game Loop begins, each user gets their turn on an alternative basis.
  * Every time a player gets his/her turn to fire a missile on the opponent's fleet, they are provided with two options:
    1.  (1) - To print the current status of the player's board and the opponent's board. (Opponent's board is abstracted in such a way that only hits and misses are shown, not the ships)
    2.  (2) - To fire a missile at a particular cell on the opponent's board
  * In the above step, if a player chooses (2), then the input format for firing at a cell on the opponent's fleet is: [A-J][1-10]. Each of the part is interpreted as follows:
    1.  [A-J]  ->  Address of a row on the board
    2.  [1-10] ->  Address of a column on the board
  * The representation of cells based on different conditions are assumed as follows:
    1.  "  _  "  ->  Cells which are yet to be fired at
    2.  "  !  "  ->  Cells which are fired but is a MISS
    3.  "  ^  "  ->  Cells which are fired and is a HIT
  * Each of the five ships are represented by a unique alphabet on the board as follows:
    1.  CARRIER    ->  C
    2.  BATTLESHIP ->  B
    3.  CRUISER    ->  R
    4.  SUBMARINE  ->  S
    5.  DESTROYER  ->  D
  * While setting the fleet on a board, player is prompted with input format like: [A-J][1-10][0-1]. Each one is interpreted as follows:
    1.  [A-J]  ->  Address of a row on the board
    2.  [1-10] ->  Address of a column on the board
    3.  [0-1]  ->  If the player wants to place a ship horizontally (i.e., along a row), then he/she is supposed to choose 0, else if the player wants to place a ship vertically (i.e., along a column) then he/she is aupposed to choose 1
  * In the above step, if a player wants to align a ship along a row then he/she has to enter the cell address of the left-most cell (suppose a player wants to place a CARRIER (size - 5) on board as follows: J5, J6, J7, J8, J9, then the input to be given for such arrangement is J50, here J represents the row, 5 represents the column and 0 represents that the J5 is the left-most cell to begin the horizontal alignment with)
  * In the above step, if a player wants to align a ship along a column then he/she has to enter the cell address of the top-most cell (suppose a player wants to place a CARRIER (size - 5) on board as follows: F10, G10, H10, I10, J10, then the input to be given for such arrangement is F101, here F represents the row, 10 represents the column and 1 represents that the F10 is the top-most cell to begin the vertical alignment with)
  * Players will be prompted in case of a wrong input, at all stages of the gameplay.
  * Until all the 5 ships of at least 1 player are destroyed, the game loop continues.
  * The game loop breaks as soon as a player loses all of his/her 5 ships.
  * The console output is printed into a PDF and uploaded with the name [output_console.pdf](https://github.com/cherrysri1997/BattleshipGame/blob/master/output_console.pdf). Please refer it for the output of whole gameplay.
  * I managed to generate an executable file for the project. [executable](https://github.com/cherrysri1997/BattleshipGame/tree/master/output/main).
  * At the end of the game WINNER will be announced and all the moves made by both the players will be displayed in order.

### Additional Requirements:
Further, to answer the question: **Explain how will you extend your design to
allow people to play over the network (p2p without having a central server).**

Since we don't want to have a central server, then the idea would be is to make one of the player's device, a server and the other one, a client.
And then create a link for a game share it to the opponent and challenge.

Another idea is to enable the hotspot/bluetooth on one device and getting opponent's device connected to it, so that they are in the same network.
Then connection provider is considered a server and connection seeking device as a client. For this to happen both the devices are supposed to be within a certain boundary and vicinity (like within a radius of 10 to 20 metres). Similar to Mini Militia.

