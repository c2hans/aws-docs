---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-place-cross-references.html
---

# How to get cross-references for a place
<a name="how-to-get-place-cross-references"></a>

Use `CrossReferences` in the `AdditionalFeatures` parameter to retrieve third-party supplier identifiers for a place. This enables you to correlate the place with entries in external systems such as Yelp and TripAdvisor.

## Potential use cases
<a name="get-place-cross-references-use"></a>
+ **Review aggregation:** Link a place to its profile on review platforms to display user ratings.
+ **Data reconciliation:** Match place records across your internal systems and third-party databases.

## Examples
<a name="get-place-cross-references-example"></a>

### Look up cross-references by place ID
<a name="get-place-cross-references-lookup"></a>

------
#### [ Sample request ]

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?additional-features=CrossReferences&key=Your_Key
```

------
#### [ Sample response ]

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "Space Needle, Seattle, WA, United States",
    "CrossReferences": [
        {
            "Source": "TripAdvisor",
            "SourcePlaceId": "d104410",
            "SourceCategories": [
                {
                    "Id": "400-4000-4580",
                    "Name": "Landmark-Attraction"
                }
            ]
        },
        {
            "Source": "Yelp",
            "SourcePlaceId": "space-needle-seattle",
            "SourceCategories": [
                {
                    "Id": "400-4000-4580",
                    "Name": "Landmark-Attraction"
                }
            ]
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?key=Your_Key&additional-features=CrossReferences'
```

------
#### [ AWS CLI ]

```
aws geo-places get-place --key ${YourKey} --place-id "YourPlaceId" --additional-features CrossReferences
```

------

## Developer tips
<a name="get-place-cross-references-dev-tips"></a>
+ To use the returned identifiers, refer to the supplier's API documentation. For example, see the [Yelp Places API](https://docs.developer.yelp.com/docs/places-intro) on the Yelp website or the [Tripadvisor Content API](https://docs.terra.tripadvisor.com/docs/overview) on the Tripadvisor website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
