# Part 3 — Loops with conditions

Notes and solutions from the **Loops with conditions** section (Part 3) of the **Python Programming MOOC 2026** course (University of Helsinki).

## Learning Goals
- Write `while` loops controlled by Boolean conditions rather than relying solely on `while True` and `break`.
- Apply the three core parts of a loop: **initialisation**, **condition**, and **updating** iteration variables.
- Prevent infinite loops by ensuring the loop condition eventually evaluates to `False`.
- Debug loops using `print` statements and visualizers like [Python Tutor](https://pythontutor.com/) to inspect variable states step by step.
- Build `strings` incrementally inside loops using string concatenation (`+=`) and `f-strings`.

## Exercises Covered
- **Print numbers:** Print even numbers from `2` to `30` using a `while` loop.
- **Fix the code: Countdown:** Fix the condition and variable update in a countdown loop.
- **Numbers:** Print positive integers smaller than a user-provided upper limit.
- **Powers of two:** Print powers of `2` (`1, 2, 4, 8, ...`) starting at `1` without exceeding the upper limit.
- **Powers of base n:** Generalize powers of two so the user specifies both the upper limit and the multiplication base.
- **The sum of consecutive numbers, version 1:** Sum consecutive integers starting from `1` (`1 + 2 + 3 + ...`) until the sum is greater than or equal to the limit, then print the total.
- **The sum of consecutive numbers, version 2:** Print both the full expression and the final sum (e.g., `The consecutive sum: 1 + 2 + 3 + 4 = 10`).

## Key Takeaways
- **Three parts of a `while` loop:** Set initial values before the loop, check a condition before each iteration, and update variables inside the loop body.
- **Counters vs. accumulators:** Keep the sequence counter (`1, 2, 3, ...`) separate from variables that accumulate a running total or build a string.
- **Building strings gradually:** Use `+=` and `f-strings` inside loops, handling the first element carefully so leading separators don't sneak in.