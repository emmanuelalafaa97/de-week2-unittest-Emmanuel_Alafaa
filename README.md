# de-week2-unittest-Emmanuel_Alafaa
## Unittesting


# Artificial Pancreas System (Prototype)

A simplified, data-driven simulation of glucose regulation using Python.
This project models how an **Artificial Pancreas System** might make real-time decisions to maintain healthy blood glucose levels based on **carb intake** and **exercise** inputs.

---

## Overview

The **Artificial Pancreas System** simulates the control logic behind automated insulin delivery.
It receives two key input features:

* **Carbohydrate intake (carbs)** — increases glucose levels
* **Exercise duration (minutes)** — decreases glucose levels

Based on these changes, the system predicts and applies one of three possible actions:

1. `deliver_insulin` — if glucose is above the safe range
2. `warn_low_glucose` — if glucose is below the safe range
3. `maintain` — if glucose is within the target range

The goal of this prototype is to understand how data and simple control systems can be used to mimic biological feedback mechanisms.

---

## Class Design

```python
class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
```

### Constructor Parameters

| Parameter             | Description                                             | Example Value |
| --------------------- | ------------------------------------------------------- | ------------- |
| `glucose_level`       | Current blood glucose reading.                          | 100           |
| `insulin_sensitivity` | How strongly insulin affects glucose drop.              | 1.0           |
| `target_glucose`      | The “ideal” glucose level the system tries to maintain. | 100           |
| `tolerance`           | Acceptable deviation above/below the target.            | 10            |
| `min_glucose`         | Minimum safe glucose value to prevent dangerous lows.   | 50            |

---

## Key Methods

### `meal(carbs: float)`

Simulates a meal event — increases glucose based on carb units consumed.

### `exercise(duration: float)`

Simulates physical activity — decreases glucose based on duration.

### `predict_action()`

Acts as the decision-making component:

* If glucose > `target + tolerance` → **deliver_insulin**
* If glucose < `target - tolerance` → **warn_low_glucose**
* Otherwise → **maintain**

Returns both the **action name** and the **new glucose level**.

---

## Testing 

Once the class is implemented, write **unittest tests** to validate that the system behaves correctly under different conditions.
Thorough testing ensures the model’s reliability and accuracy — an essential aspect of any healthcare-related system.

### Core Tests to Implement

1. **Glucose increases after a meal**

   * Feed the system a meal and verify `glucose_level` rises.

2. **Glucose decreases after exercise**

   * Simulate exercise and confirm `glucose_level` drops.

3. **Correct action returned**

   * High glucose → `"deliver_insulin"`
   * Low glucose → `"warn_low_glucose"`
   * Normal range → `"maintain"`

4. **Glucose never below minimum threshold**

   * After long exercise, ensure `glucose_level` doesn’t fall below 50.

5. **Total insulin tracking**

   * Check that `total_insulin_delivered` increases properly when insulin is given.

6. **Sequential events**

   * Simulate multiple actions (e.g., meal → exercise → insulin) and verify correct state updates.

7. **Invalid input handling**

   * Ensure the system raises appropriate errors for negative or non-numeric inputs.

---

## Project Structure

```
main/
    __init__.py
    artificial_pancreas.py
tests/
    __init__.py
    test_artificial_pancreas.py
README.md
requirements.txt
.gitignore
```

---

## Example Usage

```python
from main.artificial_pancreas import ArtificialPancreasSystem

aps = ArtificialPancreasSystem(glucose_level=120)

# Simulate eating and exercising
aps.meal(25)
aps.exercise(15)

# Predict and apply an action
action, new_glucose = aps.predict_action()

print(f"Action: {action}, New Glucose Level: {new_glucose}")
```

---

## Constants

| Constant               | Meaning                                 | Default |
| ---------------------- | --------------------------------------- | ------- |
| `GLUCOSE_PER_CARB`     | Glucose increase per carb unit          | 0.5     |
| `GLUCOSE_BURN_PER_MIN` | Glucose decrease per minute of exercise | 0.3     |

---

## Learning Objectives

* Implement class-based modeling in Python
* Apply logical decision-making to a real-world biomedical scenario
* Design and execute **unit tests** using `unittest`
* Understand the importance of reliable, safety-critical testing in healthcare systems

---

## How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/artificial-pancreas-system.git
   cd artificial-pancreas-system
   ```

2. **Create a virtual environment**

      on windows:
      ```
      python -m venv (.name of env)

      (.name of env)\Scripts\activate

      
      ```
     on linux or WSL:
     ```
        python -m venv (.name of env)

        source ~/path_to_file/env_name/bin/activate

     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tests**

   ```bash
   python -m unittest file.py
   ```


```



