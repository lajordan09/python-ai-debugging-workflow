```
# **DEBUG_LOG.md — AI Collaboration Record**

## **Task: Debugging & Refactoring a Legacy Data Processing Script**

**Date:** May 30, 2026 
**Developer:** LaQuita  Jordan
**Project:** Customer Analytics Pipeline (process_data.py)

---

## **Step 1: Understanding the Codebase**

### **Prompt to AI**
**Understand the codebase**

I asked the AI to provide a high‑level summary of the script, break down each function, identify side effects, and call out potential bugs, inefficiencies, and PEP 8 violations.

### **AI Response (Summary)**

- The script loads customer data, processes transactions, computes metrics, generates reports, and exports customer data.
- Functions analyzed:
  - `__init__()` — initializes internal structures
  - `load_data()` — loads customer CSV
  - `process_transactions()` — loads transactions and updates totals
  - `calculate_customer_metrics()` — computes revenue, averages, top customers, category breakdown
  - `find_matches()` — substring search
  - `generate_report()` — JSON report generation
  - `export_customer_data()` — CSV/JSON export
- Potential issues:
  - No validation for malformed CSV rows
  - Risky assumptions about dict structure
  - Inefficient loops in metrics and search
  - Possible bug in `export_customer_data()` when determining fieldnames

### **My Notes**
The AI’s breakdown helped me quickly understand the flow and identify where the export bug might originate.

---

## **Step 2: Diagnosing the Bug**

### **Prompt to AI**
**Diagnose the bug**
```
[I provided the error log: error.log 
](https://github.com/lajordan09/python-ai-debugging-workflow/blob/main/error.log)

```
Error exporting data: 'dict' object has no attribute 'keys'


### **AI Response (Root Cause)**

- The JSON export failed because **`self.customers` contained at least one entry that was *not* a dict**.
- This corruption happens when a malformed transaction row overwrites a customer entry.
- Example: a row like  
  `T003,name,75.00,2024-01-12,clothing`  
  causes `"name"` to become a customer_id key.
- JSON export then fails because it attempts to serialize a structure containing invalid entries.

### **My Notes**
This matched the behavior in the real error log. The AI’s reasoning clarified why the CSV export succeeded but JSON export failed.

---

## **Step 3: Writing a Failing Unit Test**

### **Prompt to AI**
**Create failing unit test**

I asked for a unittest that reproduces the failure.

### **AI Response (Test Case)**

The AI generated a test that:

- Creates temporary CSV files
- Injects a malformed transaction row (`customer_id = "name"`)
- Calls `export_customer_data(..., "json")`
- Asserts that the export fails (before the fix)

### **My Notes**
This test successfully reproduced the exact error from the logs.

---

## **Step 4: Refactoring & Fixing the Code**

### **Prompt to AI**
**Refactor export_customer_data**

I asked the AI to fix the bug and improve the function.

### **AI Response (Refactor Summary)**

The AI rewrote `export_customer_data()` to:

- Validate that each customer entry is a dict
- Skip malformed entries safely
- Build a clean structure before exporting
- Improve PEP 8 compliance
- Add better error handling

### **My Notes**
After applying the fix, JSON export no longer crashed — even with malformed data.

---

## **Step 5: Updating the Test to Expect Success**

### **Prompt to AI**
**Update test for success**

After the fix, the JSON export should succeed.

### **AI Response (Updated Assertion)**

```python
self.assertTrue(
    result,
    "JSON export should succeed after handling malformed customer entry safely"
)

### **My Notes**
The updated test passed, confirming the fix.

---

## **Step 6: Additional Performance Optimizations**

### **Prompts to AI**
- **Optimize find_matches**
- **Optimize calculate_customer_metrics**

### **AI Response (Optimizations)**

- Replaced nested loops with list comprehension in `find_matches()`
- Used `defaultdict(int)` for category counting
- Cleaned up sorting logic for top customers
- Improved readability and maintainability

### **My Notes**
These optimizations improved performance without changing behavior.

---

## **Step 7: Final Testing**

### **Results**

- ✔ All unit tests passed  
- ✔ JSON export works correctly  
- ✔ Malformed entries are safely skipped  
- ✔ No more `'dict' object has no attribute 'keys'`  
- ✔ Performance improvements verified  

---

## **Reflection on AI Collaboration**

### **What Worked Well**
- Detailed prompts produced high‑quality analysis
- The AI’s reasoning helped pinpoint the root cause quickly
- Iterative refinement led to robust fixes
- The AI generated complete, runnable unit tests

### **Challenges**
- Initial diagnosis required clarification
- Some optimizations needed additional guidance
- Ensuring correctness still required human review and testing

### **Key Takeaways**
1. AI accelerates debugging when given precise context  
2. Human oversight ensures correctness and code quality  
3. Iterative prompting produces the best results  
4. AI collaboration is most effective when paired with strong testing discipline  

---
```
