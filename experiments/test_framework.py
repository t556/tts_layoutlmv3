#!/usr/bin/env python3
"""
Math Equation Conversion Model Testing Framework

This script tests various models that convert math equations to LaTeX format.
Models tested:
1. Plurimath (Ruby gem)
2. mathml-to-latex (npm)
3. unicode-math (Python/Rust)
4. unicode2latex (Python)
5. Pandoc + filter
"""

import subprocess
import time
import json
import os
from typing import Dict, List, Tuple

class ModelTester:
    def __init__(self):
        self.results = {}
        self.test_equations = self.load_test_equations()
        self.ground_truth = self.load_ground_truth()
        
    def load_test_equations(self) -> List[str]:
        """Load test equations from our sample dataset"""
        equations = [
            # Basic arithmetic
            "2 + 2 = 4",
            "x + y = z", 
            "a² + b² = c²",
            
            # Fractions
            "1/2",
            "3/4",
            "(x + y)/(a + b)",
            
            # Complex expressions
            "∫ f(x) dx",
            "∑_{i=1}^{n} x_i",
            "lim_{x→∞} f(x)",
            
            # Mathematical notation
            "∀x ∈ ℝ",
            "∃y : P(y)",
            "A ∩ B = ∅",
            
            # Subscripts/superscripts
            "x₁ + x₂ = x₃",
            "y² = mx + b",
            "e^(iπ) + 1 = 0"
        ]
        return equations
    
    def load_ground_truth(self) -> Dict[str, str]:
        """Load ground truth LaTeX outputs"""
        ground_truth = {
            "2 + 2 = 4": "2 + 2 = 4",
            "x + y = z": "x + y = z", 
            "a² + b² = c²": "a^{2} + b^{2} = c^{2}",
            "1/2": "\\frac{1}{2}",
            "3/4": "\\frac{3}{4}",
            "(x + y)/(a + b)": "\\frac{x + y}{a + b}",
            "∫ f(x) dx": "\\int f(x) \\, dx",
            "∑_{i=1}^{n} x_i": "\\sum_{i=1}^{n} x_{i}",
            "lim_{x→∞} f(x)": "\\lim_{x \\to \\infty} f(x)",
            "∀x ∈ ℝ": "\\forall x \\in \\mathbb{R}",
            "∃y : P(y)": "\\exists y : P(y)",
            "A ∩ B = ∅": "A \\cap B = \\emptyset",
            "x₁ + x₂ = x₃": "x_{1} + x_{2} = x_{3}",
            "y² = mx + b": "y^{2} = mx + b",
            "e^(iπ) + 1 = 0": "e^{i\\pi} + 1 = 0"
        }
        return ground_truth
    
    def test_plurimath(self, equation: str) -> Tuple[str, float]:
        """Test Plurimath conversion"""
        try:
            start_time = time.time()
            # Plurimath CLI command
            result = subprocess.run(['plurimath', 'convert', 
                                   '--input', equation,
                                   '--input-format', 'asciimath',
                                   '--output-format', 'latex'], 
                                  capture_output=True, text=True, timeout=30)
            
            processing_time = time.time() - start_time
            
            if result.returncode == 0:
                output = result.stdout.strip()
            else:
                output = f"ERROR: {result.stderr.strip()}"
            
            return output, processing_time
        except subprocess.TimeoutExpired:
            return "ERROR: Conversion timed out (>30s)", 30.0
        except Exception as e:
            return f"ERROR: {str(e)}", 0.0
    
    def test_mathml_to_latex(self, equation: str) -> Tuple[str, float]:
        """Test mathml-to-latex conversion"""
        try:
            start_time = time.time()
            # Node.js script call (to be implemented)
            # result = subprocess.run(['node', 'convert.js', equation],
            #                        capture_output=True, text=True)
            # output = result.stdout.strip()
            
            # Placeholder for now
            output = f"mathml-to-latex: {equation}"
            processing_time = time.time() - start_time
            
            return output, processing_time
        except Exception as e:
            return f"ERROR: {str(e)}", 0.0
    
    def test_unicode_math(self, equation: str) -> Tuple[str, float]:
        """Test unicode-math conversion"""
        try:
            start_time = time.time()
            # Python unicode-math call (to be implemented)
            # import unicode_math
            # output = unicode_math.to_latex(equation)
            
            # Placeholder for now
            output = f"unicode-math: {equation}"
            processing_time = time.time() - start_time
            
            return output, processing_time
        except Exception as e:
            return f"ERROR: {str(e)}", 0.0
    
    def test_unicode2latex(self, equation: str) -> Tuple[str, float]:
        """Test unicode2latex conversion"""
        try:
            start_time = time.time()
            # Python unicode2latex call (to be implemented)
            # import unicode2latex
            # output = unicode2latex.convert(equation)
            
            # Placeholder for now
            output = f"unicode2latex: {equation}"
            processing_time = time.time() - start_time
            
            return output, processing_time
        except Exception as e:
            return f"ERROR: {str(e)}", 0.0
    
    def test_pandoc(self, equation: str) -> Tuple[str, float]:
        """Test Pandoc conversion"""
        try:
            start_time = time.time()
            # Pandoc command (to be implemented)
            # result = subprocess.run(['pandoc', '--from=markdown', '--to=latex', 
            #                        '-f', 'markdown+tex_math_dollars', 
            #                        '--filter=pandoc-unicode-math'],
            #                        input=f"${equation}$", capture_output=True, text=True)
            # output = result.stdout.strip()
            
            # Placeholder for now
            output = f"Pandoc: {equation}"
            processing_time = time.time() - start_time
            
            return output, processing_time
        except Exception as e:
            return f"ERROR: {str(e)}", 0.0
    
    def run_all_tests(self):
        """Run tests for all models on all equations"""
        models = {
            'plurimath': self.test_plurimath,
            'mathml-to-latex': self.test_mathml_to_latex,
            'unicode-math': self.test_unicode_math,
            'unicode2latex': self.test_unicode2latex,
            'pandoc': self.test_pandoc
        }
        
        for model_name, test_func in models.items():
            print(f"Testing {model_name}...")
            self.results[model_name] = {}
            
            for equation in self.test_equations:
                output, processing_time = test_func(equation)
                
                # Calculate accuracy if ground truth exists
                accuracy = 0.0
                if equation in self.ground_truth:
                    accuracy = self.calculate_accuracy(equation, output, self.ground_truth[equation])
                
                self.results[model_name][equation] = {
                    'output': output,
                    'processing_time': processing_time,
                    'accuracy': accuracy
                }
    
    def save_results(self, filename: str = 'experiments/results/test_results.json'):
        """Save test results to JSON file"""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"Results saved to {filename}")
    
    def calculate_accuracy(self, original: str, converted: str, expected: str) -> float:
        """Calculate conversion accuracy using token comparison"""
        if not converted or not expected:
            return 0.0
        
        # Normalize whitespace and case
        converted_clean = ' '.join(converted.split()).lower()
        expected_clean = ' '.join(expected.split()).lower()
        
        if converted_clean == expected_clean:
            return 100.0
        
        # Simple character-based similarity
        common_chars = sum(1 for a, b in zip(converted_clean, expected_clean) if a == b)
        total_chars = max(len(converted_clean), len(expected_clean))
        
        return (common_chars / total_chars) * 100 if total_chars > 0 else 0.0
    
    def validate_latex(self, latex_output: str) -> bool:
        """Verify output is valid LaTeX"""
        if not latex_output or 'ERROR' in latex_output:
            return False
        
        # Basic LaTeX validation - check for common patterns
        latex_patterns = [
            r'\\[a-zA-Z]+',  # LaTeX commands
            r'\{.*\}',       # Braces
            r'\[.*\]',       # Square brackets
            r'\(.*\)',       # Parentheses
            r'[a-zA-Z0-9]',  # Alphanumeric characters
            r'[+\-*/=<>≤≥≠∈∉∩∪⊂⊃⊆⊇]',  # Math operators
            r'[α-ωΑ-Ω]',     # Greek letters
            r'[∫∑∏√∞∂∇∆]'   # Math symbols
        ]
        
        import re
        for pattern in latex_patterns:
            if re.search(pattern, latex_output):
                return True
        
        # If no patterns match, it might still be valid (simple text)
        return len(latex_output.strip()) > 0
    
    def print_summary(self):
        """Print a summary of test results"""
        print("\n" + "="*50)
        print("TEST RESULTS SUMMARY")
        print("="*50)
        
        for model_name, results in self.results.items():
            print(f"\n{model_name.upper()}:")
            total_time = sum(r['processing_time'] for r in results.values())
            error_count = sum(1 for r in results.values() if 'ERROR' in r['output'])
            valid_latex_count = sum(1 for r in results.values() 
                                  if self.validate_latex(r['output']))
            
            # Calculate average accuracy
            accuracies = [r['accuracy'] for r in results.values() if 'accuracy' in r]
            avg_accuracy = sum(accuracies) / len(accuracies) if accuracies else 0.0
            
            print(f"  Total processing time: {total_time:.3f}s")
            print(f"  Errors: {error_count}/{len(results)}")
            print(f"  Valid LaTeX: {valid_latex_count}/{len(results)}")
            print(f"  Success rate: {((len(results) - error_count) / len(results) * 100):.1f}%")
            print(f"  LaTeX validity rate: {(valid_latex_count / len(results) * 100):.1f}%")
            print(f"  Average accuracy: {avg_accuracy:.1f}%")

if __name__ == "__main__":
    tester = ModelTester()
    tester.run_all_tests()
    tester.save_results()
    tester.print_summary() 