---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-translations.html
---

# How to get address translations
<a name="how-to-geocode-translations"></a>

`AddressTranslations` allows you to retrieve all name translations and alternative names for address components in all available languages. You specify which address components to translate using the `AddressTranslations` request parameter.

## Potential use cases
<a name="geocode-translations-use"></a>
+ **Multilingual applications:** Display address components in multiple languages for international users.
+ **Localization:** Show both local-language and user-preferred-language names for cities and regions.

## Examples
<a name="geocode-translations-example"></a>

### Get translations for locality and region
<a name="geocode-translations-city-region"></a>

------
#### [ Sample request ]

```
{
    "QueryText": "1 Rue de Rivoli, Paris",
    "AddressTranslations": ["Locality", "Region"]
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
            "Title": "1 Rue de Rivoli, 75004 Paris, France",
            "Translations": {
                "Locality": [
                    {
                        "Names": [
                            {
                                "Value": "Paris",
                                "Language": "fr",
                                "Type": "BaseName",
                                "Primary": true
                            },
                            {
                                "Value": "Parigi",
                                "Language": "it",
                                "Type": "Exonym"
                            },
                            {
                                "Value": "パリ",
                                "Language": "ja",
                                "Type": "Exonym"
                            }
                        ],
                        "Preference": "Primary"
                    }
                ],
                "Region": [
                    {
                        "Names": [
                            {
                                "Value": "Île-de-France",
                                "Language": "fr",
                                "Type": "BaseName",
                                "Primary": true
                            },
                            {
                                "Value": "IDF",
                                "Language": "fr",
                                "Type": "Abbreviation"
                            }
                        ],
                        "Preference": "Primary"
                    }
                ]
            }
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
    "QueryText": "1 Rue de Rivoli, Paris",
    "AddressTranslations": ["Locality", "Region"]
}'
```

------
#### [ AWS CLI ]

```
aws geo-places geocode --key ${YourKey} --query-text "1 Rue de Rivoli, Paris" --address-translations Locality Region
```

------

## Developer tips
<a name="geocode-translations-dev-tips"></a>
+ Valid values for `AddressTranslations` are `District`, `Locality`, `Region`, and `SubRegion`.
+ Each translation includes a `Type` field indicating the kind of name variant: `BaseName` (official name), `Abbreviation`, `Exonym` (translation to another language), `Shortened`, or `Synonym`.
+ The `Primary` field indicates the primary name variant for a given language.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
