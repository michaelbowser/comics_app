# Comic Database Architecture

**Version:** 0.1

---

# Purpose

The Comic Database project is a command-line application for managing a comic book collection using Python and PostgreSQL.

The architecture separates user interaction, application logic, and database access into distinct layers. This separation makes the project easier to understand, maintain, test, and extend.

Current architecture:

```text
User
  │
  ▼
main.py
  │
  ▼
Repositories
  │
  ▼
db.py
  │
  ▼
PostgreSQL
```

---

# Startup Sequence

When the program is started with:

```bash
python src/main.py
```

Python performs the following steps:

1. Opens `main.py`.
2. Reads the file from top to bottom.
3. Imports required modules.

   * `publisher.py`
   * `series.py`
4. Those modules import `db.py`.
5. Python creates function objects for every function definition it encounters.
6. Python reaches:

```python
if __name__ == "__main__":
```

7. The condition evaluates to `True`.
8. `main()` is called.
9. The application begins executing.

---

# Runtime Flow

Once `main()` begins, the application enters a loop.

```text
Display Menu
      │
      ▼
Receive User Input
      │
      ▼
Determine User Choice
      │
      ▼
Call Appropriate Function
      │
      ▼
Execute Repository Function
      │
      ▼
Display Result
      │
      ▼
Repeat Until Exit
```

---

# Current Menu Structure

```text
1. List Publishers
2. Add Publisher
3. List Series
4. Add Series
5. Exit
```

---

# Request Lifecycle Example

### Example: Add Series

```text
User
 │
 │ Selects "4"
 ▼
main.py
 │
 ▼
create_series()
 │
 ├── Display publishers
 ├── Ask for Publisher ID
 ├── Ask for title
 ├── Ask for volume
 └── Ask for start year
 │
 ▼
add_series()
 │
 ▼
db.py
 │
 ▼
PostgreSQL
 │
 │ INSERT INTO series
 ▼
Returns new series_id
 │
 ▼
add_series()
 │
 ▼
create_series()
 │
 ▼
Display success message
```

---

# Responsibilities

## main.py

Responsible for application control flow.

Responsibilities:

* Display menus
* Receive user input
* Decide which operation to execute
* Display output

Does **not**:

* Execute SQL
* Open database connections

---

## publisher.py

Responsible for publisher database operations.

Responsibilities:

* Retrieve publishers
* Insert publishers

Does **not**:

* Display menus
* Request user input

---

## series.py

Responsible for series database operations.

Responsibilities:

* Retrieve series
* Insert series

Does **not**:

* Control application flow
* Print output

---

## db.py

Responsible only for creating PostgreSQL connections.

Responsibilities:

* Connect to PostgreSQL
* Return connection objects

Does **not**:

* Know about publishers
* Know about series
* Contain SQL business logic

---

## PostgreSQL

Responsible for persistent storage.

Responsibilities:

* Store data
* Execute SQL
* Enforce constraints
* Maintain relationships between tables

Examples:

* Primary Keys
* Foreign Keys
* NOT NULL constraints

---

# Data Flow

Every request follows the same pattern.

```text
User
 │
 ▼
main.py
 │
 ▼
Repository
 │
 ▼
db.py
 │
 ▼
PostgreSQL
 │
 ▼
db.py
 │
 ▼
Repository
 │
 ▼
main.py
 │
 ▼
User
```

Information always returns through the same layers that received it.

---

# Repository Pattern

Each repository follows the same workflow.

```text
Receive Parameters
        │
        ▼
Open Database Connection
        │
        ▼
Create Cursor
        │
        ▼
Execute SQL
        │
        ▼
Fetch Results
        │
        ▼
Return Python Objects
```

Example:

```text
get_all_publishers()

↓

execute()

↓

fetchall()

↓

list[tuple]

↓

main.py
```

---

# Database Relationships

Current schema:

```text
Publishers
    │
    ▼
Series
    │
    ▼
Issues
    │
    ▼
Owned Comics
```

Relationships:

* One Publisher → Many Series
* One Series → Many Issues
* One Issue → Many Owned Comics

These relationships are enforced by foreign keys.

---

# Design Principles

## Separation of Responsibilities

| Component       | Responsibility                    |
| --------------- | --------------------------------- |
| `main.py`       | Control flow and user interaction |
| `repositories/` | Database operations               |
| `db.py`         | Database connection management    |
| PostgreSQL      | Data persistence and integrity    |

---

## Repository Pattern

Repositories isolate SQL from the rest of the application.

Advantages:

* SQL exists in one location.
* User interface remains independent.
* Easier testing.
* Easier migration to a web application or API.

---

## Control Flow

`main.py` decides **what happens next**.

Repositories perform work but never decide application behavior.

---

## Data Ownership

* PostgreSQL owns persistent data.
* Python owns program logic.
* Repositories translate between SQL results and Python objects.

---

# Lessons Learned

Key concepts learned while building this project:

* Importing a module is different from calling a function.
* Functions are defined during import but execute only when called.
* Every function returns a value (`None` if no explicit `return` is provided).
* `fetchall()` is a method of the database cursor provided by `psycopg`.
* `main.py` controls execution; repositories perform database work; PostgreSQL stores and protects the data.

---

# Future Architecture

As the project grows, the structure will likely evolve toward:

```text
src/
├── controllers/
├── repositories/
├── models/
├── services/
├── db.py
└── main.py
```

This will make it possible to support multiple interfaces—CLI, web, REST API, or batch imports—while reusing the same repository layer.

