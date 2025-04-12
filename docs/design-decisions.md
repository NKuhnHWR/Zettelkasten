---
title: Design Decisions
nav_order: 3
---

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Setup of html files

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-03-2025

### Problem statement

The first problem addressed is how to design the html templates. There is to be discussed where the styling is made and if there is a cental file where all other files inherit from.

### Decision

I decided to create a style.css file and a base.html file in addition to the actual templates. This decision was made because it is on the long run the more effective way. By choosing this option I make sure that each page has the same basic structure. This is less work for maintaining when changing the structure. In addition it is more user friendly when every page has the same basic structure.

### Regarded options

I regarded two alternative options:

+ Setup page structure for each html file seperate
+ Creating a base template from wich the other files inherit

| Criterion | No inheritance from base.html | Inheritance from base.html |
| --- | --- | --- |
| **Knowledge** | No extra knowlede about inheritance needed | Requires knowledge about inheritance |
| **Maintaining the structure** | Harder because each file has to be maintained for itself | Easier because all files inherit from base |
| **User experience** | Just good when every html file has the same structure | Ensured by having the same structure by inheritance |

## 02: Register and Login function

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-03-2025

### Problem statement

Should the Register and Login function be implemented in html or in python?

### Decision

I decided to use WTForms and implement the Register and Login function in Python.

### Regarded options

I regarded two alternative options:

+ Build a form in the according html file
+ Implement the function in Python using WTForms

| Criterion | Implement in html | Implement using WTForms |
| --- | --- | --- |
| **Data validation** | Data validation is not automatically implemented | WTForms comes with data validation |
| **Maintaining the structure** | Harder because each file has to be maintained for itself | Easier because all files inherit from base |
| **User experience** | Just good when every html file has the same structure | Ensured by having the same structure by inheritance |

## Other design decisions

To be very honest: There weren't many decisions I made in a conscious consideration of all options. Most of this project was created by try and error of different options until I found an option that worked and fulfilled the requirements. There were also challenges I mastered by choosing an option I already used in this project. For example: I copied the Login and Register form 1:1 (Source on the source page). The form for the Note was created by adapting the Register form because I knew how it worked. 