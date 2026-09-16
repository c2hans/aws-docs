---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-geocoding.html
---

# Geocoding using Amazon Location
<a name="search-place-index-geocoding"></a>

Geocoding is a process that converts text, such as an address, a region, a business name, or point of interest, into a set of geographic coordinates. You can use place index resources to submit geocoding requests and incorporate data retrieved from geocoding to display data on a map for your web or mobile application.

This section guides you through how to send a simple geocoding request, and how to send geocoding requests with optional specifications.

## Geocoding
<a name="geocoding"></a>

You can submit a simple request to geocode using the `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` operation to convert an address to a set of coordinates. A simple request contains the following required parameter:

**Note**
In the latest API, use `[Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html)` for addresses and `[SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html)` for free-form place and business queries, under `geo-places`. Neither requires a place index resource.
+ `Text` – An address, name, city, or region to convert to a set of coordinates. For example, the string `Any Town`.

To specify a maximum number of results per pages, use the following optional parameter:
+ `MaxResults` – Limits the maximum number of results returned in the query response.

You can use the AWS CLI or the Amazon Location APIs.

------
#### [ API ]

The following example is a `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` request to search the place index resource, {{ExamplePlaceIndex}}, for an address, name, city or region called {{Any Town}}.

```
POST /places/v0/indexes/{{ExamplePlaceIndex}}/search/text
Content-type: application/json

{
    "Text": "{{Any Town}}",
    "MaxResults": 10
}
```

------
#### [ AWS CLI ]

The following example is a `[search-place-index-for-text](https://docs.aws.amazon.com/cli/latest/reference/location/search-place-index-for-text.html)` command to search the place index resource, {{ExamplePlaceIndex}}, for an address, name, city or region called {{Any Town}}.

```
aws location \
    search-place-index-for-text \
        --index-name {{ExamplePlaceIndex}} \
        --text "{{Any Town}}" \
        --max-results 10
```

------

## Geocode near a position
<a name="geocoding-near"></a>

When geocoding, you can geocode near a given position with the following optional parameter:
+ `BiasPosition` – The position you want to search nearby. This narrows your search by searching for results closest to the given position. Defined as `[longitude, latitude]`

The following example is a `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` request to search the place index resource for an address, name, city or region called {{Any Town}} near the position [{{-123.4567}},{{45.6789}}].

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json

{
   "Text": "Any Town",
   "BiasPosition": [{{-123.4567}},{{45.6789}}]
}
```

## Geocode within a bounding box
<a name="geocoding-bbox"></a>

You can geocode within a bounding box to narrow your results to coordinates within a given boundary using the following optional parameter:
+ `FilterBBox` – A bounding box that you specify to filter your results to coordinates within the box's boundaries. Defined as `[LongitudeSW, LatitudeSW, LongitudeNE, LatitudeNE]`
**Note**
A request can't contain both the `FilterBBox` and `BiasPosition` parameters. Specifying both parameters in the request returns a `ValidationException` error.

The following example is a `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` request to search within a bounding box for an address, name, city or region called {{Any Town}}. The bounding box follows that:
+ The longitude of the southwest corner is {{-124.1450}}.
+ The latitude of the southwest corner is {{41.7045}}.
+ The longitude of the northeast corner is {{-124.1387}}.
+ The latitude of the northeast corner is {{41.7096}}.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json

{
   "Text": "Any Town",
   "FilterBBox":  [
        {{-124.1450}},{{41.7045}},
        {{-124.1387}},{{41.7096}}
    ]
}
```

## Geocode within a country
<a name="geocoding-filtercountry"></a>

You can geocode within one or more countries you specify by using the following optional parameter:
+ `FilterCountries` – The country or region you want to geocode within. You can define up to 100 countries in one request using a [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) three letter country code. For example, use `AUS` for Australia.

The following example is a `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` request to search for an address, name, city or region called {{Any Town}} in Germany and France.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json

{
   "Text": "Any Town",
   "FilterCountries": ["{{DEU}}","{{FRA}}"]
}
```

## Filtering by category
<a name="geocoding-filtercategories"></a>

You can filter the categories that are returned in your geocode request by using the following optional parameter:
+ `FilterCategories` – The categories of results you want returned in your query. You can specify up to 5 categories in one request. You can find the list of Amazon Location Service categories in the [Categories](category-filtering.md) section. For example, you can specify `Hotel` to specify only returning hotels in your query.

The following example is a `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` request to search for an coffee shop called {{Hometown Coffee}} in the United States.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json

{
   "Text": "Hometown Coffee",
   "FilterCategories": ["Coffee Shop"],
   "FilterCountries": ["USA"]
}
```

For more details about filtering on categories, see [Place categories and filtering results with Amazon Location](category-filtering.md)

## Geocode in a preferred language
<a name="geocoding-language"></a>

You can set a language preference for results of your search by using the optional `Language` parameter. For example, a search for **100 Main St, Anytown, USA** may return `100 Main St, Any Town, USA` by default. But if you select `fr` as the `Language`, then the results may return `100 Rue Principale, Any Town, États-Unis` instead.
+ `Language` – A language code to use for rendering the results of your query. The value must be a valid [BCP 47](https://www.rfc-editor.org/info/bcp47) language code. For example, `en` for English.

**Note**
If `Language` is not specified, or the specified language is not supported for a result, the partner's default language for that result will be used.

The following example is a `SearchPlaceIndexforText` request to search for a place called **Any Town** with the preferred language specified as `de`.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json
{
   "Text": "Any Town",
   "Language": "de"
}
```

## Example response
<a name="geocoding-example-response"></a>

**Example**
The following is an example response when you call the `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)` operation from the Amazon Location Places APIs. The results include relevant [places](https://docs.aws.amazon.com/location/previous/APIReference/API_Place.html) and the request [summary](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForTextSummary.html). Two responses are shown, based on selecting Esri or HERE as the partner.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/text
Content-type: application/json

{
   "Text": "Amazon",
   "MaxResults": 1,
   "FilterCountries": ["USA"],
   "BiasPosition": [-112.10, 46.32]
}
```

```
{
    "Results": [
        {
            "Place": {
                "Country": "USA",
                "Geometry": {
                    "Point": [
                        -112.10667999999998,
                        46.319090000000074
                    ]
                },
                "Interpolated": false,
                "Label": "Amazon, MT, USA",
                "Municipality": "Amazon",
                "Region": "Montana",
                "SubRegion": "Jefferson County"
            },
            "Distance": 523.4619749879726,
            "Relevance": 1
        }
    ],
    "Summary": {
        "BiasPosition": [
            -112.1,
            46.32
        ],
        "DataSource": "Esri",
        "FilterCountries": [
            "USA"
        ],
        "MaxResults": 1,
        "ResultBBox": [
            -112.10667999999998,
            46.319090000000074,
            -112.10667999999998,
            46.319090000000074
        ],
        "Text": "Amazon"
    }
}
```

```
{
    "Summary": {
        "Text": "Amazon",
        "BiasPosition": [
            -112.1,
            46.32
        ],
        "FilterCountries": [
            "USA"
        ],
        "MaxResults": 1,
        "ResultBBox": [
            -112.10668,
            46.31909,
            -112.10668,
            46.31909
        ],
        "DataSource": "Here"
    },
    "Results": [
        {
            "Place": {
                "Label": "Amazon, Jefferson City, MT, United States",
                "Geometry": {
                    "Point": [
                        -112.10668,
                        46.31909
                    ]
                },
                "Neighborhood": "Amazon",
                "Municipality": "Jefferson City",
                "SubRegion": "Jefferson",
                "Region": "Montana",
                "Country": "USA",
                "Interpolated": false,
                "TimeZone": {
                    "Name": "America/Denver",
                    "Offset": -25200
                }
            },
            "PlaceId": "AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ",            "Distance": 523.4619749905755
        }
    ]
}
```
