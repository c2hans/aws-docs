---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-place-address-names-mode.html
---

# How to get administrative address names
<a name="how-to-get-place-address-names-mode"></a>

Use the `address-names-mode` query parameter set to `Administrative` to return official administrative names for address components. `Administrative` currently applies only to addresses in the United States.

## Potential use cases
<a name="get-place-address-names-mode-use"></a>
+ **Address standardization:** Normalize city names to their official administrative form when displaying place details.

## Examples
<a name="get-place-address-names-mode-example"></a>

### Use Administrative mode
<a name="get-place-address-names-mode-admin"></a>

------
#### [ Sample request ]

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?address-names-mode=Administrative&key=Your_Key
```

------
#### [ Sample response ]

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "Empire State Building, New York, NY, United States",
    "Address": {
        "Label": "Empire State Building, 350 5th Ave, New York, NY 10118, United States",
        "Locality": "New York"
    }
}
```

------
#### [ cURL ]

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?address-names-mode=Administrative&key=Your_Key'
```

------
#### [ AWS CLI ]

```
aws geo-places get-place --key ${YourKey} --place-id "YourPlaceId" --address-names-mode Administrative
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
