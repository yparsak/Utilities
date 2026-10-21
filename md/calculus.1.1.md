# 1.1 The Concept of a Limit

The concept of a limit is the foundational building block of calculus. It allows us to describe the behavior of a function as the input approaches a specific value, regardless of whether the function is actually defined at that value.

## Conceptual Explanation

In algebra, we often ask: "What is the value of $f(x)$ when $x = a$?" 
In calculus, we ask: "As $x$ gets closer and closer to $a$, what value does $f(x)$ approach?"

A limit exists if the function approaches the same specific value from both the left side (values smaller than $a$) and the right side (values larger than $a$).

### Formal Notation
We denote the limit of $f(x)$ as $x$ approaches $a$ as:
$$\lim_{x \to a} f(x) = L$$
This reads as: "The limit of $f(x)$ as $x$ approaches $a$ equals $L$."

## Illustrative Examples

### Example 1: A Simple Continuous Function
Consider the function $f(x) = 2x + 3$. To find the limit as $x$ approaches 1:
$$\lim_{x \to 1} (2x + 3) = 2(1) + 3 = 5$$
In this case, the limit is simply the value of the function at $x=1$.

### Example 2: A Hole in the Function (Removable Discontinuity)
Consider the function:
$$f(x) = \frac{x^2 - 1}{x - 1}$$
If we try to plug in $x = 1$, we get $\frac{0}{0}$, which is undefined. However, we can simplify the expression for all $x \neq 1$:
$$f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1$$
Now, we can find the limit as $x$ approaches 1:
$$\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} (x + 1) = 1 + 1 = 2$$
Even though the function is not defined at $x=1$, the limit exists and is equal to 2 because the function values approach 2 from both sides.

## Summary
- **The limit** describes the destination, not necessarily the arrival.
- **Existence**: A limit $\lim_{x \to a} f(x)$ exists if and only if the left-hand limit $\lim_{x \to a^-} f(x)$ and the right-hand limit $\lim_{x \to a^+} f(x)$ are equal.
