---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-address-names-mode.html
---

# How to control address name variants
<a name="how-to-geocode-address-names-mode"></a>

`AddressNamesMode` specifies how address names are returned. If not set, the service returns normalized (official) names by default. When set to `Matched`, address names in the response are based on the input query rather than official names. When set to `Administrative`, the service returns the official administrative names for address components. `Administrative` currently applies only to addresses in the United States.

## Potential use cases
<a name="geocode-address-names-mode-use"></a>
+ **Address form completion:** Use `Matched` to return names consistent with what the user typed, reducing confusion in autocomplete workflows.
+ **Address standardization:** Use `Administrative` to normalize city names to their official administrative form for data quality and deduplication.

## Examples
<a name="geocode-address-names-mode-example"></a>

### Use Matched mode
<a name="geocode-address-names-mode-matched"></a>

------
#### [ Sample request ]

```
{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Matched"
}
```

------
#### [ Sample response ]

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "100 Universal City Plz, Universal City, CA 91608, United States",
            "Address": {
                "Label": "100 Universal City Plz, Universal City, CA 91608, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "CA",
                    "Name": "California"
                },
                "Locality": "Universal City",
                "PostalCode": "91608",
                "Street": "Universal City Plz",
                "AddressNumber": "100"
            },
            "Position": [
                -118.36054,
                34.13857
            ]
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Matched"
}'
```

------
#### [ AWS CLI ]

```
aws geo-places geocode --key ${YourKey} --query-text "100 Universal City Plaza, Hollywood, CA" --address-names-mode Matched
```

------

### Use Administrative mode
<a name="geocode-address-names-mode-administrative"></a>

------
#### [ Sample request ]

```
{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Administrative"
}
```

------
#### [ Sample response ]

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "100 Universal Terrace Pkwy, Los Angeles, CA 91608, United States",
            "Address": {
                "Label": "100 Universal Terrace Pkwy, Los Angeles, CA 91608, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "CA",
                    "Name": "California"
                },
                "Locality": "Los Angeles",
                "PostalCode": "91608",
                "Street": "Universal Terrace Pkwy",
                "AddressNumber": "100"
            },
            "Position": [
                -118.36054,
                34.13857
            ]
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Administrative"
}'
```

------
#### [ AWS CLI ]

```
aws geo-places geocode --key ${YourKey} --query-text "100 Universal City Plaza, Hollywood, CA" --address-names-mode Administrative
```

------

## Developer tips
<a name="geocode-address-names-mode-dev-tips"></a>
+ If not set, the service returns normalized (official) names by default.
+ `Administrative` currently applies only to addresses in the United States.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
