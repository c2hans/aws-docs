---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonlocationserviceplaces.html
---

# Data retrieval APIs for Amazon Location Service Places
<a name="amazonlocationserviceplaces"></a>

Amazon Location Service Places provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="geo-places-Autocomplete"></a>[Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html) | Autocomplete text input with potential places and addresses as the user types | Read |
| <a name="geo-places-Geocode"></a>[Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html) | Geocode a textual address or place into geographic coordinates | Read |
| <a name="geo-places-GetPlace"></a>[GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html) | Query a place by it's unqiue place ID | Read |
| <a name="geo-places-ReverseGeocode"></a>[ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html) | Convert geographic coordinates into a human-readable address or place | Read |
| <a name="geo-places-SearchNearby"></a>[SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html) | Retrieve places near a position which match to a set of user defined restrictions such as category or food type offered by the place | Read |
| <a name="geo-places-SearchText"></a>[SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html) | Query for places using a single free-form text input | Read |
| <a name="geo-places-Suggest"></a>[Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html) | Suggest potential places based on the user's input | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
