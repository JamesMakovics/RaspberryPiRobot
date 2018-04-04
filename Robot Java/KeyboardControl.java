

public class KeyboardControl implements InitRobot{

    public static void moveForward(){
        leftMotorForward.on();
        rightMotorForward.on();
        leftMotorBackward.off();
        rightMotorBackward.off();
    }
    public static void moveBackward(){
        leftMotorBackward.on();
        rightMotorBackward.on();
        leftMotorForward.off();
        rightMotorForward.off();
    }
    public static void moveLeft(){
        rightMotorForward.on();
        leftMotorForward.off();
        leftMotorBackward.off();
        rightMotorBackward.off();
    }
    public static void moveRight(){
        rightMotorForward.off();
        leftMotorForward.on();
        leftMotorBackward.off();
        rightMotorBackward.off();
    }
    public static void stop(){
        rightMotorForward.off();
        leftMotorForward.off();
        leftMotorBackward.off();
        rightMotorBackward.off();
    }

void keyPressed() {
  final int k = keyCode;

  if (k == ' ' | k == ENTER | k == RETURN)

  else setDirection(k, true);
}

void keyReleased() {
  setDirection(keyCode, false);
}

static final void setDirection(int k, boolean decision) {
  if      (k == UP    | k == 'W')   moveForward();
  else if (k == DOWN  | k == 'S')   moveBackward();
  else if (k == LEFT  | k == 'A')   moveLeft();
  else if (k == RIGHT | k == 'D')   moveRight();
  else stop();
}

}
