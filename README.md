# Computer Guesses The Number 🤖

This Python script features a reverse "Guess the Number" game: the **user picks a secret number**, and the computer attempts to guess it. The computer receives hints (`l` for low, `h` for high) from the user to narrow down the range.

The main difference between this version and the player-guess version is the strategy.

## 🚀 Getting Started

### Prerequisites

You only need a working installation of **Python 3**.

### Installation and Running

1.  **Clone the repository** (if new):
    ```bash
    git clone [https://github.com/YourUsername/computer-guess-number.git](https://github.com/YourUsername/computer-guess-number.git)
    cd computer-guess-number
    ```
    (Replace `YourUsername` with your actual GitHub username)

2.  **Run the script** from your terminal:
    ```bash
    python GuessTheNum_cpu_.py
    ```

3.  **Play the game!** Think of a number within the specified range (currently 1 to 10). The computer will start guessing, and you must provide **accurate feedback** (`l`, `h`, or `c`).

## 🧠 How the Computer Guesses

The core logic is within the `computer_guess(x)` function:

1.  **Range Tracking:** The computer maintains a `low` (starting at 1) and a `high` (starting at `x`) bound for the possible number range.
2.  **Randomized Guessing:** Within the `while` loop, the computer selects a **random number** between the current `low` and `high` bounds.
3.  **Adjusting Bounds:**
    * If the user inputs **`h` (too high)**, the current guess is set as the new **upper limit (`high`)** by setting `high = guesse - 1`.
    * If the user inputs **`l` (too low)**, the current guess is set as the new **lower limit (`low`)** by setting `low = guesse + 1`.

> **Note:** The current implementation in `GuessTheNum_cpu_.py` has a slight logical flaw in its boundary adjustment: it only adjusts the guess value (`guesse -= 1` or `guesse += 1`) instead of the bounding variables (`low` and `high`). For true range narrowing, the lines inside the feedback check should be:
> ```python
> if feedback == "h":
>     high = guesse - 1 # Correct adjustment
> elif feedback == "l":
>     low = guesse + 1   # Correct adjustment
> ```
> This logic fix would make the computer guess much more efficiently!

## 💡 Potential Improvements

* Implement the **binary search algorithm** (always guessing the midpoint of `low` and `high`) instead of a random guess for maximum efficiency.
* Fix the boundary adjustment logic (as noted above) to prevent infinite loops or incorrect guesses when the range narrows.
* Allow the user to set the upper limit (`x`) at runtime.

---

Would you like me to show you the **corrected `computer_guess` function** that uses the proper boundary adjustments for efficient guessing?
