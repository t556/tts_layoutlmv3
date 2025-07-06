#!/usr/bin/env python3
"""
Plurimath Feasibility Test

Quick test to verify Plurimath installation and basic functionality.
"""

import subprocess
import json
import time
from pathlib import Path

def test_plurimath_installation():
    """Test if Plurimath is properly installed"""
    try:
        result = subprocess.run(['plurimath', '--help'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Plurimath installed successfully")
            print(f"   Available commands: convert, help")
            return True
        else:
            print(f"❌ Plurimath installation check failed")
            print(f"   Error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Plurimath command not found")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Plurimath command timed out")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_single_equation(equation: str, expected_latex: str = None):
    """Test Plurimath with a single equation"""
    if not equation:
        print("❌ No equation provided")
        return None, 0.0, False
        
    print(f"\n🧪 Testing equation: {equation}")
    
    try:
        start_time = time.time()
        
        # Run Plurimath conversion (convert asciimath to latex)
        result = subprocess.run(['plurimath', 'convert', 
                               '--input', equation,
                               '--input-format', 'asciimath',
                               '--output-format', 'latex'], 
                              capture_output=True, text=True, timeout=30)
        
        processing_time = time.time() - start_time
        
        if result.returncode == 0:
            output = result.stdout.strip()
            print(f"✅ Conversion successful")
            print(f"   Output: {output}")
            print(f"   Processing time: {processing_time:.3f}s")
            
            if expected_latex:
                accuracy = calculate_simple_accuracy(output, expected_latex)
                print(f"   Accuracy vs expected: {accuracy:.1f}%")
            
            return output, processing_time, True
        else:
            print(f"❌ Conversion failed")
            print(f"   Error: {result.stderr}")
            return None, processing_time, False
            
    except subprocess.TimeoutExpired:
        print("❌ Conversion timed out (>30s)")
        return None, 30.0, False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None, 0.0, False

def calculate_simple_accuracy(output: str, expected: str) -> float:
    """Simple accuracy calculation based on character matching"""
    if not output or not expected:
        return 0.0
    
    # Normalize whitespace and case
    output_clean = ' '.join(output.split()).lower()
    expected_clean = ' '.join(expected.split()).lower()
    
    if output_clean == expected_clean:
        return 100.0
    
    # Simple character-based similarity
    common_chars = sum(1 for a, b in zip(output_clean, expected_clean) if a == b)
    total_chars = max(len(output_clean), len(expected_clean))
    
    return (common_chars / total_chars) * 100 if total_chars > 0 else 0.0

def main():
    """Main feasibility test"""
    print("=" * 60)
    print("PLURIMATH FEASIBILITY TEST")
    print("=" * 60)
    
    # Test 1: Installation check
    print("\n1. Installation Check")
    if not test_plurimath_installation():
        print("❌ Plurimath not available. Please install with: sudo gem install plurimath")
        return
    
    # Test 2: Simple equation test
    print("\n2. Simple Equation Test")
    test_equation = "2 + 2 = 4"
    expected_latex = "2 + 2 = 4"  # Simple case, should be similar
    
    output, processing_time, success = test_single_equation(test_equation, expected_latex)
    
    # Test 3: Complex equation test
    print("\n3. Complex Equation Test")
    complex_equation = "∫ f(x) dx"
    output2, processing_time2, success2 = test_single_equation(complex_equation)
    
    # Summary
    print("\n" + "=" * 60)
    print("FEASIBILITY TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Installation: {'PASS' if success else 'FAIL'}")
    print(f"✅ Simple equation: {'PASS' if success else 'FAIL'}")
    print(f"✅ Complex equation: {'PASS' if success2 else 'FAIL'}")
    print(f"⏱️  Processing time: {processing_time:.3f}s (simple), {processing_time2:.3f}s (complex)")
    
    if success and success2:
        print("\n🎉 Plurimath feasibility test PASSED!")
        print("   Ready to proceed with full testing framework.")
    else:
        print("\n⚠️  Plurimath feasibility test FAILED!")
        print("   Need to troubleshoot installation or configuration.")

if __name__ == "__main__":
    main() 