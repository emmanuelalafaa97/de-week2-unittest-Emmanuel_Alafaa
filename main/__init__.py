import unittest

### Your Testing Task

## Once your class is ready, write **pytest tests** that check the following behaviors.

##> Remember: thorough testing is crucial, you should know the limitations of your system. 
#In real-world systems, poorly designed tests can lead to unreliable outcomes and in healthcare applications, that could literally be a matter of life and death.


class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise

    MIN_GLUCOSE_LEVEL = 50      # define minimum level glucse that realistically drop to

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        # TODO: initialize class attributes here
    
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance

        if glucose_level >= ArtificialPancreasSystem.MIN_GLUCOSE_LEVEL:
                  self.glucose_level = glucose_level
        else:
             self.glucose_level = ArtificialPancreasSystem.MIN_GLUCOSE_LEVEL

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        # TODO: increase glucose based on carbs eaten
        self.glucose_level += carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        # TODO: decrease glucose based on duration of exercise
        self.glucose_level -= duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.

        If glucose is too high** (above `target_glucose + tolerance`):
         - The system should `"deliver_insulin"`.
         - Decide the insulin dose based on how much above the target the glucose is.
         - After giving insulin, subtract the dose from the current glucose level.

        or 

        If glucose is too low** (below `target_glucose - tolerance`):
            - The system should `"warn_low_glucose"`.

         or If glucose is **within** the target range:
        - `"maintain"` (do nothing).

        > Return both the action name (`"deliver_insulin"`, `"warn_low_glucose"`, `"maintain"`)  
        > and the **new glucose level
        
        """
        # TODO: decide what to do if glucose is too high, too low, or stable
        max_glucose_level = self.target_glucose + self.tolerance
        low_glucose_level = self.target_glucose - self.tolerance

        if self.glucose_level > max_glucose_level:
           print(max_glucose_level, "is the Max allowable Glucose level which was exceeded by:", self.glucose_level - self.target_glucose)
           return "deliver_insulin as glucose level is:",  self.glucose_level
        

        elif self.glucose_level < low_glucose_level:
           print("low glucose")
           return "warn_low_glucose", self.glucose_level
        
        else:
           print("stable glucose levels")
           return "maintain as glucose level is:", self.glucose_level


         

 ### Example Usage (Once Implemented)
controller = ArtificialPancreasSystem(0, 1.0, 100, 10)
#controller.meal(40)
#controller.exercise(20)
#action, level = controller.predict_action()
#print(action, level)


### Starter Pytest code
class TestFactorial(unittest.TestCase):
    def test_glucose_increases_after_meal(system):
    #TODO
     """
       Test to confirm that Glucose increases after a meal:
      Feed the system a meal and verify `glucose_level` goes up. 
     """
     system.assertEqual(controller.meal(40), 20)

class TestFactorial(unittest.TestCase):
    def test_glucose_never_below_min(system):
    # TODO
     """
      Test to confirm that Glucose never drops below the minimum glucose level of 50
      After long exercise, `glucose_level` should not fall below your defined floor (e.g., 50). 
     """
     system.assertTrue(controller.glucose(50))

class TestFactorial(unittest.TestCase):
    def test_glucose_decreases_after_excercise(system):
    # TODO
      '''
        test to confirm that Glucose decreases after exercise**
        Simulate exercise and verify `glucose_level` goes down.
      '''
      system.assertEqual(controller.exercise(20), 6)
        


### Core Tests


 

