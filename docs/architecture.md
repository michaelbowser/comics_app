# Comic Database Architecture

**Version:** 0.1

---

# Purpose

The Comic Database project is a command-line application that allows a user to manage a comic book collection using Python and PostgreSQL.

The design emphasizes separation of responsibilities so that the user interface, business logic, and database access remain independent.

Current architecture:

```
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

Python performs the following steps.

1. Opens `main.py`.
2. Reads the file from top to bottom.
3. Imports required modules.

   * `publisher.py`
   * `series.py`
4. Each imported module imports `db.py`.
5. Python creates function objects for every function definition.
6. Python reaches:

```python
if __name__ == "__main__":
```

7. The condition evaluates to `True`.
8. `main()` is called.
9. The application begins execution.

---

# Runtime Flow

After startup, the program enters an infinite loop.

```
Display Menu

↓

Receive User Input

↓

Determine Selected Option

↓

Call Appropriate Function

↓

Perform Database Operation

↓

Display Result

↓

Repeat
```

The loop ends only when the user selects Exit.

---

# Current Menu Structure

```
1. List Publishers
2. Add Publisher
3. List Series
4. Add Series
5. Exit
```

---

# Request Flow Example

Example: **Add Series**

```
User

↓

Select Menu Option 4

↓

main.py

↓

create_series()

↓

Display Publishers

↓

Collect User Input

↓

add_series()

↓

db.py

↓

PostgreSQL

↓

INSERT INTO series

↓

Return new series_id

↓

Display Success Message
```

---

# Responsibilities

## main.py

Responsible for application control.

Responsibilities:

* Display menu
* Receive user input
* Decide which function to execute
* Display output to the user

Does **not**:

* Execute SQL
* Open database connections

---

## publisher.py

Responsible only for publisher database operations.

Responsibilities:

* Retrieve publishers
* Insert publishers

Does **not**:

* Print menus
* Ask the user for input

---

## series.py

Responsible only for series database operations.

Responsibilities:

* Retrieve series
* Insert series
* Execute SQL queries related to the `series` table

Does **not**:

* Display information
* Control program flow

---

## db.py

Responsible only for database connectivity.

Responsibilities:

* Create PostgreSQL connections
* Return connection objects

Does **not**:

* Know anything about publishers
* Know anything about series
* Execute business logic

---

## PostgreSQL

Responsible for persistent storage.

Responsibilities:

* Store data
* Enforce constraints
* Execute SQL
* Maintain relationships between tables

Examples:

* Primary Keys
* Foreign Keys
* NOT NULL constraints

---

# Data Flow

Example:

```
User

↓

main.py

↓

Repository

↓

db.py

↓

PostgreSQL

↓

db.py

↓

Repository

↓

main.py

↓

User
```

Information always flows back through the same layers.

---

# Current Repository Pattern

Each repository follows the same design.

```
Receive Parameters

↓

Open Connection

↓

Create Cursor

↓

Execute SQL

↓

Fetch Results

↓

Return Python Objects
```

Example:

```
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

```
Publishers

↓

Series

↓

Issues

↓

Owned Comics
```

Relationships:

* One Publisher → Many Series
* One Series → Many Issues
* One Issue → Many Owned Comics

Foreign keys enforce these relationships.

---

# Design Principles

## Separation of Responsibilities

Each module has one primary responsibility.

| Module       | Responsibility                    |
| ------------ | --------------------------------- |
| main.py      | Control flow and user interaction |
| repositories | Database operations               |
| db.py        | Database connection management    |
| PostgreSQL   | Data storage and integrity        |

---

## Repository Pattern

Repositories isolate SQL from the rest of the application.

Advantages:

* SQL exists in one location.
* User interface remains independent.
* Easier to test.
* Easier to replace the interface (CLI, web, API).

---

## Control Flow

Only `main.py` decides what happens next.

Repositories perform work but never decide application behavior.

---

## Data Ownership

The database owns persistent data.

Python owns program logic.

Repositories translate between Python objects and SQL results.

---

# Future Architecture

Planned additions:

```
src/

controllers/

repositories/

models/

services/

db.py
```

Possible future interfaces:

* CLI
* Flask web application
* FastAPI REST API
* Batch import tools

The repository layer should remain reusable regardless of the interface.

---

# Lessons Learned

During development the following concepts became clear:

* Importing a module is different from calling a function.
* Functions are defined during import but execute only when called.
* `return` statements determine what information flows back to the caller.
* `fetchall()` is a cursor method provided by `psycopg`, returning query results as Python objects.
* `main.py` controls execution; repositories perform data access; PostgreSQL manages persistence and relationships.

