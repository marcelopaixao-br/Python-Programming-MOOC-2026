# Part 2, Section 3: Combining Conditions

This section explores advanced logical control flow using boolean operators (`and`, `or`, `not`), nested conditional statements, and complex range evaluations to handle multi-tier rules and data validation.

---

## 📂 Exercises Included

| Exercise | File Name | Description | Key Concepts |
| :--- | :--- | :--- | :--- |
| **Age check** | `01_ex_Age_check.py` | Validates user age ranges, identifying implausible entries or edge cases. | Logical `and`, numeric boundaries, multi-branch conditionals |
| **Nephews** | `02_ex_Nephews.py` | Identifies character names belonging to specific family groups (Donald Duck or Mickey Mouse). | Logical `or`, string equality checks |
| **Grades and points** | `03_ex_Grades_and_points.py` | Evaluates numerical point scores and maps them to corresponding academic grades. | Interval filtering (`and`), error bounds handling |
| **FizzBuzz** | `04_ex_FizzBuzz.py` | Checks integer divisibility by 3, 5, or both simultaneously. | Modulo operator (`%`), strictness hierarchy in conditional ordering |
| **Leap year** | `05_ex_Leap_year.py` | Determines if a year is a leap year using hierarchical divisibility rules. | Nested/hierarchical conditional branches |
| **Alphabetically in the middle** | `06_ex_Alphabetically_in_the_middle.py` | Compares three separate letters to find which one sits in the middle alphabetically. | Chained comparisons (`a <= x <= b`), logical disjunction (`or`) |
| **Gift tax calculator** | `07_ex_Gift_tax_calculator.py` | Calculates progressive gift taxes based on tax brackets, fixed bases, and rates. | Multi-tier range evaluations, floating-point math, string formatting (`:.2f`) |

---

## 🚀 Key Learnings & Concepts

* **Boolean Operators (`and`, `or`, `not`):** Combining multiple boolean expressions to build complex condition checks simultaneously.
* **Strictness Hierarchy:** Ordering conditional checks from most specific (e.g., checking both conditions with `and`) to general to prevent logical short-circuiting.
* **Range Boundaries & Formatting:** Evaluating numerical intervals efficiently and applying precise string formatting (like `:.2f`) for monetary or decimal outputs.git status