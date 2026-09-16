---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-autocomplete.html
---

# Autocomplete using Amazon Location
<a name="search-place-index-autocomplete"></a>

Autocomplete provides responsive feedback to end users as they are typing their search query. It provides suggestions for addresses and points of interest based on partial or misspelled free-form text. You can use place index resources to request autocomplete suggestions, and display the resulting suggestions in your application.

Amazon Location does not support storage of autocomplete suggestions. An error is returned if the place index used for an autocomplete call is configured for use with stored geocodes. To use stored geocodes and query for suggestions, create and configure multiple place indexes.

This section describes how to send an autocomplete request. It starts with the most basic form of the request, and then shows optional parameters that you can use to increase the relevance of autocomplete search results.

## Using autocomplete
<a name="autocomplete"></a>

You can submit a simple request for autocomplete suggestions by using the `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` operation. The simplest form of the request has a single required parameter, the query `Text`:

**Note**
In the latest API, use `[Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html)` or `[Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html)` under `geo-places`. Neither requires a place index resource.
+ `Text` – The free-form partial text to use to generate place suggestions. For example, the string `eiffel tow`.

To limit the number of results returned, add the optional `MaxResults` parameter:
+ `MaxResults` – Limits the number of results returned in the query response.

You can use the Amazon Location APIs or the AWS CLI.

------
#### [ API ]

The following example is a `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` request to search the place index resource, {{ExamplePlaceIndex}}, for up to {{5}} suggestions based on the partial place name {{kamp}}.

```
POST /places/v0/indexes/{{ExamplePlaceIndex}}/search/suggestions
Content-type: application/json

{
    "Text": "{{kamp}}",
    "MaxResults": {{5}}
}
```

------
#### [ AWS CLI ]

The following example is a `[search-place-index-for-suggestions](https://docs.aws.amazon.com/cli/latest/reference/location/search-place-index-for-suggestions.html)` command to search the place index resource, {{ExamplePlaceIndex}}, for up to {{5}} suggestions based on the partial place name {{kamp}}.

```
aws location \
              search-place-index-for-suggestions \
              --index-name {{ExamplePlaceIndex}} \
              --text {{kamp}} \
              --max-results 5
```

------

The call to `SearchPlaceIndexForSuggestions` results in a list of places with a name and an ID for each. You can use those results to present suggestions of what the user might be searching for, as they are typing, such as providing a dropdown list of choices underneath a text box. For example, here are the results for suggestions, based on a user typing {{kamp}}.

```
{
    "Summary": {
        "Text": "kamp",
        "MaxResults": 5,
        "DataSource": "Esri"
    },
    "Results": [
        {
            "Text": "Kampuchea",
            "PlaceId": "AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ"
        },
        {
            "Text": "Kampoul, Kabul, AFG",
            "PlaceId": "AQAAAIAAA1mxl_-9ffzXD07rBgo9fh6E01Pd1YKvuT5rz2qBDxqBkhTlgkeiOPR2s5sa3YBLxUqQI8bhymsYcu9R-DkX3L9QSi3CB5LhNPu160iSFJo6H8S1CrxO3QsJALhrr9mdbg0R4R4YDywkhkeBlnbn7g5C5LI_wYx873WeQZuilwtsGm8jcMA0Ya5oK4netQC6piVx6zmnPdwBs-UeXcb_bg"
        },
        {
            "Text": "Kampala, UGA",
            "PlaceId": "AQAAAIAAzZfZt3qMruKGObyhP6MM0pqy2L8SULlVWT7a3ertLBRS6Q5n7I4s9D7E0nRHADAj7mL7kvX1Q8HD-mpuiATXNJ1Ix4_V_1B15zHe8jlYKMWvXbgbO8cMpgR2fqYqZMR1x-dfBOO8OoqujKZldvPIDK1kNe3GwcaqvvMWWPMeaGd203brFynubAe-MmFF-Gjz-WBMfUy9og6MV7bkk6NGCA"
        },
        {
            "Text": "Kampar, Riau, IDN",
            "PlaceId": "AQAAAIAAvbXXx-srOi111tHOkPdao0GF7WQ_KaZ444SEnevycp6Gtf_2JWgPfCE5bIQCYwya1uZQpX2a8YJoFm2K7Col4fLu7IK0yYOLhZx4kp6QzbG4xEAGzfWtWq6nfbb0lZfuHY6r0g1sRlN1aucvwim4AEcKRzckqaa93JI8064pj6Q59kN37pAa3JX4ayEzH1DzIL3m3oqxzd4O16yGfhAIgA"
        },
        {
            "Text": "Kampung Pasir Gudang Baru, Johor, MYS",
            "PlaceId": "AQAAAIAA4HLQHdjUDcaaXLE9wtNIT1cjQYLgkBnMoG2eNN0AaQ8PJoWabLRXmmPUaAj8MAD6vT0i6zqaun5Mixyj7vnYXrk2xp59cbgdqvQaPoWhSCVxBOX0WGs3cZ8TnIRn3c-6v8_UfmqC7es1gUyECfMGK04VBKiwpHwCzjNsqymkd9BC3A9K3QlMgd3dkrGjv_vV94iLlnFTbaecrckl2UDCkA"
        }
    ]
}
```

The next section explains how to use the `PlaceID` from these results.

## Using the autocomplete results
<a name="autocomplete-results"></a>

The call to `SearchPlaceIndexForSuggestions` results in a list of places with a name and an ID for each. You can use those results to present suggestions of what the user might be searching for, as they are typing, such as providing a dropdown list of choices underneath a text box. When the user chooses one of the results, you can then call the [GetPlace](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html) operation with the ID of their selection to return the details of that place, including location, address, or other details.

**Note**
A `PlaceId` is valid only if all of the following are the same in the original search request, and the call to `GetPlace`.
Customer AWS account
AWS Region
Data provider specified in the place index resource

Typically, you use `GetPlace` with the Amazon Location APIs. The following example is a `[GetPlace](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html)` request to find one of the suggestions from the previous section. This example is based on the partial place name {{kamp}}.

```
POST /places/v0/indexes/{{ExamplePlaceIndex}}/places/{{AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ}}
```

## Autocomplete near a position
<a name="autocomplete-near"></a>

 When you search for autocomplete place suggestions by using `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)`, you can get more locally-relevant suggestions by adding the following optional parameter:
+ `BiasPosition` – The position you want to search nearby. Defined as `[longitude, latitude]`.

The following example uses a `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` request to search the place index resource {{ExamplePlaceIndex}} for place suggestions matching the partial query {{kamp}} near the position [{{32.5827}},{{0.3169}}].

```
POST /places/v0/indexes/ExamplePlaceIndex/search/suggestions
Content-type: application/json

{
    "Text": "{{kamp}}",
    "BiasPosition": [{{32.5827}},{{0.3169}}]
}
```

The suggestions returned for the same `Text` can be different if a different `BiasPosition` is chosen, such as [{{-96.7977}}, {{32.7776}}].

## Autocomplete within a bounding box
<a name="autocomplete-bbox"></a>

You can narrow your autocomplete search to receive only suggestions for places which are located within a given boundary by adding the following optional parameter:
+ `FilterBBox` – A bounding box that you specify to filter your results to coordinates within the box's boundaries. Defined as `[LongitudeSW, LatitudeSW, LongitudeNE, LatitudeNE]`
**Note**
A request can't contain both the `FilterBBox` and `BiasPosition` parameters. Specifying both parameters in the request returns a `ValidationException` error.

The following example uses a `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` request to search the place index resource {{ExamplePlaceIndex}} for place suggestions matching the partial query {{kamp}}, and which are contained within the bounding box where:
+ The longitude of the southwest corner of the bounding box is {{32.5020}}.
+ The latitude of the southwest corner of the bounding box is {{0.2678}}.
+ The longitude of the northeast corner of the bounding box is {{32.6129}}.
+ The latitude of the northeast corner of the bounding box is {{0.3502}}.

```
POST /places/v0/indexes/ExamplePlaceIndex/search/suggestions
Content-type: application/json

{
    "Text": "{{kamp}}",
    "FilterBBox": [
        {{32.5020}}, {{0.2678}},
        {{32.6129}}, {{0.3502}}
    ]
}
```

 The suggestions returned for the same `Text` are different if a different `FilterBBox` is chosen, such as [{{-97.9651}}, {{32.0640}}, {{ -95.1196}}, {{34.0436}}].

## Autocomplete within a country
<a name="autocomplete-country"></a>

You can narrow your autocomplete search to receive only suggestions for places which are located within a given country, or set of countries, by adding the following optional parameter:
+ `FilterCountries` – The countries you want to search for place suggestions within. You can specify up to 100 countries in one request using a [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) three-letter country code. For example, use `AUS` for Australia.

 The following example uses a `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` request to search the place index resource {{ExamplePlaceIndex}} for place suggestions matching the partial query {{kamp}} and which are contained within Uganda, Kenya, or Tanzania:

```
POST /places/v0/indexes/ExamplePlaceIndex/search/suggestions
Content-type: application/json

{
    "Text": "kamp",
    "FilterCountries": ["{{UGA}}", "{{KEN}}", "{{TZA}}"]
}
```

 The suggestions returned for the same `Text` are different if a different `FilterCountries` list is chosen, such as ["{{USA}}"].

## Example response
<a name="autocomplete-basic-response"></a>

The following is an example response of suggested autocompletions for the `[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)` operation, using the text {{kamp}}.

```
{
    "Summary": {
        "Text": "kamp",
        "MaxResults": 5,
        "DataSource": "Esri"
    },
    "Results": [
        {
            "Text": "Kampuchea",
            "PlaceId": "AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ"
        },
        {
            "Text": "Kampoul, Kabul, AFG",
            "PlaceId": "AQAAAIAAA1mxl_-9ffzXD07rBgo9fh6E01Pd1YKvuT5rz2qBDxqBkhTlgkeiOPR2s5sa3YBLxUqQI8bhymsYcu9R-DkX3L9QSi3CB5LhNPu160iSFJo6H8S1CrxO3QsJALhrr9mdbg0R4R4YDywkhkeBlnbn7g5C5LI_wYx873WeQZuilwtsGm8jcMA0Ya5oK4netQC6piVx6zmnPdwBs-UeXcb_bg"
        },
        {
            "Text": "Kampala, UGA",
            "PlaceId": "AQAAAIAAzZfZt3qMruKGObyhP6MM0pqy2L8SULlVWT7a3ertLBRS6Q5n7I4s9D7E0nRHADAj7mL7kvX1Q8HD-mpuiATXNJ1Ix4_V_1B15zHe8jlYKMWvXbgbO8cMpgR2fqYqZMR1x-dfBOO8OoqujKZldvPIDK1kNe3GwcaqvvMWWPMeaGd203brFynubAe-MmFF-Gjz-WBMfUy9og6MV7bkk6NGCA"
        },
        {
            "Text": "Kampar, Riau, IDN",
            "PlaceId": "AQAAAIAAvbXXx-srOi111tHOkPdao0GF7WQ_KaZ444SEnevycp6Gtf_2JWgPfCE5bIQCYwya1uZQpX2a8YJoFm2K7Col4fLu7IK0yYOLhZx4kp6QzbG4xEAGzfWtWq6nfbb0lZfuHY6r0g1sRlN1aucvwim4AEcKRzckqaa93JI8064pj6Q59kN37pAa3JX4ayEzH1DzIL3m3oqxzd4O16yGfhAIgA"
        },
        {
            "Text": "Kampung Pasir Gudang Baru, Johor, MYS",
            "PlaceId": "AQAAAIAA4HLQHdjUDcaaXLE9wtNIT1cjQYLgkBnMoG2eNN0AaQ8PJoWabLRXmmPUaAj8MAD6vT0i6zqaun5Mixyj7vnYXrk2xp59cbgdqvQaPoWhSCVxBOX0WGs3cZ8TnIRn3c-6v8_UfmqC7es1gUyECfMGK04VBKiwpHwCzjNsqymkd9BC3A9K3QlMgd3dkrGjv_vV94iLlnFTbaecrckl2UDCkA"
        }
    ]
}
```
