---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-reverse-geocode.html
---

# Reverse geocoding using Amazon Location
<a name="search-place-index-reverse-geocode"></a>

Reverse geocoding is a process that converts a set of coordinates into meaningful text, such as an address, a region, a business name, or point of interest. You can use place index resources to submit reverse geocoding requests and incorporate data retrieved from reverse geocoding to display data on a map for your web or mobile application.

This section guides you through how to send a simple reverse geocoding request.

## Reverse geocoding
<a name="reverse-geocode"></a>

You can submit a simple request to reverse geocode a set of coordinates and convert them to a meaningful address, a point of interest or a general location without an address using the `[SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html)` operation. A simple request contains the following required parameter:
+ `Position` – A set of coordinates that you want to convert to an address, point of interest, or general location. Defined using the format `[longitude,latitude]`.

To specify a maximum number of results per pages, add the following optional parameter:
+ `MaxResults` – Limits the maximum number of results returned in the query response.

If you want to specify a preferred language for the results of your query, use the following optional parameter:
+ `Language` – A language code to be used for rendering results. The value must be a valid [BCP 47](https://www.rfc-editor.org/info/bcp47) language code. For example, `en` for English.

**Note**
If `Language` is not specified, or the specified language is not supported for a result, the partner's default language for that result will be used.

You can use the AWS CLI or the Amazon Location APIs.

------
#### [ API ]

The following example is a `[SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html)` request to search the place index resource, {{ExamplePlaceIndex}}, for a meaningful address, point of interest or general location near the position [{{122.3394}},{{47.6159}}].

```
POST /places/v0/indexes/{{ExamplePlaceIndex}}/search/position
Content-type: application/json

{
   "Position": [{{-122.3394}},{{47.6159}}],
   "MaxResults": 5,
   "Language": "de"
}
```

------
#### [ AWS CLI ]

The following example is a `[search-place-index-for-position](https://docs.aws.amazon.com/cli/latest/reference/location/search-place-index-for-position.html)` command to search the place index resource, {{ExamplePlaceIndex}}, for a meaningful address, point of interest or general location near the position [{{122.3394}},{{47.6159}}].

```
aws location \
    search-place-index-for-position \
        --index-name {{ExamplePlaceIndex}} \
        --position {{-122.3394}} {{47.6159}} \
        --max-results 5 \
        --language de
```

------

## Example response
<a name="reverse-geocoding-example-response"></a>

**Example**
The following is an example response when calling the `[SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html)` operation from the Amazon Location Places APIs. The results return relevant [places](https://docs.aws.amazon.com/location-places/latest/APIReference/API_Place.html) and the request [summary](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPositionSummary.html). Two responses are shown, based on selecting Esri or Here as the partner.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/position
Content-type: application/json

{
   "Position": [-122.3394,47.6159],
   "MaxResults": 1
}
```

```
{
    "Results": [
        {
            "Place": {
                "AddressNumber": "2111",
                "Country": "USA",
                "Geometry": {
                    "Point": [
                        -122.33937999999995,
                        47.61591000000004
                    ]
                },
                "Interpolated": false,
                "Label": "The Spheres, 2111 7th Ave, Seattle, WA, 98121, USA",
                "Municipality": "Seattle",
                "Neighborhood": "Belltown",
                "PostalCode": "98121",
                "Region": "Washington",
                "SubRegion": "King County"
            },
            "Distance": 1.8685861313438727
        }
    ],
    "Summary": {
        "DataSource": "Esri",
        "MaxResults": 1,
        "Position": [
            -122.3394,
            47.6159
        ]
    }
}
```

```
{
    "Summary": {
        "Position": [
            -122.3394,
            47.6159
        ],
        "MaxResults": 1,
        "DataSource": "Here"
    },
    "Results": [
        {
            "Place": {
                "Label": "2111 7th Ave, Seattle, WA 98121-5114, United States",
                "Geometry": {
                    "Point": [
                        -122.33938,
                        47.61591
                    ]
                },
                "AddressNumber": "2111",
                "Street": "7th Ave",
                "Neighborhood": "Belltown",
                "Municipality": "Seattle",
                "SubRegion": "King",
                "Region": "Washington",
                "Country": "USA",
                "PostalCode": "98121-5114",
                "Interpolated": false,
                "TimeZone": {
                    "Name": "America/Los_Angeles",
                    "Offset": -28800
                }
            },
            "PlaceId": "AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ",
            "Distance": 1.868586125090601
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
