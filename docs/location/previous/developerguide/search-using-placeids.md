---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/search-using-placeids.html
---

# Use place IDs with Amazon Location
<a name="search-using-placeids"></a>

Searching for places returns a list of results. Most results include a `PlaceId` for that result. You can use a `PlaceId` in a `[GetPlace](https://docs.aws.amazon.com/location-places/latest/APIReference/API_GetPlace.html)` operation to return the information about that place (including name, address, location, or other details).

**Note**
Using [SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForSuggestions.html) will return `PlaceId` results for any place indexes created with any data source. Using [SearchPlaceIndexForText](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html) or [SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForPosition.html) will return a `PlaceId` only if the data source used is HERE.

Each `PlaceId` uniquely defines the place it refers to, but a single place can have more than one `PlaceId` over time, and based on the context. The following rules describe the uniqueness and longevity of a `PlaceId`.
+ The `PlaceId` returned in calls that you make is specific to your AWS account, to the AWS Region, and to the data provider in your `PlaceIndex` resource. `GetPlace` will find results only when these three attributes match the original call that created the `PlaceId`.
+ The `PlaceId` for a place will change when the data about that place changes. For example, when the business that it refers to moves location or changes names.
+ The `PlaceId` returned from a repeated search call may change when the backend service makes an update. The older `PlaceId` will continue to be found, but new calls to search may return a different ID.

The `PlaceId` is a string. There is no specific limit to the length of a `PlaceId`. The following is an example of a valid `PlaceId`.

```
AQAAAIAADsn2T3KdrRWeaXLeVEyjNx_JfeTsMB0NVCEAnAZoJ-o3nqdlJZAdgcT2oWi1w9pS4wXXOk3O1vsKlGsPyHjV4EJxsu289i3hVO_BUPgP7SFoWAi8BW2v7LvAjQ5NfUPy7a1v9ajT3feIqcUZszWSTqKbJHFYvQqW7wdqhpQq3Wy-et39ZQDWSPLZUzgcjN-6VD2gyKkH0Po7gSm8YSJNSQ
```

Calling `GetPlace` with a `PlaceId` for a place whose data has changed (for example, a business location that has gone out of business), will result in a `404`, `ResourceNotFound` error. Calling `GetPlace` with a `PlaceId` that is not valid, or one out of context, such as from another AWS account, will return a `400`, `ValidationException` error.

While you can use PlaceID in subsequent requests, PlaceID is not intended to be a permanent identifier and the ID can change between consecutive API calls. Please see the following PlaceID behaviour for each data provider:
+ **Esri**: Place IDs will change every quarter at a minimum. The typical time period for these changes would be March, June, September, and December. Place IDs might also change between the typical quarterly change but that will be much less frequent.
+ **HERE**: We recommend that you cache data for no longer than a week to keep your data data fresh. You can assume that less than 1% ID shifts will release over release which is approximately 1 - 2 times per week.
+ **Grab**: Place IDs can expire or become invalid in the following situations.
  + **Data operations**: The POI may be removed from Grab POI database by Grab Map Ops based on the ground-truth, such as being closed in the real world, being detected as a duplicate POI, or having incorrect information. Grab will synchronize data to the Waypoint environment on weekly basis.
  + **Interpolated POI**: Interpolated POI is a temporary POI generated in real time when serving a request, and it will be marked as derived in the `place.result_type` field in the response. The information of interpolated POIs will be retained for at least 30 days, which means that within 30 days, you are able to obtain POI details by Place ID from Place Details API. After 30 days, the interpolated POIs(both Place ID and details) may expire and inaccessible from the Places Details API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
