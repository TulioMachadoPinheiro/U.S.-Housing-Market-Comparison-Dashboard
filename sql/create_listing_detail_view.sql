USE housing_market_db;
GO

CREATE OR ALTER VIEW vw_listing_detail AS
SELECT
    id,
    formattedAddress,
    city,
    state,
    zipCode,
    county,
    latitude,
    longitude,
    propertyType,
    bedrooms,
    bathrooms,
    squareFootage,
    lotSize,
    yearBuilt,
    status,
    price,
    listingType,
    listedDate,
    removedDate,
    createdDate,
    lastSeenDate,
    daysOnMarket,
    mlsName,
    mlsNumber,
    source_zip,
    price_per_sq_ft,
    property_age
FROM sale_listings_cleaned;
GO

SELECT TOP 20 *
FROM vw_listing_detail;