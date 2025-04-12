---
title: Reference
parent: Technical Docs
nav_order: 3
---


{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Login

### login()

**Route:** '/login'

**Methods:** `POST` `GET` 

**Purpose:** Login the user and redirect to the dashboard if login is successful.

**Sample output:**

Redirection to dashboard or show Error if Login was not successful.

---

## Dashboard

### dashboard()

**Route:** '/dashboard'

**Methods:** `POST` `GET` 

**Purpose:** Show all Notes from the user and show all categories in a sidebar.

**Sample output:**

![Alle Notizen](assets/images/AlleNotizen.png)

---
## Register

### register()

**Route:** '/register'

**Methods:** `POST` `GET` 

**Purpose:** Register the user and redirect to the Login if registration is successful.

**Sample output:**

Redirection to login or show Error if Registration was not successful.


---

## Dashboard

### dashboard()

**Route:** '/dashboard'

**Methods:** `POST` `GET` 

**Purpose:** Show all Notes from the user and show all categories in a sidebar.

**Sample output:**

![Alle Notizen](assets/images/AlleNotizen.png)

---

## Note
### note()

**Route:** '/note'

**Methods:** `POST` `GET` 

**Purpose:** Show form to create a new note and save the new note. 

**Sample output:**

![Notiz erstellen](assets/images/NotizErstellen.png)

---

## Change note
### change_note(id)

**Route:** '/change_note/<int:id>'

**Methods:** `POST` `GET` 

**Purpose:** Show form to change a note with prefilled fields. 

**Sample output:**

![Notiz bearbeiten](assets/images/NotizBearbeiten.png)

---

## Filter dashboard
### filtered_dashboard(id)

**Route:** '/filtered_dashboard/<int:id>'

**Methods:** `POST` `GET` 

**Purpose:** Show all Notes from the chosen category and show all categories in a sidebar.

**Sample output:**

![Gefiltertes Dashboard](assets/images/GefilterteNotiz.png)

---

## Delete Note
### delete_note(id)

**Route:** '/delete_note/<int:id>'

**Methods:** `POST` `GET` 

**Purpose:** Deleting the chosen note.
**Sample output:**

Dashboard without the deleted note.