# Ground Truth LaTeX Outputs

## Expected LaTeX conversions for test equations

### Basic Arithmetic
- Input: `2 + 2 = 4`
- Expected: `2 + 2 = 4`

- Input: `x + y = z`
- Expected: `x + y = z`

- Input: `a² + b² = c²`
- Expected: `a^{2} + b^{2} = c^{2}`

### Fractions
- Input: `1/2`
- Expected: `\frac{1}{2}`

- Input: `3/4`
- Expected: `\frac{3}{4}`

- Input: `(x + y)/(a + b)`
- Expected: `\frac{x + y}{a + b}`

### Complex Expressions
- Input: `∫ f(x) dx`
- Expected: `\int f(x) \, dx`

- Input: `∑_{i=1}^{n} x_i`
- Expected: `\sum_{i=1}^{n} x_{i}`

- Input: `lim_{x→∞} f(x)`
- Expected: `\lim_{x \to \infty} f(x)`

### Mathematical Notation
- Input: `∀x ∈ ℝ`
- Expected: `\forall x \in \mathbb{R}`

- Input: `∃y : P(y)`
- Expected: `\exists y : P(y)`

- Input: `A ∩ B = ∅`
- Expected: `A \cap B = \emptyset`

### Equations with Subscripts/Superscripts
- Input: `x₁ + x₂ = x₃`
- Expected: `x_{1} + x_{2} = x_{3}`

- Input: `y² = mx + b`
- Expected: `y^{2} = mx + b`

- Input: `e^(iπ) + 1 = 0`
- Expected: `e^{i\pi} + 1 = 0`

## Notes
- These are idealized expected outputs
- Actual outputs may vary based on model implementation
- Some models may use different LaTeX conventions
- Accuracy will be calculated based on similarity to these expected outputs 