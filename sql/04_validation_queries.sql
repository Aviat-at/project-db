USE project_db;

-- Verify table structure
SHOW COLUMNS FROM ClimateData;

-- Verify data exists
SELECT COUNT(*) AS total_records FROM ClimateData;

-- Verify humidity column exists and has data
SELECT location, humidity FROM ClimateData LIMIT 5;