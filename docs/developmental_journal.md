# Development Journal

---

## Project Goal

Build a production-quality comic book inventory application while learning professional backend software development practices.

Rather than focusing only on writing code, the project emphasizes understanding architecture, debugging, database design, and software engineering principles.

---

## Session 1

### Accomplishments

* Installed PostgreSQL
* Created database
* Built schema
* Learned SQL fundamentals

### Lessons Learned

* PostgreSQL roles are different from databases.
* A schema defines the structure of the database.
* Primary keys uniquely identify rows.
* Foreign keys create relationships.

---

## Session 2

### Accomplishments

* Connected Python to PostgreSQL using psycopg.
* Built reusable database connection function.
* Created first repository.

### Lessons Learned

* SQL should not live in the user interface.
* Repository functions isolate database operations.
* Context managers automatically clean up resources.

---

## Session 3

### Accomplishments

* Built Publisher repository.
* Built Series repository.
* Added interactive CLI.

### Lessons Learned

* Importing a module is different from calling a function.
* Functions execute only when called.
* `fetchall()` is a cursor method that returns query results.
* `return` statements control what information flows back to the caller.

---

## Session 4

### Accomplishments

* Improved debugging workflow.
* Built application architecture documentation.
* Began thinking about software design instead of individual lines of code.

### Lessons Learned

* Read tracebacks from the bottom up.
* Trace data through the application layer by layer.
* Separate control flow from work.
* Think in terms of responsibilities rather than files.

---

# Mental Models Developed

* A function should have one primary responsibility.
* The controller decides what happens next.
* Repositories perform database work.
* PostgreSQL owns persistent data.
* Data flows through layers and returns through the same layers.

---

# Personal Observations

Patterns noticed while building this project:

* Understanding *why* a design exists is more valuable than memorizing syntax.
* Debugging improves when the application is viewed as interacting layers.
* Small, incremental features are easier to build, understand, and test than large changes.

---

# Future Reflections

As the project grows, continue documenting:

* New architectural decisions
* Debugging discoveries
* Database improvements
* Lessons learned
* Ideas for future refactoring

This journal is intended for my future self. It should explain not only what changed, but why the change was made.

