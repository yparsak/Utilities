# 1.2 Calculating Limits Numerically and Graphically

While algebraic manipulation is a powerful tool for finding limits, it is not always possible or intuitive. Numerically and graphically estimating limits allows us to understand function behavior when a formula is complex or unknown.

## Conceptual Explanation

Calculating limits numerically involves creating a table of values. We choose values of $x$ that get progressively closer to the target value $a$ from both the left ($x < a$) and the right ($x > a$). If the corresponding $f(x)$ values approach a single constant $L$, we can conclude that the limit is $L$.

Calculating limits graphically involves observing the trend of the function's graph on a coordinate plane. We trace the path of the curve from both sides of the vertical line $x = a$. If the paths converge toward the same y-value $L$, the limit exists.

## Illustrative Examples

### Example 1: Numerical Estimation
Consider the limit $\lim_{x \to 0} \frac{\sin(x)}{x}$. Plugging in $x=0$ results in $\frac{0}{0}$, which is indeterminate. Let's examine values closer to 0:

| $x$ (from left) | $f(x)$ | $x$ (from right) | $f(x)$ |
| :--- | :--- | :--- | :--- |
| -0.1 | 0.99833 | 0.1 | 0.99833 |
| -0.01 | 0.99998 | 0.01 | 0.99998 |
| -0.001 | 1.00000 | 0.001 | 1.00000 |

As $x \to 0$ from both sides, $f(x)$ approaches 1. Thus, we estimate:
$$\lim_{x \to 0} \frac{\sin(x)}{x} = 1$$

### Example 2: Graphical Estimation
Consider a function $g(x)$ defined by a piecewise graph where there is a jump at $x=2$. 
- As we follow the graph from the left ($x \to 2^-$), the y-value approaches 3.
- As we follow the graph from the right ($x \to 2^+$), the y-value approaches 5.

Since the left-hand limit $\lim_{x \to 2^-} g(x) = 3$ and the right-hand limit $\lim_{x \to 2^+} g(x) = 5$ are not equal:
$$\lim_{x \to 2} g(x) \text{ does not exist (DNE)}$$

## Summary
- **Numerical Approach**: Use tables of values to observe trends as $x$ gets arbitrarily close to $a$.
- **Graphical Approach**: Visualize the function's path to see if the left and right sides converge to the same point.
- **Limitation**: Numerical and graphical methods provide estimates; algebraic methods provide exact proofs.
