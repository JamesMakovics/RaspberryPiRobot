
public class robotControls  implements KeyListener {


    public void keyPressed(KeyEvent e) {
           // Invoked when a key has been pressed.
           if (e.getKeyCode() == KeyEvent.VK_W) {
                motorMethods.moveForward();
           }
           else if (e.getKeyCode() == KeyEvent.VK_A) {
                motorMethods.moveLeft();
           }
           else if (e.getKeyCode() == KeyEvent.VK_S) {
                motorMethods.moveBackward();
           }
           else if (e.getKeyCode() == KeyEvent.VK_D) {
                motorMethods.moveRight();
           }
       }

       public void keyReleased(KeyEvent e) {
           // Invoked when a key has been released.
           motorMethods.stop();
       }
}

//This was previous code that may be used later
// if      (k == UP    | k == 'W')   moveForward();
// else if (k == DOWN  | k == 'S')   moveBackward();
// else if (k == LEFT  | k == 'A')   moveLeft();
// else if (k == RIGHT | k == 'D')   moveRight();
// else stop();
