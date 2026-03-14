USE housing_market_db;
GO

SELECT
    state,
    zipCode,
    COUNT(*) AS listing_count,
    AVG(price) AS avg_price,
    AVG(squareFootage) AS avg_sq_ft,
    AVG(price_per_sq_ft) AS avg_price_per_sq_ft,
    AVG(daysOnMarket) AS avg_days_on_market,
    AVG(property_age) AS avg_property_age
FROM sale_listings_cleaned
GROUP BY state, zipCode
ORDER BY state, zipCode;