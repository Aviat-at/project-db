USE project_db;

INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
VALUES 
    ('New York', '2023-01-15', 5.5, 12.3, 65.0),
    ('London', '2023-01-15', 8.2, 8.7, 72.5),
    ('Tokyo', '2023-01-15', 12.8, 5.2, 68.0),
    ('Sydney', '2023-01-15', 25.3, 2.1, 55.5),
    ('Berlin', '2023-01-15', 3.7, 9.8, 70.0),
    ('Mumbai', '2023-01-15', 28.6, 0.5, 80.2),
    ('Toronto', '2023-01-15', -2.4, 15.0, 62.3),
    ('Dubai', '2023-01-15', 22.1, 0.1, 45.8),
    ('Singapore', '2023-01-15', 30.2, 7.5, 85.0),
    ('Paris', '2023-01-15', 7.8, 6.4, 75.5);