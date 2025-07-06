# Math Equation Conversion Model Testing Roadmap

## Project Overview
Testing and evaluating models that convert digital textbook math equations to LaTeX code for an MVP implementation.

## Test Models (Ranked by Priority)
1. **Plurimath 0.9+** (Ruby gem, CLI & API) - Highest accuracy (≥98%)
2. **mathml-to-latex v1.5.0** (npm) - Lightweight JavaScript parser (97-99% accuracy)
3. **unicode-math** (Python/Rust) - UnicodeMath to LaTeX conversion
4. **unicode2latex** (Python) - Bidirectional Unicode ↔ LaTeX mapping
5. **Pandoc + pandoc-unicode-math filter** - Document-level conversion

## Experiment Structure

### Phase 1: Environment Setup and Data Preparation
- [ ] Create organized directory structure
- [ ] Extract sample equations from test PDFs
- [ ] Set up evaluation metrics and test cases
- [ ] Install and configure each model

### Phase 2: Individual Model Testing
For each model (A → E):
- [ ] Basic installation and configuration
- [ ] Test with sample equations from Sources/
- [ ] Document accuracy, performance, and limitations
- [ ] Create comparison matrix

### Phase 3: Comparative Analysis
- [ ] Side-by-side accuracy comparison
- [ ] Performance benchmarking
- [ ] Error pattern analysis
- [ ] MVP recommendation

## Directory Structure
```
tts_layoutlmv3/
├── Sources/                    # Original test files
├── scrap/                      # Experimental/test work
├── experiments/                # Organized experiment results
│   ├── data/                   # Extracted equations and test cases
│   ├── results/                # Model outputs and evaluations
│   └── comparisons/            # Comparative analysis
├── notes/                      # Progress documentation
└── tools/                      # Finalized scripts and utilities
```

## Success Criteria (MVP)
- **Accuracy**: >95% token preservation for common math expressions
- **Performance**: <5 seconds per page processing
- **Reliability**: Consistent output format (LaTeX)
- **Ease of Integration**: Simple API or CLI interface

## Next Steps
1. Set up directory structure
2. Extract sample equations from test PDFs
3. Begin with Plurimath testing (highest priority)
4. Document findings in notes/

## Evaluation Metrics
- **Token Accuracy**: Percentage of correctly converted symbols/operators
- **Structural Integrity**: Preservation of fraction trees, nested expressions
- **Processing Speed**: Time per equation/page
- **Error Types**: Classification of conversion failures
- **Output Quality**: Valid LaTeX syntax and readability 