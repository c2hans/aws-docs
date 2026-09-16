---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html
---

# Suggest
<a name="API_geoplaces_Suggest"></a>

 `Suggest` provides intelligent predictions or recommendations based on the user's input or context, such as relevant places, points of interest, query terms or search category. It is designed to help users find places or point of interests candidates or identify a follow on query based on incomplete or misspelled queries. It returns a list of possible matches or refinements that can be used to formulate a more accurate query. Users can select the most appropriate suggestion and use it for further searching. The API provides options for filtering results by location and other attributes, and allows for additional features like phonemes and timezones. The response includes refined query terms and detailed place information.

For more information, see [Suggest](https://docs.aws.amazon.com/location/latest/developerguide/suggest.html) in the *Amazon Location Service Developer Guide*.

Try the Suggest API in the [API Playground](https://console.aws.amazon.com/location/api-playground/home#/suggest).

## Request Syntax
<a name="API_geoplaces_Suggest_RequestSyntax"></a>

```
POST /v2/suggest?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "AdditionalFeatures": [ "{{string}}" ],
   "BiasPosition": [ {{number}} ],
   "Filter": {
      "BoundingBox": [ {{number}} ],
      "Circle": {
         "Center": [ {{number}} ],
         "Radius": {{number}}
      },
      "IncludeCountries": [ "{{string}}" ]
   },
   "IntendedUse": "{{string}}",
   "Language": "{{string}}",
   "MaxQueryRefinements": {{number}},
   "MaxResults": {{number}},
   "PoliticalView": "{{string}}",
   "QueryText": "{{string}}",
   "TravelMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geoplaces_Suggest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_geoplaces_Suggest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalFeatures](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-AdditionalFeatures"></a>
 A list of optional additional parameters, such as time zone, that can be requested for each result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the `Core` and `TimeZone` values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `Core | TimeZone | Phonemes | Access | CrossReferences`
Required: No

 ** [BiasPosition](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-BiasPosition"></a>
The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in `[lng, lat]` and in the WGS 84 format.
The fields `BiasPosition`, `FilterBoundingBox`, and `FilterCircle` are mutually exclusive.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [Filter](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-Filter"></a>
A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
Type: [SuggestFilter](API_geoplaces_SuggestFilter.md) object
Required: No

 ** [IntendedUse](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored). Currently, `Suggest` does not support storage of results.
Type: String
Valid Values: `SingleUse`
Required: No

 ** [Language](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-Language"></a>
 A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the following codes: `en, id, km, lo, ms, my, pt, th, tl, vi, zh`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxQueryRefinements](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-MaxQueryRefinements"></a>
 Maximum number of query terms to be returned for use with a search text query. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [MaxResults](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-MaxResults"></a>
 An optional limit for the number of results returned in a single call.
Default value: 20
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [PoliticalView](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** [QueryText](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-QueryText"></a>
The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.
The fields `QueryText` and `QueryID` are mutually exclusive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [TravelMode](#API_geoplaces_Suggest_RequestSyntax) **   <a name="location-geoplaces_Suggest-request-TravelMode"></a>
Indicates the mode of mobility used by the end user. This is used to improve the relevance of search results. Valid values are `Car`, `Scooter`, and `Truck`.
Type: String
Valid Values: `Car | Scooter | Truck`
Required: No

## Response Syntax
<a name="API_geoplaces_Suggest_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "QueryRefinements": [
      {
         "EndIndex": number,
         "OriginalTerm": "string",
         "RefinedTerm": "string",
         "StartIndex": number
      }
   ],
   "ResultItems": [
      {
         "Highlights": {
            "Address": {
               "Label": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ]
            },
            "Title": [
               {
                  "EndIndex": number,
                  "StartIndex": number,
                  "Value": "string"
               }
            ]
         },
         "Place": {
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
            }
         },
         "Query": {
            "QueryId": "string",
            "QueryType": "string"
         },
         "SuggestResultItemType": "string",
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geoplaces_Suggest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_Suggest_ResponseSyntax) **   <a name="location-geoplaces_Suggest-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [QueryRefinements](#API_geoplaces_Suggest_ResponseSyntax) **   <a name="location-geoplaces_Suggest-response-QueryRefinements"></a>
 Maximum number of query terms to be returned for use with a search text query. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [QueryRefinement](API_geoplaces_QueryRefinement.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [ResultItems](#API_geoplaces_Suggest_ResponseSyntax) **   <a name="location-geoplaces_Suggest-response-ResultItems"></a>
List of places or results returned for a query.
Type: Array of [SuggestResultItem](API_geoplaces_SuggestResultItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_geoplaces_Suggest_Errors"></a>

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
<a name="API_geoplaces_Suggest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/Suggest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/Suggest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Suggest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/Suggest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Suggest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/Suggest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/Suggest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/Suggest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/Suggest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Suggest)
