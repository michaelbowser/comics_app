# Database Design

**Version:** 0.1

---

# Purpose

This document explains the design of the PostgreSQL database used by the Comic Database project.

Rather than documenting SQL syntax, this document explains **why the tables exist**, **how they relate**, and **why the relationships were chosen**.

---

# Current Database Structure

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

Each table represents a single concept within the comic collection.

---

# Publishers

Stores comic book publishers.

Examples:

* Marvel
* DC
* Image Comics
* Dark Horse
* Valiant

Primary Key:

```text
publisher_id
```

A publisher may publish many series.

Relationship:

```text
One Publisher
        │
        ▼
Many Series
```

---

# Series

Stores comic series.

Examples:

* Amazing Spider-Man
* Batman
* Saga

Fields:

* publisher_id
* title
* volume
* start_year

Primary Key:

```text
series_id
```

Foreign Key:

```text
publisher_id
```

Every series belongs to exactly one publisher.

---

# Issues

Stores individual comic issues.

Examples:

* Amazing Spider-Man #300
* Batman #404

Each issue belongs to exactly one series.

Relationship:

```text
One Series
        │
        ▼
Many Issues
```

---

# Owned Comics

Represents physical copies owned by the collector.

This table exists because multiple copies of the same issue may exist.

Example:

```text
Amazing Spider-Man #300

Copy 1
Near Mint

Copy 2
Very Fine
```

Instead of duplicating issue information, every owned comic references an issue.

Relationship:

```text
One Issue
        │
        ▼
Many Owned Copies
```

---

# Why Normalize?

Instead of storing:

```text
Marvel
Amazing Spider-Man
Issue 300
```

inside every owned comic, the database stores relationships.

Advantages:

* Less duplicated data
* Easier updates
* Better consistency
* Smaller database
* Faster searches

---

# Primary Keys

Every table has a unique identifier.

Examples:

```text
publisher_id

series_id

issue_id

owned_comic_id
```

Primary keys uniquely identify each row.

---

# Foreign Keys

Foreign keys connect tables together.

Examples:

```text
series.publisher_id

↓

publishers.publisher_id
```

and

```text
issues.series_id

↓

series.series_id
```

Foreign keys prevent invalid relationships.

For example, a series cannot reference a publisher that does not exist.

---

# Future Tables

Potential additions include:

* Creators
* Characters
* Story Arcs
* Genres
* Locations
* Teams
* Cover Artists
* Variants
* Grading Companies

These will extend the database while preserving the existing relationships.

---

# Design Philosophy

The database models the real-world hierarchy of comic publishing.

```text
Publisher

↓

Series

↓

Issue

↓

Owned Copy
```

Each level depends on the one above it.

This design minimizes duplication, preserves data integrity, and supports future expansion.

