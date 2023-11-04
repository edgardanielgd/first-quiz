package org.velezreyes.quiz.question6;

public class VendingMachineImpl {

  // Instantiate drinks
  public static Drink instantiateScottColaDrink() {
    return new Drink() {

      public String getName() {
        return "ScottCola";
      }

      public boolean isFizzy() {
        return true;
      }
    };
  }

  public static Drink instantiateKarenTeaDrink() {
    return new Drink() {

      public String getName() {
        return "KarenTea";
      }

      public boolean isFizzy() {
        return false;
      }
    };
  }

  public static VendingMachine getInstance() {
    return new VendingMachine() {

      private int money;

      public void insertQuarter() {
        money += 25;
      }

      public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

        switch (name) {
          case "ScottCola": {
            if (money < 75)
              throw new NotEnoughMoneyException();

            money -= 75;
            return instantiateScottColaDrink();
          }

          case "KarenTea": {
            if (money < 100)
              throw new NotEnoughMoneyException();

            money -= 100;
            return instantiateKarenTeaDrink();
          }

          default:
            throw new UnknownDrinkException();
        }

      }
    };
  }
}
