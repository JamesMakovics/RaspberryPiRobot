

public class motorMethods implements InitRobot{

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

}
