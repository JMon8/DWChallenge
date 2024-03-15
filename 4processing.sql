-- Number of books written each year by each author
SELECT a.author_key,
        b.first_publish_year,
        COUNT(*) AS book_count
FROM books b
JOIN book_authors ba
    ON b.key = ba.book_key
JOIN authors a
    ON ba.author_key = a.author_key


;

-- Avg number of books per author by year
WITH author_book_count AS (
    SELECT a.author_key,
            b.first_publish_year,
            COUNT(*) AS book_count
    FROM books b
    JOIN book_authors ba
        ON b.key = ba.book_key
    JOIN authors a
        ON ba.author_key = a.author_key
    GROUP BY a.author_key, b.first_publish_year
)

SELECT first_publish_year,
        CAST(SUM(book_count) as DOUBLE)/
        CAST(COUNT(DISTINCT author_key) as DOUBLE) AS avg_books_per_author
FROM author_book_count
GROUP BY first_publish_year

