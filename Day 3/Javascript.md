# JavaScript Documentation — Introduction through DOM

> Documentation based on the supplied **Introduction to Javascript** presentation.
> Scope: **Introduction → Basics → Control Flow → Functions → Arrays → Objects → DOM**.

---

## Table of Contents

1. [Introduction to JavaScript](#1-introduction-to-javascript)
2. [Basics of JavaScript](#2-basics-of-javascript)
3. [Control Flow](#3-control-flow)
4. [Functions](#4-functions)
5. [Arrays](#5-arrays)
6. [Objects](#6-objects)
7. [DOM — Document Object Model](#7-dom--document-object-model)
8. [Quick Revision Sheet](#8-quick-revision-sheet)

> **Scope Note:** The original presentation continues after DOM with Event Handling, Callback, Promise, Async/Await, and Closures. Those topics are intentionally not included here.

---

# 1. Introduction to JavaScript

## 1.1 What is JavaScript?

JavaScript is a programming language used to add behavior and interactivity to web applications.

According to the supplied presentation:

- JavaScript was created by **Brendan Eich**.
- It was initially created for adding simple interactivity in the **Netscape browser**.
- It is an important core technology in web application development along with **HTML** and **CSS**.

## 1.2 Where Does JavaScript Run?

| Environment | Role |
|---|---|
| **Browser** | Client-side scripting, interactivity, and DOM updates |
| **Node.js** | Server-side scripting, backend applications, and APIs |
| **Cross-platform frameworks** | Desktop, mobile, and IoT applications |

## 1.3 HTML, CSS and JavaScript

| Technology | Responsibility | Examples |
|---|---|---|
| **HTML** | Structure | Headings, paragraphs, buttons |
| **CSS** | Styling | Colors, layout, animations |
| **JavaScript** | Behavior | Click actions, form validation, dynamic content |

### Simple Analogy

Think of a webpage as a building:

- **HTML** → Structure
- **CSS** → Appearance
- **JavaScript** → Behavior and interaction

---

# 2. Basics of JavaScript

## 2.1 Variables

Variables are named storage locations used to hold values.

The presentation introduces three variable keywords:

### `var`

- Used in older JavaScript code.
- The presentation recommends using it mainly when old-browser support is required.

### `let`

- Introduced in 2015.
- Cannot be redeclared in the same scope.

### `const`

- Introduced in 2015.
- Cannot be redeclared.
- Cannot be reassigned.
- Has block scope.

## 2.2 When to Use `var`, `let`, or `const`

The supplied presentation recommends:

1. Always declare variables.
2. Use `const` if the value should not be changed.
3. Use `const` if the type/reference should not be changed, including arrays and objects.
4. Use `let` only when `const` cannot be used.
5. Use `var` only when you must support old browsers.

### Example

```javascript
const college = "SSGMCE";
let count = 25;

count = count + 1;

// Reassignment of a const variable is not allowed:
// college = "ABC";
```

---

## 2.3 Data Types

The presentation covers the following data types:

| Data Type | Meaning | Example |
|---|---|---|
| **String** | Text | `"Apexaiq"` |
| **Number** | Numeric value | `25`, `3.14` |
| **Boolean** | Logical value | `true`, `false` |
| **Null** | Intentional empty value | `null` |
| **Undefined** | Declared but not assigned | `undefined` |
| **Object** | Collection of key-value pairs | `{ name: "A" }` |
| **Array** | Ordered collection of values | `[10, "JS", true]` |

---

## 2.4 Operators

### Arithmetic Operators

```text
+   -   *   /   %
```

Used for calculations.

### Comparison Operators

```text
==   ===   !=   <   >
```

Used to compare values.

### Logical Operators

```text
&&   ||   !
```

- `&&` → AND
- `||` → OR
- `!` → NOT

### Assignment Operators

```text
=   +=   -=   *=   /=
```

Used to assign or update values.

---

# 3. Control Flow

Control flow determines which statements execute and how many times they execute.

The presentation covers:

- Conditional Statements
- Loops

---

## 3.1 Conditional Statements

### `if`

Executes a block of code if a specified condition is true.

### `else`

Executes a block if the condition is false.

### `else if`

Tests another condition when the previous condition is false.

### `switch`

Used to specify many alternative blocks of code.

### Example: `if / else if / else`

```javascript
const marks = 78;

if (marks >= 90) {
    console.log("Excellent");
} else if (marks >= 60) {
    console.log("Good");
} else {
    console.log("Needs improvement");
}
```

### Example: `switch`

```javascript
const day = 2;

switch (day) {
    case 1:
        console.log("Monday");
        break;

    case 2:
        console.log("Tuesday");
        break;

    default:
        console.log("Invalid day");
}
```

---

## 3.2 Loops

The presentation covers five types:

| Loop | Use |
|---|---|
| **for** | Loops through a block of code a specified number of times |
| **for/in** | Loops through the properties of an object |
| **for/of** | Loops through the values of an iterable |
| **while** | Loops while a specified condition is true |
| **do/while** | Executes the block and continues while the condition is true |

### Example: `for`

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

### Example: `for...of`

```javascript
const fruits = ["Apple", "Mango", "Banana"];

for (const fruit of fruits) {
    console.log(fruit);
}
```

---

# 4. Functions

## 4.1 What is a Function?

A function is a block of code designed to perform a task.

According to the presentation:

- A function runs when it is called/invoked.
- Functions help in reusing code.

## 4.2 Key Concepts

| Concept | Meaning |
|---|---|
| **Parameters** | Input values |
| **Return** | Output value |
| **Global Scope** | Accessible from broader/global code |
| **Local Scope** | Available inside a function |
| **Block Scope** | Available inside `{ }` when using `let`/`const` |

---

## 4.3 Types of Functions

### 1. Function Declaration

- Defined using the `function` keyword.
- Hoisted.
- Can be called before its declaration.

```javascript
function add(a, b) {
    return a + b;
}

console.log(add(10, 20));
```

### 2. Function Expression

- A function stored in a variable.
- Used after its definition.

```javascript
const greet = function(name) {
    return "Hello " + name;
};
```

### 3. Arrow Function

- Introduced with ES6.
- Uses the `=>` syntax.
- Does not have its own `this`.

```javascript
const square = (n) => n * n;
```

### 4. Anonymous Function

A function without a name.

It is often used as a callback.

### 5. Immediately Invoked Function Expression (IIFE)

A function that runs automatically after being defined.

### 6. Higher-Order Function

A function that:

- Takes another function as an argument, or
- Returns another function.

### 7. Recursive Function

A function that calls itself.

```javascript
function countdown(n) {
    if (n === 0) return;

    console.log(n);
    countdown(n - 1);
}
```

---

# 5. Arrays

## 5.1 What is an Array?

An array is an ordered list of values.

The presentation notes that arrays can store:

- Numbers
- Strings
- Objects
- Functions

### Example

```javascript
const fruits = ["Apple", "Mango", "Banana"];

console.log(fruits[0]); // Apple
console.log(fruits[2]); // Banana
```

---

## 5.2 Array Properties and Methods

| Property / Method | Purpose |
|---|---|
| `.length` | Returns the total number of items |
| `.push()` | Adds an item at the end |
| `.pop()` | Removes an item from the end |
| `.shift()` | Removes the first item |
| `.unshift()` | Adds an item at the start |
| `.map()` | Processes array items and creates a new array |
| `.filter()` | Creates a new array containing matching items |
| `.reduce()` | Combines values into an accumulated result |

### Example

```javascript
const numbers = [1, 2, 3];

numbers.push(4);
numbers.pop();

numbers.unshift(0);
numbers.shift();

const doubled = numbers.map(n => n * 2);

const even = numbers.filter(n => n % 2 === 0);

const total = numbers.reduce((sum, n) => sum + n, 0);
```

---

## 5.3 Why Arrays Are Useful

- Store multiple related values in one variable.
- Access values using their position/index.
- Process collections efficiently using methods such as `map()`, `filter()`, and `reduce()`.

---

# 6. Objects

## 6.1 What is an Object?

An object is a collection of **key-value pairs**.

According to the presentation:

- Keys are properties.
- Keys are always strings or symbols.
- Values can be anything: strings, numbers, arrays, functions, or other objects.

### Example

```javascript
const student = {
    name: "Aarav",
    age: 20,
    skills: ["HTML", "CSS", "JavaScript"]
};
```

---

## 6.2 Features of Objects

The supplied presentation identifies these features:

- Accessing Properties
- Adding Properties
- Updating Properties
- Deleting Properties
- Methods
- Built-in Object Methods

### Accessing Properties

```javascript
console.log(student.name);

console.log(student["age"]);
```

### Adding a Property

```javascript
student.city = "Shegaon";
```

### Updating a Property

```javascript
student.age = 21;
```

### Deleting a Property

```javascript
delete student.city;
```

### Object with a Method

```javascript
const user = {
    name: "Aarav",

    greet: function() {
        return "Hello " + this.name;
    }
};

console.log(user.greet());
```

---

## 6.3 Arrays vs Objects

| Array | Object |
|---|---|
| Ordered collection of values | Collection of key-value pairs |
| Usually accessed using an index | Usually accessed using a property/key |
| Useful for lists and collections | Useful for describing entities and their properties |

---

# 7. DOM — Document Object Model

## 7.1 What is the DOM?

**DOM** stands for **Document Object Model**.

According to the supplied presentation:

- The DOM is a programming interface for HTML and XML documents.
- It represents the page structure as a tree of nodes.
- Nodes can include elements, attributes, text, etc.
- JavaScript can manipulate the DOM to change page content, style, or structure dynamically.

---

## 7.2 DOM Tree

The original presentation contains a DOM tree diagram.

The diagram represents the structure approximately as:

```text
Document
   |
   └── <html>
       |
       ├── <head>
       │    |
       │    └── <title>
       │          |
       │          └── Text: "My title"
       |
       └── <body>
            |
            ├── <a>
            │    ├── Attribute: href
            │    └── Text: "My link"
            |
            └── <h1>
                 |
                 └── Text: "My header"
```

This demonstrates how a webpage can be represented as a hierarchy/tree.

---

## 7.3 Important DOM Nodes

| Node / Part | Example |
|---|---|
| **Document** | The overall document |
| **Element** | `<html>`, `<head>`, `<body>`, `<h1>`, `<a>` |
| **Attribute** | `href` on an `<a>` element |
| **Text** | Text contained inside an element |

---

## 7.4 Why is the DOM Important?

The presentation gives three major reasons:

### 1. Dynamic Content

The DOM lets JavaScript change content dynamically, such as:

- Text
- Images

### 2. User Interaction

The DOM enables interaction with users, such as:

- Clicking buttons
- Filling forms

### 3. Dynamic Websites

DOM manipulation helps create dynamic websites instead of static pages.

---

# 7.5 DOM Manipulation

The supplied presentation identifies four main DOM manipulation activities:

1. Selecting elements
2. Changing content
3. Changing style
4. Creating new elements

---

## 7.6 Selecting Elements

JavaScript can select HTML elements from the document.

### `getElementById()`

```javascript
const title = document.getElementById("title");
```

### `querySelector()`

```javascript
const heading = document.querySelector("h1");
```

### `querySelectorAll()`

```javascript
const buttons = document.querySelectorAll("button");
```

---

## 7.7 Changing Content

One way to change the text of an element is `textContent`.

```javascript
const message = document.getElementById("message");

message.textContent = "Welcome to JavaScript!";
```

---

## 7.8 Changing Style

The `style` property can be used to modify inline styles.

```javascript
const box = document.querySelector(".box");

box.style.fontSize = "24px";

box.style.padding = "20px";
```

---

## 7.9 Creating New Elements

JavaScript can create a new HTML element using `document.createElement()`.

```javascript
const paragraph = document.createElement("p");

paragraph.textContent =
    "This paragraph was created using JavaScript.";

document.body.appendChild(paragraph);
```

---

# 7.10 Mini DOM Example

This example combines:

- DOM element selection
- Content modification
- Style modification
- Creating a new element

### HTML

```html
<h1 id="title">Original Title</h1>

<button id="changeBtn">Change</button>

<div id="container"></div>
```

### JavaScript

```javascript
const title = document.getElementById("title");

const button = document.getElementById("changeBtn");

const container = document.getElementById("container");

button.addEventListener("click", () => {

    title.textContent = "Title Changed!";

    title.style.fontSize = "32px";

    const p = document.createElement("p");

    p.textContent = "New content added to the DOM.";

    container.appendChild(p);
});
```

> **Scope Note:** The `addEventListener()` line is shown only to demonstrate how DOM manipulation can be triggered. **Event Handling itself is the next topic in the original presentation and is outside this documentation scope.**

---

## 7.11 DOM Learning Checklist

Before moving beyond DOM, you should be able to:

- Explain what the DOM is.
- Understand the DOM as a tree representation of a webpage.
- Identify elements, attributes, and text nodes.
- Select HTML elements using JavaScript.
- Change an element's content.
- Change an element's style.
- Create new HTML elements.
- Insert newly created elements into the document.

---

# 8. Quick Revision Sheet

| Topic | Key Point |
|---|---|
| **JavaScript** | Adds behavior and interactivity to web pages |
| **Variables** | `var`, `let`, `const` |
| **Data Types** | String, Number, Boolean, Null, Undefined, Object, Array |
| **Operators** | Arithmetic, Comparison, Logical, Assignment |
| **Conditions** | `if`, `else`, `else if`, `switch` |
| **Loops** | `for`, `for/in`, `for/of`, `while`, `do/while` |
| **Functions** | Reusable blocks of code |
| **Arrays** | Ordered collections of values |
| **Objects** | Collections of key-value pairs |
| **DOM** | Tree representation of an HTML/XML document that JavaScript can manipulate |

---

# Suggested Practice Sequence

1. Create variables using `const` and `let`.
2. Write a program using `if/else`.
3. Practice `for`, `while`, and `for...of` loops.
4. Write functions with parameters and return values.
5. Create an array and practice `push()`, `pop()`, `map()`, `filter()`, and `reduce()`.
6. Create an object and practice accessing, adding, updating, and deleting properties.
7. Create a simple HTML page.
8. Use JavaScript to select elements.
9. Change text and styles using the DOM.
10. Create and insert new DOM elements.

---

## Source Boundary

This documentation is based on the supplied **Introduction to Javascript** presentation through its **DOM** section.

The original presentation places **Event Handling** immediately after DOM, followed by:

- Callback
- Promise
- Async and Await
- Closures

Those later sections are **not covered** because the requested scope ends at DOM.

---

# End of Documentation — DOM
