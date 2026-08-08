-- ============================================
-- Comic Database Schema v1
-- ============================================

DROP TABLE IF EXISTS owned_comics CASCADE;
DROP TABLE IF EXISTS issues CASCADE;
DROP TABLE IF EXISTS series CASCADE;
DROP TABLE IF EXISTS publishers CASCADE;
DROP TABLE IF EXISTS boxes CASCADE;

-- ============================================
-- Publishers
-- ============================================

CREATE TABLE publishers (
    publisher_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- ============================================
-- Series
-- ============================================

CREATE TABLE series (
    series_id SERIAL PRIMARY KEY,

    publisher_id INTEGER NOT NULL
        REFERENCES publishers(publisher_id),

    title VARCHAR(255) NOT NULL,

    volume INTEGER DEFAULT 1,

    start_year INTEGER
);

-- ============================================
-- Issues
-- ============================================

CREATE TABLE issues (
    issue_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    series_id INTEGER NOT NULL,
    issue_number INTEGER NOT NULL,
    publication_date DATE,
    is_key_issue BOOLEAN NOT NULL DEFAULT FALSE,
    variant TEXT,

    FOREIGN KEY (series_id)
    REFERENCES series(series_id)
 );

-- ============================================
-- Boxes
-- ============================================

CREATE TABLE boxes (
    box_id SERIAL PRIMARY KEY,

    label VARCHAR(50) NOT NULL UNIQUE,

    location VARCHAR(255)
);

-- ============================================
-- Owned Comics
-- ============================================

CREATE TABLE owned_comics (
    owned_id SERIAL PRIMARY KEY,

    issue_id INTEGER NOT NULL
        REFERENCES issues(issue_id),

    box_id INTEGER
        REFERENCES boxes(box_id),

    grade DECIMAL(3,1),

    purchase_price NUMERIC(10,2),

    purchase_date DATE,

    estimated_value NUMERIC(10,2),

    signed BOOLEAN DEFAULT FALSE,

    certification_company VARCHAR(25),

    certification_number VARCHAR(50),

    notes TEXT
);
