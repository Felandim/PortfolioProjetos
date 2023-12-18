-- Connect to the Chinook_Sqlite database
-- BEGIN: Connect to database
-- Replace 'path_to_database' with the actual path to the Chinook_Sqlite.sqlite file
-- For example: '/home/flandim/Documentos/programaçãoProjetos/PortfolioProjetos/4 SQL Project/Chinook_Sqlite.sqlite'
-- Replace 'database_name' with the desired name for the database connection
-- For example: 'chinook_db'
-- Replace 'username' and 'password' with the appropriate credentials if required
-- For example: 'admin' and 'password'
-- Uncomment the appropriate line based on the database engine you are using

-- For SQLite
-- CONNECT TO 'path_to_database' AS database_name;

-- For MySQL
-- CONNECT 'path_to_database' AS database_name;

-- For SQL Server
-- CONNECT 'path_to_database' AS database_name

--   USER 'username' PASSWORD 'password';

-- For PostgreSQL
-- CONNECT 'path_to_database' AS database_name
--   USER 'username' PASSWORD 'password';
-- END: Connect to database

-- Perform analysis queries on the Chinook dataset
-- BEGIN: Analysis queries

-- Example 1: Get the total number of tracks in the database
SELECT COUNT(*) AS total_tracks
FROM Track;

-- Example 2: Get the top 5 artists with the most albums
SELECT artists.Name AS artist_name, COUNT(albums.AlbumId) AS album_count
FROM Artist AS artists
JOIN Album AS albums ON artists.ArtistId = albums.ArtistId
GROUP BY artists.ArtistId
ORDER BY album_count DESC
LIMIT 5;

-- Example 3: Get the average track length by genre
SELECT genres.Name AS genre_name, AVG(tracks.Milliseconds) AS average_length
FROM Genre AS genres
JOIN Track AS tracks ON genres.GenreId = tracks.GenreId
GROUP BY genres.GenreId;

-- END: Analysis queries
