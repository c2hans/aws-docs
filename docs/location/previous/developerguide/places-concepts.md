---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/places-concepts.html
---

# Learn about Places search in Amazon Location Service
<a name="places-concepts"></a>

**Note**
We released a new version of the Places API, see the updated [Places Developer Guide](https://docs.aws.amazon.com//location/latest/developerguide/places.html) for revised information.

A key function of Amazon Location Service is the ability to search the geolocation information. Amazon Location provides this functionality via the *Place index* resource.

**Note**
For information about how to use place index resources to search in practice, see [Searching place and geolocation data using Amazon Location](searching-for-places.md).

You can use the place index APIs to search for:
+ Points of interest, such as restaurants and landmarks. Search by name, and optional location to search around, and receive a list of options ordered by relevance.
+ A street address, receiving a latitude and longitude for that address. This is known as *geocoding*.
+ A latitude and longitude position, receiving the associated street address or other information about the location. This is known as *reverse geocoding*.
+ A partial or misspelled free-form text query, typically as a user types. This is known as *autocomplete*, autosuggest, or fuzzy matching.

The place index includes which data provider to use for the search.

**Note**
Map data and other geolocation information, including exact locations, can vary across data providers. As a best practice, use the same data provider for your place index, map, and other Amazon Location resources. For example, if the places returned by your place index do not match the location of the same places provided by your map resource, you can place a marker in what appears to be the wrong location on the map.

The following shows you how to create and use place index resources:

![User click flows through SDK to place index resource using geographic coordinates.](http://docs.aws.amazon.com/location/previous/developerguide/images/illustration-places.PNG)

1. First, you create a place index resource in your AWS account by selecting a data provider.

1. You can then select and install the SDK that matches your development environment and applications. For more information about available options, see the topic about [Accessing Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/how-to-access.html).

1. Start using the Amazon Location Places APIs . For more information, see the topic about using [Places search](searching-for-places.md).

1. You can then integrate monitoring using services such as Amazon CloudWatch and AWS CloudTrail. For more information see, [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## Geocoding concepts
<a name="geocoding-concepts"></a>

An Amazon Location place index provides an action called [https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html) that allows you to specify text to search. For example, you can search for:
+ **Places** – a search for **Paris** could return the location of the city in France.
+ **Businesses** – a search for **coffee shop** could return a list of coffee shops, including their names and locations. You can also specify a location to search around or a bounding box to search within, to make the results more relevant. In this case, providing a location in downtown Seattle, Washington, would return coffee shops in that area.
+ **Addresses** – a search for **1600 Pennsylvania Ave, Washington D.C.** could return the location of the White House in the United States (which is at that address).

Searching for text in this way is generally referred to as **geocoding**, which involves finding a geographic location for the address or place.

Amazon Location Service also provides a **reverse geocoding** action called [https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html). This takes a geographic location and returns the address, business, or other information about what is at that location.

## Search results
<a name="search-results-concepts"></a>

When you make a successful search request in Amazon Location Service, one or more results are returned. Each result includes a label, which is the name or description of the result. For example, a search for **coffee shop**, might return a result with the label `Hometown Cafe`, telling you that a coffee shop called "Hometown Cafe" was found. The search result will also typically include a structured address (with properties such as the address number, unit, street, and postal code). Depending on the data provider, it will include other meta data, as well, such as the country and time zone.

For a search on a business name or category (such as **coffee shop**), you might want to show all returned results on a map. For an address search, you might want to just use the first result automatically. See the next topic for information about relevance.

## Multiple results and relevance
<a name="relevance-concepts"></a>

When searching by text, Amazon Location Service will often find more than a single result. For example, a search for **Paris** may return the city in France, but also the city in Texas. The results are sorted by the relevance, as determined by the data provider.

**Note**
Results are returned in relevance order from all providers. If you choose Esri or Grab as your data provider, the results include a relevance value that you can use to understand the relative relevance between the results of a single request.

Specifying additional information, such as a country name, or a location to search around, can change the order of results, reduce the number of results, or even change the set of results returned. For example, a search for **Paris** with a location in Texas to search around is more likely to return `Paris, Texas` as the first result than `Paris, France`.

In an interactive application, you can use relevance to help decide whether to accept the top result, or to ask a user to disambiguate between multiple returned results. If the first result has a high relevance, you might just accept it as the correct answer. If there are multiple high relevance results, or no high relevance results, you might want to list the results and let the user select the best result.

## Address results
<a name="address-concepts"></a>

You can search for addresses with Amazon Location Service using the same [https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html) action. The more information that you provide, the more likely the address returned will match the one given. For example, **123 Main St** is less likely to find a correct result than **123 Main St, Anytown, California, 90210**.

Addresses have multiple attributes, such as the street number, street, city, region, and postal code, etc. Those attributes are used to find an address in the place index that matches as many aspects as possible. The more attributes found, the more relevant the match is considered, and the more likely it will be returned.

**Note**
The relevance for address results is based on how closely the result matches the input. This could be the number of the attributes that matched, but also how closely the results match the input. For example, an input of **123 Main St** would have a higher relevance when `Main St` is found in the data, than if `Maine St` is the only result. `Maine St` will still be returned, but likely with a lower relevance value.

The search results include a label for the full address (`123 Main St, Anytown, California, 90210`), but also the individual structured attributes of the returned address. This is helpful, because you can use that, for example, to populate address fields in a database, or to examine the results and find the city, region, or postal code of the found location.

**Interpolation**

Addresses in the place index data includes exact address matches. For example, suppose that there is a street, `9th street` and one block has 2 houses, `220` and `240`, as in the following image.

![A map of a single block with two existing houses, and one new house added between them.](http://docs.aws.amazon.com/location/previous/developerguide/images/address-inference.png)

The data provider creates the geolocation data with those two known addresses. You can search for those two addresses, and they are found. After the data provider creates the map data, let's suppose that a new house is added, between the first two addresses. This new house is given the address `230`. If you search for **230 S 9th St**, the data provider will still find a result. Instead of using a known address, it will interpolate between the already known addresses, and estimate the position of the new address from those. In this case, it might assume that 230 is halfway between 220 and 240 (and on the same side of the street), and return an approximate location based on that.

**Note**
Data providers periodically update their geolocation data with new addresses. In this case, `230 S 9th St` would get added to the data provider data, but there will typically be a period when a new address has been created but is not yet added to the data.

In this case, the data provider can't tell whether the new address exists in the world, as it is not yet in the data, but provides the best answer it can from the information it has. This result is called *interpolated*, and can be returned by the data provider in the results. If `interpolated` returns `false`, it is a known address. If it returns `true`, it's an approximated address. If it's not returned, then the data provider did not provide the information about whether the result came from interpolation.

**Important**
The data provider may also return interpolated results for addresses that don't exist at all. For example in this case, if you entered **232 S 9th St**, the provider would find this nonexistent address, and return a location close to 230, but on the 240 side. Interpolated addresses are useful for getting you to the right location, but it is good to keep in mind that they are not known addresses.

## Storing geocode results
<a name="geocode-storage-concepts"></a>

When you create a place index resource, you must specify a **Data storage option** (called `IntendedUse` in the API). That can set to be either *single use* or *stored results*. This is asking about your intended use of the results. If you are going to store the results (even for caching purposes), you must choose the *storage* option, not the *single use* option.

**Note**
When you chose the stored option (labeled as **Yes, results will be stored** in the console, or choosing `storage` in the `CreatePlaceIndex` API), Amazon Location Service does not store the results for you. This is an indication that you are planning to store the results.

When looking at how you are going to use the results of your queries to Amazon Location Service, you should always be aware of the [AWS Service Terms](https://aws.amazon.com/service-terms/) that apply.

## Places terminology
<a name="places-components"></a>

**Place index resource**
Allows you to choose a data source to support search queries. For example, you can search for points of interest, addresses, or coordinates. When a search query is sent to a place index resource, it's fulfilled using the resource's configured data source.

**Geocoding**
Geocoding is the process of taking a text input, searching for it in the place index, and returning results with position.

**Reverse geocoding**
Reverse geocoding is the process of taking a position and returning information about that position from within the place index, such as the address, city, or business at that location.

**Relevance**
Relevance is how closely a result matches the input. It is not a measure of correctness.

**Interpolation**
Interpolation is the process of finding unknown addresses by using known address locations as guide points.

**ISO 3166 country codes **
Amazon Location Service Places uses [the International Organization for Standardization (ISO) 3166 ](https://www.iso.org/iso-3166-country-codes.html) country codes to refer to countries or regions.
To find the code for a specific country or region, use the[ ISO Online Browsing Platform](https://www.iso.org/obp/ui/#search).
