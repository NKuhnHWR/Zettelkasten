---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
[Jane Dane]

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

[Visualize and describe the data model(s) of your application. This description should match the actual implementation.]
The applications data model contains three entities. These are users, notes and categories. Users contains an individual ID and the users name. Notes contains an individual ID for each note, owner, content, type, source and category. Categories contains an individual ID, owner and title. 
Every user can have one to multiple notes and categories. Every note is owned by one user and is assigned to exact one category. Every category is owned by one user and can contain zero to many notes.
