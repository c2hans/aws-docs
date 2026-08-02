---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html
---

# Place categories and filtering results with Amazon Location
<a name="category-filtering"></a>

Places are categorized. If you search for a business, the business might be a `Restaurant`, for example. Even the results of a search for an address can be categorized by whether it was matched to an *address*, *street*, or *intersection*.

Broadly, Amazon Location Service categorizes places into *Place types*. Points of interest are further categorized into *Point of interest types*.

**Note**
Not all results will have categories.

You can use the categories to filter your geocoding searches.

## Filtering results
<a name="place-filtering"></a>

When you are using `SearchPlaceIndexForText`, you can filter the results that are returned by the categories that you want to use. For example:
+ If you want to search for a place called "Hometown Coffee", and only return results that are categorized as coffee shops, you can do that by calling `SearchPlaceIndexForText` and include the *Point of interest category*, `Coffee Shop` in the `FilterCategories` parameter.
+ When searching for "123 Main St, Anytown, WA, 98123, USA", you can filter result to just addresses, so you don't get matches on, for example, the postal code. Filter to just addresses by including *Place type*, `AddressType` in the `FilterCategories` parameter.

**Note**
Not all data providers support filtering, or support it in the same way. For more information, see [Filtering limitations by data provider](#filter-limitations).

The next section lists the categories that you can filter on.

## Categories
<a name="place-categories"></a>

The following lists show the categories that Amazon Location Service uses to categorize and filter. These categories are used in all languages, independent of the language parameter is set to a different language.

**Note**
Amazon Location Service maps data provider categories to this set of categories. If a data provider puts a place into a category that is not part of the Amazon Location Service category list, the provider category will be included in the results as a *supplemental category*.

**Place types** – These types are used to indicate the type of match that was used to find the result.
+ `AddressType` – Returned when the result was matched to an address.
+ `StreetType` – Returned when the result was matched to a street.
+ `IntersectionType` – Returned when the result was matched to the intersection of two streets.
+ `PointOfInterestType` – Returned when the result was match to a point of interest, such as a business, or civic location.
+ `CountryType` – Returned when the result was matched to a country or major region.
+ `RegionType` – Returned when the result was matched to a region within a country, such as a state or province.
+ `SubRegionType` – Returned when the result was matched to a subregion within a country, such as a county or metropolitan area.
+ `MunicipalityType` – Returned when the result was matched to a city or town.
+ `NeighborhoodType` – Returned when the result was matched to a neighborhood or area within a city.
+ `PostalCodeType` – Returned when the result was matched to a postal code.

**Point of interest categories** – These categories are used to indicate the type of business or location for point of interest results.
+ `Airport`
+ `Amusement Park`
+ `Aquarium`
+ `Art Gallery`
+ `ATM`
+ `Bakery`
+ `Bank`
+ `Bar`
+ `Beauty Salon`
+ `Bus Station`
+ `Car Dealer`
+ `Car Rental`
+ `Car Repair`
+ `Car Wash`
+ `Cemetery`
+ `Cinema`
+ `City Hall`
+ `Clothing Store`
+ `Coffee Shop`
+ `Consumer Electronics Store`
+ `Convenience Store`
+ `Court House`
+ `Dentist`
+ `Embassy`
+ `Fire Station`
+ `Fitness Center`
+ `Gas Station`
+ `Government Office`
+ `Grocery`
+ `Higher Education`
+ `Hospital`
+ `Hotel`
+ `Laundry`
+ `Library`
+ `Liquor Store`
+ `Lodging`
+ `Market`
+ `Medical Clinic`
+ `Motel`
+ `Museum`
+ `Nightlife`
+ `Nursing Home`
+ `Park`
+ `Parking`
+ `Pet Store`
+ `Pharmacy`
+ `Plumbing`
+ `Police Station`
+ `Post Office`
+ `Religious Place`
+ `Restaurant`
+ `School`
+ `Shopping Mall`
+ `Sports Center`
+ `Storage`
+ `Taxi Stand`
+ `Tourist Attraction`
+ `Train Station`
+ `Veterinary Care`
+ `Zoo`

## Filtering limitations by data provider
<a name="filter-limitations"></a>

Not all providers have the same filtering functionality. The following table describes the differences.

| Provider | APIs with filter support | Categories supported for filtering | Return values |
| --- | --- | --- | --- |
| Esri | `SearchPlaceIndexForText`, `SearchPlaceIndexForSuggestions` | Filter by *Place types* and *Point of interest categories*. | Categories are returned by `SearchPlaceIndexForText`, `SearchPlaceIndexForPosition`, and `GetPlace` |
| Here | `SearchPlaceIndexForText`, `SearchPlaceIndexForSuggestions` | Filter by *Place types* only. | Categories are returned by `SearchPlaceIndexForText` and `SearchPlaceIndexForSuggestions`, `SearchPlaceIndexForPosition`, and `GetPlace` |
| Grab | not supported | not supported | not supported |
| Open Data | n/a (searching places not supported) | n/a | n/a |
