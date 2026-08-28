---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html
---

# SearchNearby
<a name="API_geoplaces_SearchNearby"></a>

 `SearchNearby` queries for points of interest within a radius from a central coordinates, returning place results with optional filters such as categories, business chains, food types and more. The API returns details such as a place name, address, phone, category, food type, contact, opening hours. Also, the API can return phonemes, time zones and more based on requested parameters.

For more information, see [Search Nearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoplaces_SearchNearby_RequestSyntax"></a>

```
POST /v2/search-nearby?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "AdditionalFeatures": [ "{{string}}" ],
   "Filter": {
      "BoundingBox": [ {{number}} ],
      "ExcludeBusinessChains": [ "{{string}}" ],
      "ExcludeCategories": [ "{{string}}" ],
      "ExcludeFoodTypes": [ "{{string}}" ],
      "IncludeBusinessChains": [ "{{string}}" ],
      "IncludeCategories": [ "{{string}}" ],
      "IncludeCountries": [ "{{string}}" ],
      "IncludeFoodTypes": [ "{{string}}" ]
   },
   "IntendedUse": "{{string}}",
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PoliticalView": "{{string}}",
   "QueryPosition": [ {{number}} ],
   "QueryRadius": {{number}}
}
```

## URI Request Parameters
<a name="API_geoplaces_SearchNearby_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_geoplaces_SearchNearby_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalFeatures](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-AdditionalFeatures"></a>
A list of optional additional parameters, such as time zone, that can be requested for each result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the `TimeZone` value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `TimeZone | Phonemes | Access | Contact | CrossReferences`
Required: No

 ** [Filter](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-Filter"></a>
A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
Type: [SearchNearbyFilter](API_geoplaces_SearchNearbyFilter.md) object
Required: No

 ** [IntendedUse](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored).
When storing `SearchNearby` responses, you *must* set this field to `Storage` to comply with the terms of service. These requests will be charged at a higher rate. Please review the [user agreement](https://aws.amazon.com/location/sla/) and [service pricing structure](https://aws.amazon.com/location/pricing/) to determine the correct setting for your use case.
Type: String
Valid Values: `SingleUse | Storage`
Required: No

 ** [Language](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-Language"></a>
A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the following codes: `en, id, km, lo, ms, my, pt, th, tl, vi, zh`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-MaxResults"></a>
An optional limit for the number of results returned in a single call.
Default value: 20
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [PoliticalView](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-PoliticalView"></a>
The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** [QueryPosition](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-QueryPosition"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude] for which you are querying nearby results for. Results closer to the position will be ranked higher then results further away from the position
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [QueryRadius](#API_geoplaces_SearchNearby_RequestSyntax) **   <a name="location-geoplaces_SearchNearby-request-QueryRadius"></a>
The maximum distance in meters from the QueryPosition from which a result will be returned. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only up to a maximum value of 100,000.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 21000000.
Required: No

## Response Syntax
<a name="API_geoplaces_SearchNearby_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "NextToken": "string",
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
         "AccessRestrictions": [
            {
               "Categories": [
                  {
                     "Id": "string",
                     "LocalizedName": "string",
                     "Name": "string",
                     "Primary": boolean
                  }
               ],
               "Restricted": boolean
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
         "BusinessChains": [
            {
               "Id": "string",
               "Name": "string"
            }
         ],
         "Categories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "Contacts": {
            "Emails": [
               {
                  "Categories": [
                     {
                        "Id": "string",
                        "LocalizedName": "string",
                        "Name": "string",
                        "Primary": boolean
                     }
                  ],
                  "Label": "string",
                  "Value": "string"
               }
            ],
            "Faxes": [
               {
                  "Categories": [
                     {
                        "Id": "string",
                        "LocalizedName": "string",
                        "Name": "string",
                        "Primary": boolean
                     }
                  ],
                  "Label": "string",
                  "Value": "string"
               }
            ],
            "Phones": [
               {
                  "Categories": [
                     {
                        "Id": "string",
                        "LocalizedName": "string",
                        "Name": "string",
                        "Primary": boolean
                     }
                  ],
                  "Label": "string",
                  "Value": "string"
               }
            ],
            "Websites": [
               {
                  "Categories": [
                     {
                        "Id": "string",
                        "LocalizedName": "string",
                        "Name": "string",
                        "Primary": boolean
                     }
                  ],
                  "Label": "string",
                  "Value": "string"
               }
            ]
         },
         "CrossReferences": [
            {
               "Source": "string",
               "SourceCategories": [
                  {
                     "Id": "string",
                     "LocalizedName": "string",
                     "Name": "string",
                     "Primary": boolean
                  }
               ],
               "SourcePlaceId": "string"
            }
         ],
         "Distance": number,
         "FoodTypes": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Primary": boolean
            }
         ],
         "MapView": [ number ],
         "OpeningHours": [
            {
               "Categories": [
                  {
                     "Id": "string",
                     "LocalizedName": "string",
                     "Name": "string",
                     "Primary": boolean
                  }
               ],
               "Components": [
                  {
                     "OpenDuration": "string",
                     "OpenTime": "string",
                     "Recurrence": "string"
                  }
               ],
               "Display": [ "string" ],
               "OpenNow": boolean
            }
         ],
         "Phonemes": {
            "Address": {
               "Block": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "Country": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "District": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "Locality": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "Region": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "Street": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "SubBlock": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "SubDistrict": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ],
               "SubRegion": [
                  {
                     "Language": "string",
                     "Preferred": boolean,
                     "Value": "string"
                  }
               ]
            },
            "Title": [
               {
                  "Language": "string",
                  "Preferred": boolean,
                  "Value": "string"
               }
            ]
         },
         "PlaceAttributes": [ "string" ],
         "PlaceId": "string",
         "PlaceType": "string",
         "PoliticalView": "string",
         "Position": [ number ],
         "TimeZone": {
            "Name": "string",
            "Offset": "string",
            "OffsetSeconds": number
         },
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geoplaces_SearchNearby_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_SearchNearby_ResponseSyntax) **   <a name="location-geoplaces_SearchNearby-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [NextToken](#API_geoplaces_SearchNearby_ResponseSyntax) **   <a name="location-geoplaces_SearchNearby-response-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [ResultItems](#API_geoplaces_SearchNearby_ResponseSyntax) **   <a name="location-geoplaces_SearchNearby-response-ResultItems"></a>
List of places or results returned for a query.
Type: Array of [SearchNearbyResultItem](API_geoplaces_SearchNearbyResultItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_geoplaces_SearchNearby_Errors"></a>

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
<a name="API_geoplaces_SearchNearby_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/SearchNearby)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SearchNearby)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
