
class Car
{
    public void start(){System.out.println("Car is started");}
    public void accelerate(){System.out.println("Car is accelerated");}
    public void changeGear(){System.out.println("Car is changed");}
}

class LuxuryCar extends Car{
    public void changeGear(){System.out.println("Autogear");}
    public void openRoof(){System.out.println("Sun Roof is opened");}
}

public class Overriding {
    public static void main(){
        Car c = new LuxuryCar();
        c.start();
        c.accelerate();
        c.changeGear();
        c.openRoof();
    }    
}
