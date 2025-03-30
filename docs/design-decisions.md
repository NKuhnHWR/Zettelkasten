---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

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

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
