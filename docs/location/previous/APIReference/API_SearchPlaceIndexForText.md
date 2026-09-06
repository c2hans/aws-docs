---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html
---

# SearchPlaceIndexForText
<a name="API_SearchPlaceIndexForText"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to [`Geocode`](/location/latest/APIReference/API_geoplaces_Geocode.html) or [`SearchText`](/location/latest/APIReference/API_geoplaces_SearchText.html) unless you require Grab data.
 `SearchPlaceIndexForText` is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `Geocode` operation gives better results in the address geocoding use case, while the version 2 `SearchText` operation gives better results when searching for businesses and points of interest.
If you are using an AWS SDK or the AWS CLI, note that the Places API version 2 is found under `geo-places` or `geo_places`, not under `location`.
Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.

Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest.

Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.

**Note**
You can search for places near a given position using `BiasPosition`, or filter results within a bounding box using `FilterBBox`. Providing both parameters simultaneously returns an error.

Search results are returned in order of highest to lowest relevance.

## Request Syntax
<a name="API_SearchPlaceIndexForText_RequestSyntax"></a>

```
POST /places/v0/indexes/{{IndexName}}/search/text?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "BiasPosition": [ {{number}} ],
   "FilterBBox": [ {{number}} ],
   "FilterCategories": [ "{{string}}" ],
   "FilterCountries": [ "{{string}}" ],
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "Text": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchPlaceIndexForText_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IndexName](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-uri-IndexName"></a>
The name of the place index resource you want to use for the search.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Key](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_SearchPlaceIndexForText_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BiasPosition](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-BiasPosition"></a>
An optional parameter that indicates a preference for places that are closer to a specified position.
 If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.
For example, `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847`.
 `BiasPosition` and `FilterBBox` are mutually exclusive. Specifying both options results in an error.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [FilterBBox](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-FilterBBox"></a>
An optional parameter that limits the search results by returning only places that are within the provided bounding box.
 If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.
For example, `[-12.7935, -37.4835, -12.0684, -36.9542]` represents a bounding box where the southwest corner has longitude `-12.7935` and latitude `-37.4835`, and the northeast corner has longitude `-12.0684` and latitude `-36.9542`.
 `FilterBBox` and `BiasPosition` are mutually exclusive. Specifying both options results in an error.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** [FilterCategories](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-FilterCategories"></a>
A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match *any* of the categories listed.
For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html), in the *Amazon Location Service developer guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 35.
Required: No

 ** [FilterCountries](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-FilterCountries"></a>
An optional parameter that limits the search results by returning only places that are in a specified list of countries.
+ Valid values include [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) 3-digit country codes. For example, Australia uses three upper-case characters: `AUS`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** [Language](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-Language"></a>
The preferred language used to return results. The value must be a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.
This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.
For an example, we'll use the Greek language. You search for `Athens, Greece`, with the `language` parameter set to `en`. The result found will most likely be returned as `Athens`.
If you set the `language` parameter to `el`, for Greek, then the result found will more likely be returned as `Αθήνα`.
If the data provider does not have a value for Greek, the result will be in a language that the provider does support.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-MaxResults"></a>
An optional parameter. The maximum number of results returned per request.
The default: `50`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Text](#API_SearchPlaceIndexForText_RequestSyntax) **   <a name="location-SearchPlaceIndexForText-request-Text"></a>
The address, name, city, or region to be used in the search in free-form text format. For example, `123 Any Street`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Response Syntax
<a name="API_SearchPlaceIndexForText_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Results": [
      {
         "Distance": number,
         "Place": {
            "AddressNumber": "string",
            "Categories": [ "string" ],
            "Country": "string",
            "Geometry": {
               "Point": [ number ]
            },
            "Interpolated": boolean,
            "Label": "string",
            "Municipality": "string",
            "Neighborhood": "string",
            "PostalCode": "string",
            "Region": "string",
            "Street": "string",
            "SubMunicipality": "string",
            "SubRegion": "string",
            "SupplementalCategories": [ "string" ],
            "TimeZone": {
               "Name": "string",
               "Offset": number
            },
            "UnitNumber": "string",
            "UnitType": "string"
         },
         "PlaceId": "string",
         "Relevance": number
      }
   ],
   "Summary": {
      "BiasPosition": [ number ],
      "DataSource": "string",
      "FilterBBox": [ number ],
      "FilterCategories": [ "string" ],
      "FilterCountries": [ "string" ],
      "Language": "string",
      "MaxResults": number,
      "ResultBBox": [ number ],
      "Text": "string"
   }
}
```

## Response Elements
<a name="API_SearchPlaceIndexForText_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_SearchPlaceIndexForText_ResponseSyntax) **   <a name="location-SearchPlaceIndexForText-response-Results"></a>
A list of Places matching the input text. Each result contains additional information about the specific point of interest.
Not all response properties are included with all responses. Some properties may only be returned by specific data partners.
Type: Array of [SearchForTextResult](API_SearchForTextResult.md) objects

 ** [Summary](#API_SearchPlaceIndexForText_ResponseSyntax) **   <a name="location-SearchPlaceIndexForText-response-Summary"></a>
Contains a summary of the request. Echoes the input values for `BiasPosition`, `FilterBBox`, `FilterCountries`, `Language`, `MaxResults`, and `Text`. Also includes the `DataSource` of the place index and the bounding box, `ResultBBox`, which surrounds the search results.
Type: [SearchPlaceIndexForTextSummary](API_SearchPlaceIndexForTextSummary.md) object

## Errors
<a name="API_SearchPlaceIndexForText_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_SearchPlaceIndexForText_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/SearchPlaceIndexForText)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchPlaceIndexForText)
