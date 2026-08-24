# Development Journal

---

## Project Goal

 - Practice Python and SQL 
 - Learn, and make mistakes, designing a code database
 - Debug, Debug, Debug
 - Create a project that will bring me value, personally and
    professionally.
 - Work without LLM assistance. ChatGPT was used in conjunction until
    August 15, 2026. Db and code generally laid out. Many, Many bugs.
    Working without assistance going forward to refine and develop
    skills.

---

## Session 1


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


* Connected Python to PostgreSQL using psycopg.
* Built reusable database connection function.
* Created first repository.

### Lessons Learned

* SQL should not live in the user interface.
* Repository functions isolate database operations.
* Context managers automatically clean up resources.

---

## Session 3


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


* Improved debugging workflow.
* Built application architecture documentation.
* Began thinking about software design instead of individual lines of code.

### Lessons Learned

* Read tracebacks from the bottom up.
* Trace data through the application layer by layer.
* Separate control flow from work.
* Think in terms of responsibilities rather than files.

---

# Observations:
* A function should have one primary responsibility.
* The controller decides what happens next.
* Repositories perform database work.
* PostgreSQL owns persistent data.
* Data flows through layers and returns through the same layers.
* Understand *why* a design exists.
* Be aware of how debugging affects more than the layer that you're
working on.
* Build a function or feature at at time, verify for specific function
and edge cases.

---
### Features to be added:
 *  (LONG TERM)Create linkage to add publisher, series, issue and owned comic at
 same time.
 * when adding issue, upon series_id, have list of series display. 
 * On available issues choice from add issues, avaiable issues should
 list the full database identify
 * For owned comic, provide None parameter for purchase date and
 purchase price.
 * For list owned comics, re format so only series title and issue
 number show (top line)

