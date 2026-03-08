# Euler's Number ($e$) Calculator

**Live Preview** — [findEtoN.vercel.app](https://www.findEtoN.vercel.app)

**GitHub Repo** — [github.com/nishchup489-afk/findEtoN](https://www.github.com/nishchup489-afk/findEtoN)

**Project 2 of 100 Python Live Projects**

This project calculates **$e$ (Euler's Number) to the Nth decimal place** using Python.

It started as a raw **CLI math experiment** and later evolved into a small **FastAPI web application** with a clean user interface. The goal was to explore the boundaries of infinite series and precision handling in a web environment.

So this project is not just a calculator. It is a journey through **Taylor series convergence**, **Decimal context management**, and **responsive UI design**.

---

# What this project contains

This project has **two forms**.

## 1. CLI Version

If you only want the raw Python logic, the core function `get_e(n)` handles the mathematical computation. It focuses on the infinite series expansion without the overhead of a web server.

## 2. Website Version

The website version takes an integer input from the user through a form, sends it to a **FastAPI backend**, calculates $e$ using high-precision arithmetic, and renders the result dynamically using **Jinja2 templates**.

---

# Stack Used

* **Python 3.14.0**
* **FastAPI** — Backend routing and request handling
* **Jinja2 Templates** — Injects calculated digits directly into HTML
* **Tailwind CSS (v4)** — Used for the UI styling and responsive layout
* **Decimal Module** — Enables arbitrary precision arithmetic
* **Vercel** — Deployment platform

---

# The Mathematical Journey

Calculating $e$ differs from calculating $\pi$. While $\pi$ often requires specialized algorithms, $e$ can be computed using the elegant **Taylor Series expansion**.

## Method 1 — Standard Floating Point (`math.e`)

**Idea**

Use Python’s built-in constant:

```python
math.e
```

and format it to the requested decimal length.

**Problem**

Python floats follow the IEEE-754 standard and only store about **15–17 digits of precision**.

Any request beyond that simply prints meaningless digits.

**Verdict**

Not suitable for high-precision computation.

---

## Method 2 — Taylor Series with `Decimal`

This is the final algorithm used in the project.

### Taylor Series Formula

$$
e = \sum_{n=0}^{\infty} \frac{1}{n!}
$$

Expanded form:

$$
e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \dots
$$

### Why it works

The factorial in the denominator grows extremely fast:

$$
n! = 1 \times 2 \times 3 \times \dots \times n
$$

Because of this rapid growth, the terms

$$
\frac{1}{n!}
$$

become extremely small very quickly.

This allows the infinite series to **converge rapidly**, meaning only a modest number of iterations are required to obtain many correct digits.

---

# Why `Decimal` Is Required

To compute hundreds or thousands of digits, Python must use **arbitrary precision arithmetic**.

This is controlled using the `Decimal` context.

Example:

```python
from decimal import getcontext
getcontext().prec = n + 5
```

### Precision vs Slicing

**Precision**

We set precision to:

$$
n + 5
$$

The extra **5 digits act as a buffer** to prevent rounding errors from corrupting the final digit.

**Slicing**

After computing the value, the result is converted to a string and trimmed:

```python
str(result)[:n+2]
```

The `+2` accounts for the `"2"` and `"."` at the start of Euler’s number.

---

# Algorithm Flow (Plain Language)

1. **Input**
   The user requests $n$ digits of $e$.

2. **Preparation**
   Decimal precision is set to:

$$
n + \text{buffer}
$$

3. **Iteration**
   A loop calculates each term of the Taylor series:

$$
\frac{1}{i!}
$$

4. **Optimization**
   Instead of recomputing factorial each iteration, the next term is derived from the previous one.

5. **Convergence**
   The loop stops once the new term becomes smaller than the target precision.

6. **Output**
   The final value is sliced and displayed in the UI.

---

# UI and UX

The web interface was designed to reflect the mathematical elegance of the constant.

Features include:

* **Glassmorphism** style card design
* **Mathematical themed background**
* **Responsive layout** for mobile and desktop

---

# Caution

Even though the Taylor series converges quickly, requesting extremely large values such as:

$$
n > 10{,}000
$$

will still consume significant CPU time.

High-precision division and factorial operations are computationally expensive.

Use large requests responsibly.

---

# Project Summary

This project is **Project #2 in a series of 100 Python projects**.

It demonstrates:

* Implementing **infinite series mathematics**
* Managing **Decimal precision contexts**
* Handling **form input → numeric computation** in FastAPI
* Rendering results dynamically using **Jinja templates**
* Deploying a Python application to **Vercel**

---

**Powered by Python, the Taylor Series, and a love for irrational numbers.**
