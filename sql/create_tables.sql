CREATE TABLE raw_properties (
    property_id INT IDENTITY(1,1) PRIMARY KEY,
    state VARCHAR(100),
    city VARCHAR(100),
    zip_code VARCHAR(10),
    price FLOAT,
    year_built INT,
    sq_ft FLOAT
);

CREATE TABLE cleaned_properties (
    property_id INT IDENTITY(1,1) PRIMARY KEY,
    state VARCHAR(100),
    city VARCHAR(100),
    zip_code VARCHAR(10),
    price FLOAT,
    year_built INT,
    sq_ft FLOAT,
    price_per_sq_ft FLOAT
);