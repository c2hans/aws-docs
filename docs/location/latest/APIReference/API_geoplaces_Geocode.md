---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html
---

# Geocode
<a name="API_geoplaces_Geocode"></a>

 `Geocode` converts a textual address or place into geographic coordinates. You can obtain geographic coordinates, address component, and other related information. It supports flexible queries, including free-form text or structured queries with components like street names, postal codes, and regions. The Geocode API can also provide additional features such as time zone information and the inclusion of political views. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this operation.

For more information, see [Geocode](https://docs.aws.amazon.com/location/latest/developerguide/geocode.html) in the *Amazon Location Service Developer Guide*.

Try the Geocode API in the [API Playground](https://console.aws.amazon.com/location/api-playground/home#/geocode).

## Request Syntax
<a name="API_geoplaces_Geocode_RequestSyntax"></a>

```
POST /v2/geocode?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "AdditionalFeatures": [ "{{string}}" ],
   "AddressNamesMode": "{{string}}",
   "AddressTranslations": [ "{{string}}" ],
   "BiasPosition": [ {{number}} ],
   "Filter": {
      "IncludeCountries": [ "{{string}}" ],
      "IncludePlaceTypes": [ "{{string}}" ]
   },
   "IntendedUse": "{{string}}",
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "PoliticalView": "{{string}}",
   "PostalCodeMode": "{{string}}",
   "QueryComponents": {
      "AddressNumber": "{{string}}",
      "Country": "{{string}}",
      "District": "{{string}}",
      "Locality": "{{string}}",
      "PostalCode": "{{string}}",
      "Region": "{{string}}",
      "Street": "{{string}}",
      "SubRegion": "{{string}}"
   },
   "QueryText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geoplaces_Geocode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_geoplaces_Geocode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalFeatures](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-AdditionalFeatures"></a>
A list of optional additional parameters, such as time zone, that can be requested for each result.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `TimeZone | Access | SecondaryAddresses | Intersections`
Required: No

 ** [AddressNamesMode](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-AddressNamesMode"></a>
Specifies how address names are returned. If not set, the service returns normalized (official) names by default. When set to `Matched`, address names in the response are based on the input query rather than official names. When set to `Administrative`, the service returns the official administrative names for address components. `Administrative` currently applies only to addresses in the United States.
Type: String
Valid Values: `Matched | Administrative`
Required: No

 ** [AddressTranslations](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-AddressTranslations"></a>
Specifies which address components to include translations for. Translations include all name variants and alternative names for the requested fields in all available languages. Valid values are `District`, `Locality`, `Region`, and `SubRegion`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `District | Locality | Region | SubRegion`
Required: No

 ** [BiasPosition](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-BiasPosition"></a>
The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in `[lng, lat]` and in the WGS 84 format.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [Filter](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-Filter"></a>
A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
Type: [GeocodeFilter](API_geoplaces_GeocodeFilter.md) object
Required: No

 ** [IntendedUse](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored). If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
When storing `Geocode` responses, you *must* set this field to `Storage` to comply with the terms of service. These requests will be charged at a higher rate. Please review the [user agreement](https://aws.amazon.com/location/sla/) and [service pricing structure](https://aws.amazon.com/location/pricing/) to determine the correct setting for your use case.
Type: String
Valid Values: `SingleUse | Storage`
Required: No

 ** [Language](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-Language"></a>
A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-MaxResults"></a>
An optional limit for the number of results returned in a single call.
Default value: 20
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [PoliticalView](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-PoliticalView"></a>
The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** [PostalCodeMode](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-PostalCodeMode"></a>
The `PostalCodeMode` affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If it's populated with the value `EnumerateSpannedLocalities`, all cities in that postal code are returned. If it's populated with the value `EnumerateSpannedDistricts`, all combinations of the postal code with the corresponding district and city names are returned.
Type: String
Valid Values: `MergeAllSpannedLocalities | EnumerateSpannedLocalities | EnumerateSpannedDistricts`
Required: No

 ** [QueryComponents](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-QueryComponents"></a>
A structured free text query allows you to search for places by the name or text representation of specific properties of the place.
Type: [GeocodeQueryComponents](API_geoplaces_GeocodeQueryComponents.md) object
Required: No

 ** [QueryText](#API_geoplaces_Geocode_RequestSyntax) **   <a name="location-geoplaces_Geocode-request-QueryText"></a>
The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## Response Syntax
<a name="API_geoplaces_Geocode_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "ResultItems": [
      {
         "AccessPoints": [
            {
               "Label": "string",
               "Position": [ number ],
               "Primary": boolean,
               "Type": "string"
            }
         ],
         "Address": {
            "AddressNumber": "string",
            "Block": "string",
            "Building": "string",
            "Country": {
               "Code2": "string",
               "Code3": "string",
               "Name": "string"
            },
            "District": "string",
            "Intersection": [ "string" ],
            "Label": "string",
            "Locality": "string",
            "PostalCode": "string",
            "Region": {
               "Code": "string",
               "Name": "string"
            },
            "SecondaryAddressComponents": [
               {
                  "Designator": "string",
                  "Number": "string"
               }
            ],
            "Street": "string",
            "StreetComponents": [
               {
                  "BaseName": "string",
                  "Direction": "string",
                  "Language": "string",
                  "Prefix": "string",
                  "Suffix": "string",
                  "Type": "string",
                  "TypePlacement": "string",
                  "TypeSeparator": "string"
               }
            ],
            "SubBlock": "string",
            "SubDistrict": "string",
            "SubRegion": {
               "Code": "string",
               "Name": "string"
            }
         },
         "AddressNumberCorrected": boolean,
         "Categories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "Distance": number,
         "EstimatedPointAddress": boolean,
         "FoodTypes": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Primary": boolean
            }
         ],
         "Intersections": [
            {
               "AccessPoints": [
                  {
                     "Label": "string",
                     "Position": [ number ],
                     "Primary": boolean,
                     "Type": "string"
                  }
               ],
               "Address": {
                  "AddressNumber": "string",
                  "Block": "string",
                  "Building": "string",
                  "Country": {
                     "Code2": "string",
                     "Code3": "string",
                     "Name": "string"
                  },
                  "District": "string",
                  "Intersection": [ "string" ],
                  "Label": "string",
                  "Locality": "string",
                  "PostalCode": "string",
                  "Region": {
                     "Code": "string",
                     "Name": "string"
                  },
                  "SecondaryAddressComponents": [
                     {
                        "Designator": "string",
                        "Number": "string"
                     }
                  ],
                  "Street": "string",
                  "StreetComponents": [
                     {
                        "BaseName": "string",
                        "Direction": "string",
                        "Language": "string",
                        "Prefix": "string",
                        "Suffix": "string",
                        "Type": "string",
                        "TypePlacement": "string",
                        "TypeSeparator": "string"
                     }
                  ],
                  "SubBlock": "string",
                  "SubDistrict": "string",
                  "SubRegion": {
                     "Code": "string",
                     "Name": "string"
                  }
               },
               "Distance": number,
               "MapView": [ number ],
               "PlaceId": "string",
               "Position": [ number ],
               "RouteDistance": number,
               "Title": "string"
            }
         ],
         "MainAddress": {
            "AccessPoints": [
               {
                  "Label": "string",
                  "Position": [ number ],
                  "Primary": boolean,
                  "Type": "string"
               }
            ],
            "Address": {
               "AddressNumber": "string",
               "Block": "string",
               "Building": "string",
               "Country": {
                  "Code2": "string",
                  "Code3": "string",
                  "Name": "string"
               },
               "District": "string",
               "Intersection": [ "string" ],
               "Label": "string",
               "Locality": "string",
               "PostalCode": "string",
               "Region": {
                  "Code": "string",
                  "Name": "string"
               },
               "SecondaryAddressComponents": [
                  {
                     "Designator": "string",
                     "Number": "string"
                  }
               ],
               "Street": "string",
               "StreetComponents": [
                  {
                     "BaseName": "string",
                     "Direction": "string",
                     "Language": "string",
                     "Prefix": "string",
                     "Suffix": "string",
                     "Type": "string",
                     "TypePlacement": "string",
                     "TypeSeparator": "string"
                  }
               ],
               "SubBlock": "string",
               "SubDistrict": "string",
               "SubRegion": {
                  "Code": "string",
                  "Name": "string"
               }
            },
            "PlaceId": "string",
            "PlaceType": "string",
            "Position": [ number ],
            "Title": "string"
         },
         "MapView": [ number ],
         "MatchScores": {
            "Components": {
               "Address": {
                  "AddressNumber": number,
                  "Block": number,
                  "Building": number,
                  "Country": number,
                  "District": number,
                  "Intersection": [ number ],
                  "Locality": number,
                  "PostalCode": number,
                  "Region": number,
                  "SecondaryAddressComponents": [
                     {
                        "Number": number
                     }
                  ],
                  "SubBlock": number,
                  "SubDistrict": number,
                  "SubRegion": number
               },
               "Title": number
            },
            "Overall": number
         },
         "ParsedQuery": {
            "Address": {
               "AddressNumber": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Block": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Building": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Country": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "District": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Locality": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "OtherComponents": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "PostalCode": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Region": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SecondaryAddressComponents": [
                  {
                     "Designator": "string",
                     "EndIndex": number,
                     "Number": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Street": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubBlock": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubDistrict": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubRegion": [
                  {
                     "EndIndex": number,
                     "QueryComponent": "string",
                     "StartIndex": number,
                     "Value": "string"
                  }
               ]
            },
            "Title": [
               {
                  "EndIndex": number,
                  "QueryComponent": "string",
                  "StartIndex": number,
                  "Value": "string"
               }
            ]
         },
         "PlaceId": "string",
         "PlaceType": "string",
         "PoliticalView": "string",
         "Position": [ number ],
         "PostalCodeDetails": [
            {
               "PostalAuthority": "string",
               "PostalCode": "string",
               "PostalCodeType": "string",
               "UspsZip": {
                  "ZipClassificationCode": "string"
               },
               "UspsZipPlus4": {
                  "RecordTypeCode": "string"
               }
            }
         ],
         "SecondaryAddresses": [
            {
               "AccessPoints": [
                  {
                     "Label": "string",
                     "Position": [ number ],
                     "Primary": boolean,
                     "Type": "string"
                  }
               ],
               "Address": {
                  "AddressNumber": "string",
                  "Block": "string",
                  "Building": "string",
                  "Country": {
                     "Code2": "string",
                     "Code3": "string",
                     "Name": "string"
                  },
                  "District": "string",
                  "Intersection": [ "string" ],
                  "Label": "string",
                  "Locality": "string",
                  "PostalCode": "string",
                  "Region": {
                     "Code": "string",
                     "Name": "string"
                  },
                  "SecondaryAddressComponents": [
                     {
                        "Designator": "string",
                        "Number": "string"
                     }
                  ],
                  "Street": "string",
                  "StreetComponents": [
                     {
                        "BaseName": "string",
                        "Direction": "string",
                        "Language": "string",
                        "Prefix": "string",
                        "Suffix": "string",
                        "Type": "string",
                        "TypePlacement": "string",
                        "TypeSeparator": "string"
                     }
                  ],
                  "SubBlock": "string",
                  "SubDistrict": "string",
                  "SubRegion": {
                     "Code": "string",
                     "Name": "string"
                  }
               },
               "PlaceId": "string",
               "PlaceType": "string",
               "Position": [ number ],
               "Title": "string"
            }
         ],
         "TimeZone": {
            "Name": "string",
            "Offset": "string",
            "OffsetSeconds": number
         },
         "Title": "string",
         "Translations": {
            "District": [
               {
                  "Names": [
                     {
                        "Language": "string",
                        "Primary": boolean,
                        "Transliterated": boolean,
                        "Type": "string",
                        "Value": "string"
                     }
                  ],
                  "Preference": "string"
               }
            ],
            "Locality": [
               {
                  "Names": [
                     {
                        "Language": "string",
                        "Primary": boolean,
                        "Transliterated": boolean,
                        "Type": "string",
                        "Value": "string"
                     }
                  ],
                  "Preference": "string"
               }
            ],
            "Region": [
               {
                  "Names": [
                     {
                        "Language": "string",
                        "Primary": boolean,
                        "Transliterated": boolean,
                        "Type": "string",
                        "Value": "string"
                     }
                  ],
                  "Preference": "string"
               }
            ],
            "SubRegion": [
               {
                  "Names": [
                     {
                        "Language": "string",
                        "Primary": boolean,
                        "Transliterated": boolean,
                        "Type": "string",
                        "Value": "string"
                     }
                  ],
                  "Preference": "string"
               }
            ]
         }
      }
   ]
}
```

## Response Elements
<a name="API_geoplaces_Geocode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_Geocode_ResponseSyntax) **   <a name="location-geoplaces_Geocode-response-PricingBucket"></a>
The pricing bucket for which the query is charged at, or the maximum pricing bucket when the query is charged per item within the query.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [ResultItems](#API_geoplaces_Geocode_ResponseSyntax) **   <a name="location-geoplaces_Geocode-response-ResultItems"></a>
List of places or results returned for a query.
Type: Array of [GeocodeResultItem](API_geoplaces_GeocodeResultItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_geoplaces_Geocode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** FieldList **
Test stub for FieldList.
 ** Reason **
Test stub for reason
HTTP Status Code: 400

## See Also
<a name="API_geoplaces_Geocode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/Geocode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/Geocode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Geocode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/Geocode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Geocode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/Geocode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/Geocode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/Geocode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/Geocode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Geocode)
