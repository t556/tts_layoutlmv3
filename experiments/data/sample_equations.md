# Sample Equations Test Dataset

## Source: How To Prove It.pdf
*Manual extraction of representative equations for testing*

### Basic Arithmetic
- `2 + 2 = 4`
- `x + y = z`
- `a² + b² = c²`

### Fractions
- `1/2`
- `3/4`
- `(x + y)/(a + b)`

### Complex Expressions
- `∫ f(x) dx`
- `∑_{i=1}^{n} x_i`
- `lim_{x→∞} f(x)`

## Source: Whittley_IBM_Paper.pdf
*Manual extraction of representative equations for testing*

### Mathematical Notation
- `∀x ∈ ℝ`
- `∃y : P(y)`
- `A ∩ B = ∅`

### Equations with Subscripts/Superscripts
- `x₁ + x₂ = x₃`
- `y² = mx + b`
- `e^(iπ) + 1 = 0`

## Test Categories
1. **Basic Operations**: +, -, ×, ÷, =, ≠
2. **Fractions**: Simple and nested
3. **Greek Letters**: α, β, γ, δ, etc.
4. **Mathematical Symbols**: ∫, ∑, ∏, ∞, etc.
5. **Subscripts/Superscripts**: x₁, y², etc.
6. **Complex Expressions**: Nested fractions, integrals, limits

## Notes
- These are manually extracted examples
- Each equation will be tested with all 5 models
- We'll measure conversion accuracy and output quality
- Focus on common textbook equation types 