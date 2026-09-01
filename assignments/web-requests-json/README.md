# 📘 Assignment: Web Requests and JSON

## 🎯 Objective

Learn how Python can fetch data from the internet, decode JSON responses, and turn raw API data into useful information for a simple project.

## 📝 Tasks

### 🛠️ Fetch Data from an API

#### Description
Use Python to request data from a public API and load the JSON response into a Python dictionary.

#### Requirements
Completed program should:

- Use Python's `urllib.request` or another built-in HTTP client to request a JSON-based API.
- Read the response and convert it from JSON text into Python data.
- Print at least 3 pieces of information from the response, such as a title, a value, or a status field.
- Handle a failed request gracefully by printing a helpful error message.

Example output:
```python
Status: OK
Name: Mergington High School
Students: 1200
```

### 🛠️ Build a Simple Data Summary

#### Description
Turn the API data into a small summary report that helps a user understand the information quickly.

#### Requirements
Completed program should:

- Extract the key fields you need from the API response.
- Create a readable summary using `print()` statements.
- Format the output clearly so a person can read it without technical knowledge.
- Include at least one calculation or comparison based on the received data.
- Explain in comments what each major section of the code does.

Example output:
```python
Weather Summary
---------------
Location: Seattle
Temperature: 68°F
Condition: Clear
Recommendation: Light jacket recommended.
```
