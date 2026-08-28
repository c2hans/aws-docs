---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html
---

# Autocomplete
<a name="API_geoplaces_Autocomplete"></a>

 `Autocomplete` completes potential places and addresses as the user types, based on the partial input. The API enhances the efficiency and accuracy of address by completing query based on a few entered keystrokes. It helps you by completing partial queries with valid address completion. Also, the API supports the filtering of results based on geographic location, country, or specific place types, and can be tailored using optional parameters like language and political views. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this operation.

For more information, see [Autocomplete](https://docs.aws.amazon.com/location/latest/developerguide/autocomplete.html) in the *Amazon Location Service Developer Guide*.

Try the Autocomplete API in the [API Playground](https://console.aws.amazon.com/location/api-playground/home#/autocomplete).

## Request Syntax
<a name="API_geoplaces_Autocomplete_RequestSyntax"></a>

```
POST /v2/autocomplete?key={{Key}} HTTP/1.1
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
      "IncludeCountries": [ "{{string}}" ],
      "IncludePlaceTypes": [ "{{string}}" ]
   },
   "IntendedUse": "{{string}}",
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "PoliticalView": "{{string}}",
   "PostalCodeMode": "{{string}}",
   "QueryText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geoplaces_Autocomplete_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_geoplaces_Autocomplete_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalFeatures](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-AdditionalFeatures"></a>
A list of optional additional parameters that can be requested for each result.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `Core`
Required: No

 ** [BiasPosition](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-BiasPosition"></a>
The position in longitude and latitude that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in `[lng, lat]` and in the WGS 84 format.
The fields `BiasPosition`, `FilterBoundingBox`, and `FilterCircle` are mutually exclusive.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [Filter](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-Filter"></a>
A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
Type: [AutocompleteFilter](API_geoplaces_AutocompleteFilter.md) object
Required: No

 ** [IntendedUse](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored). Currently, `Autocomplete` does not support storage of results.
Type: String
Valid Values: `SingleUse`
Required: No

 ** [Language](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-Language"></a>
A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-MaxResults"></a>
An optional limit for the number of results returned in a single call.
Default value: 5
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [PoliticalView](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-PoliticalView"></a>
The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.
The following political views are currently supported:
+  `ARG`: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands
+  `EGY`: Egypt's view on Bir Tawil
+  `IND`: India's view on Gilgit-Baltistan
+  `KEN`: Kenya's view on the Ilemi Triangle
+  `MAR`: Morocco's view on Western Sahara
+  `RUS`: Russia's view on Crimea
+  `SDN`: Sudan's view on the Halaib Triangle
+  `SRB`: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands
+  `SUR`: Suriname's view on the Courantyne Headwaters and Lawa Headwaters
+  `SYR`: Syria's view on the Golan Heights
+  `TUR`: Turkey's view on Cyprus and Northern Cyprus
+  `TZA`: Tanzania's view on Lake Malawi
+  `URY`: Uruguay's view on Rincon de Artigas
+  `VNM`: Vietnam's view on the Paracel Islands and Spratly Islands
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** [PostalCodeMode](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-PostalCodeMode"></a>
The `PostalCodeMode` affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If it's populated with the value `EnumerateSpannedLocalities`, all cities in that postal code are returned. If it's populated with the value `EnumerateSpannedDistricts`, all combinations of the postal code with the corresponding district and city names are returned.
Type: String
Valid Values: `MergeAllSpannedLocalities | EnumerateSpannedLocalities | EnumerateSpannedDistricts`
Required: No

 ** [QueryText](#API_geoplaces_Autocomplete_RequestSyntax) **   <a name="location-geoplaces_Autocomplete-request-QueryText"></a>
The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.
The fields `QueryText`, and `QueryID` are mutually exclusive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Response Syntax
<a name="API_geoplaces_Autocomplete_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "ResultItems": [
      {
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
         "EstimatedPointAddress": boolean,
         "Highlights": {
            "Address": {
               "AddressNumber": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Block": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Building": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Country": {
                  "Code": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ],
                  "Name": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ]
               },
               "District": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Intersection": [
                  [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ]
               ],
               "Label": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Locality": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "PostalCode": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "Region": {
                  "Code": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ],
                  "Name": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ]
               },
               "Street": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubBlock": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubDistrict": [
                  {
                     "EndIndex": number,
                     "StartIndex": number,
                     "Value": "string"
                  }
               ],
               "SubRegion": {
                  "Code": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ],
                  "Name": [
                     {
                        "EndIndex": number,
                        "StartIndex": number,
                        "Value": "string"
                     }
                  ]
               }
            },
            "Title": [
               {
                  "EndIndex": number,
                  "StartIndex": number,
                  "Value": "string"
               }
            ]
         },
         "Language": "string",
         "PlaceId": "string",
         "PlaceType": "string",
         "PoliticalView": "string",
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geoplaces_Autocomplete_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_Autocomplete_ResponseSyntax) **   <a name="location-geoplaces_Autocomplete-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [ResultItems](#API_geoplaces_Autocomplete_ResponseSyntax) **   <a name="location-geoplaces_Autocomplete-response-ResultItems"></a>
List of places or results returned for a query.
Type: Array of [AutocompleteResultItem](API_geoplaces_AutocompleteResultItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_geoplaces_Autocomplete_Errors"></a>

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
<a name="API_geoplaces_Autocomplete_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/Autocomplete)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Autocomplete)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
