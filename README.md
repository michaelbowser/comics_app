####  This is a personal comic book inventory/collection application built
####  with Python and PostgresSQL.

It has two primary purposes:

 1. Practice development skills by building a personally practical
    application from the ground up.
 2. Track and estimate the value of my comic collection for potential sale.

#### Project Goals

  1. Python and Postgres integration
  2. Database build from scratch
  3. Front and backend integration
  4. Debugging Practice
  5. Features such as filtering, searching, and data analysis

#### Current Features
  
  1. PostgreSQL Database 
  2. Relational Schema
  3. Publisher table 
  4. Series table 
  5. Issues table 
  6. Storage Box tracking
  7. Python/PostgreSQL integration 

#### Project Structure
comic_db
|
|- .venv/
|
|- sql/
|  |- schema.sql 
|
|- src/
|  |- db.py 
|  |- db_test.py 
|  |- repositories/
|  |- models/
|
|
|- tests/
|- requirements.txt 
|- README.md 
|- .gitignore

#### Database Design

Tables:
 - Publishers 
   - Differentiates publishers like DC and Marvel
 - Series
   - Stores comic series and links each series to a publisher 
 - Issues 
   - Stores information for each issue 
 - Boxes
   - Indicates particular box comic is stored in 
 - owned_comics
   - combo value of each comics grade, box location, estimated valuation
    and box location

#### Tech Stack 
  - Python 3 
  - PostgreSQL
  - psycopg
  - Git 
  - Neovim 
  - Linux (Arch / Omarchy)

#### Phases of development
 - Phase 1 
   - Install PostgreSQL
   - Create db schema
   - Connect Python to PostgreSQL
 - Phase 2 
   - Repo layer
   - CRUD 
   - Search by: title, publisher and issue number

 - Phase 3 
   - Collections stats 
   - Value tracking 
   - import/export

 - Phase 4 
   - Text-based interface
   - Web interface
   - Barcode support
   - Cover image support 

#### Author 

 Michael Bowser
 

   

