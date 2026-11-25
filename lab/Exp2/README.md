# Experiment 2 - Cascading Style Sheets (CSS) Styling

## Aim
To design and style web documents using various Cascading Style Sheets (CSS) techniques including External, Internal, and Inline styles, CSS Selectors, Box Model, Responsive Layouts (Flexbox and Grid), and CSS Animations & Transitions.

## Student Information
- **Name:** Akshat Mamgain
- **SAP ID:** 590014875

## Technologies Used
- HTML5
- CSS3 (Flexbox, CSS Grid, Transitions, Keyframe Animations)

## How to Create the Experiment
1. Create a folder named `Exp2` inside the `lab/` directory.
2. Create six part folders: `parta`, `partb`, `partc`, `partd`, `parte`, and `partf`.
3. Create an HTML file in each part folder for its demonstration. For Part A, also create `styles.css` in the same folder.
4. Add the HTML page structure (`<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`) to each file.
5. Add CSS according to each part's topic (external, internal, inline, selectors, layout, or animations).
6. Save the files and open each HTML page in a browser to review the result.

## Procedure / Steps to Perform
1. **External CSS (Part A):** Open `parta/index-external.html`. Confirm its `<link>` points to `styles.css`, then edit the stylesheet to style the page. Resize the browser to observe the responsive layout.
2. **Internal CSS (Part B):** Open `partb/index-internal.html`. Inspect the CSS inside the `<style>` element in `<head>` and change a rule to see its effect.
3. **Inline CSS (Part C):** Open `partc/index-inline.html`. Inspect the `style` attributes on elements and change a property to see how inline styling works.
4. **CSS Selectors (Part D):** Open `partd/index-selectors.html`. Review examples of type, class, ID, attribute, pseudo-class, and pseudo-element selectors; hover or focus interactive elements where applicable.
5. **Flexbox and Grid (Part E):** Open `parte/index-layout.html`. Examine the Flexbox and Grid sections, then resize the browser to observe how the layout adapts.
6. **Animations and Transitions (Part F):** Open `partf/index-animations.html`. Hover over animated elements and observe the transitions, transforms, and keyframe animation.
7. Repeat any interaction after changing a CSS value, save the file, and refresh the page to compare the result.

## Directory Structure
- `parta/` — **External CSS**: Demonstrates linking an external stylesheet (`styles.css`) with cards, grids, and responsive media queries.
- `partb/` — **Internal CSS**: Demonstrates embedded styling using the `<style>` tag within the document `<head>`.
- `partc/` — **Inline CSS**: Demonstrates element-level styling applied via the `style` attribute.
- `partd/` — **CSS Selectors**: Comprehensive demonstration of universal, element, class, ID, attribute, pseudo-class (`:hover`, `:focus`, `:nth-child`), and pseudo-element (`::before`, `::after`) selectors.
- `parte/` — **CSS Layout**: In-depth demonstration of modern layout techniques using Flexbox (one-dimensional) and CSS Grid (two-dimensional).
- `partf/` — **CSS Animations & Transitions**: Demonstrates keyframe animations, hover transforms, loading spinners, and multi-property transitions.

## How to View
Open any of the `.html` files directly in your web browser:
```bash
# Example using default browser on Windows
start lab/Exp2/parta/index-external.html
start lab/Exp2/partb/index-internal.html
start lab/Exp2/partc/index-inline.html
start lab/Exp2/partd/index-selectors.html
start lab/Exp2/parte/index-layout.html
start lab/Exp2/partf/index-animations.html
```

## Learning Outcome
Mastered the three methods of CSS application (external, internal, inline) and their specificity hierarchy; gained proficiency in using complex CSS selectors, building responsive layouts with Flexbox and CSS Grid, and enhancing user experience with CSS transitions and keyframe animations.
