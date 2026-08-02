---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/searching-for-places.html
---

# Searching place and geolocation data using Amazon Location
<a name="searching-for-places"></a>

**Note**
We released a new version of the Places API, see the updated [Places Developer Guide](https://docs.aws.amazon.com//location/latest/developerguide/places.html) or [Places API](https://docs.aws.amazon.com//location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html) for revised information.

Amazon Location includes the ability to search the geolocation, or *place*, data of your chosen provider. There are several kinds of searching available.
+ **Geocoding** – Geocoding is the process of searching for addresses, regions, business names, or other points of interest, based on text input. It returns details and the location (in latitude and longitude) of the results found.
+ **Reverse geocoding** – Reverse geocoding allows you to find places near a given location.
+ **Autocomplete** – Autocomplete is the process of making automatic suggestions as the user types in a query. For example, if they type **Par** one suggestion might be `Paris, France`.

Amazon Location lets you choose a data provider for place search operations by creating and configuring a place index resource.

Once you create your resource, you can send requests using the AWS SDK for your preferred language, Amplify, or the REST API endpoints. You can use data from the response to mark locations on a map, enrich position data, and to convert positions into human-readable text.

**Note**
For an overview of searching place concepts, see [Learn about Places search in Amazon Location Service](places-concepts.md).

**Topics**
+ [Places prerequisites using Amazon Location](places-prerequisites.md)
+ [Geocoding using Amazon Location](search-place-index-geocoding.md)
+ [Reverse geocoding using Amazon Location](search-place-index-reverse-geocode.md)
+ [Autocomplete using Amazon Location](search-place-index-autocomplete.md)
+ [Use place IDs with Amazon Location](search-using-placeids.md)
+ [Place categories and filtering results with Amazon Location](category-filtering.md)
+ [Amazon Aurora PostgreSQL user-defined functions for Amazon Location Service](database-address-validation.md)
+ [Managing your place index resources with Amazon Location](managing-place-indexes.md)
