---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPosition.html
---

# SearchPlaceIndexForPosition
<a name="API_SearchPlaceIndexForPosition"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to [`ReverseGeocode`](/location/latest/APIReference/API_geoplaces_ReverseGeocode.html) or [`SearchNearby`](/location/latest/APIReference/API_geoplaces_SearchNearby.html) unless you require Grab data.
 `SearchPlaceIndexForPosition` is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `ReverseGeocode` operation gives better results in the address reverse-geocoding use case, while the version 2 `SearchNearby` operation gives better results when searching for businesses and points of interest near a specific location.
If you are using an AWS SDK or the AWS CLI, note that the Places API version 2 is found under `geo-places` or `geo_places`, not under `location`.
Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.

Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.

## Request Syntax
<a name="API_SearchPlaceIndexForPosition_RequestSyntax"></a>

```
POST /places/v0/indexes/{{IndexName}}/search/position?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "Position": [ {{number}} ]
}
```

## URI Request Parameters
<a name="API_SearchPlaceIndexForPosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IndexName](#API_SearchPlaceIndexForPosition_RequestSyntax) **   <a name="location-SearchPlaceIndexForPosition-request-uri-IndexName"></a>
The name of the place index resource you want to use for the search.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Key](#API_SearchPlaceIndexForPosition_RequestSyntax) **   <a name="location-SearchPlaceIndexForPosition-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_SearchPlaceIndexForPosition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Language](#API_SearchPlaceIndexForPosition_RequestSyntax) **   <a name="location-SearchPlaceIndexForPosition-request-Language"></a>
The preferred language used to return results. The value must be a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.
This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.
For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the `language` parameter set to `en`. The `city` in the results will most likely be returned as `Athens`.
If you set the `language` parameter to `el`, for Greek, then the `city` in the results will more likely be returned as `Αθήνα`.
If the data provider does not have a value for Greek, the result will be in a language that the provider does support.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_SearchPlaceIndexForPosition_RequestSyntax) **   <a name="location-SearchPlaceIndexForPosition-request-MaxResults"></a>
An optional parameter. The maximum number of results returned per request.
Default value: `50`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Position](#API_SearchPlaceIndexForPosition_RequestSyntax) **   <a name="location-SearchPlaceIndexForPosition-request-Position"></a>
Specifies the longitude and latitude of the position to query.
 This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.
For example, `[-123.1174, 49.2847]` represents a position with longitude `-123.1174` and latitude `49.2847`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

## Response Syntax
<a name="API_SearchPlaceIndexForPosition_ResponseSyntax"></a>

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
         "PlaceId": "string"
      }
   ],
   "Summary": {
      "DataSource": "string",
      "Language": "string",
      "MaxResults": number,
      "Position": [ number ]
   }
}
```

## Response Elements
<a name="API_SearchPlaceIndexForPosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_SearchPlaceIndexForPosition_ResponseSyntax) **   <a name="location-SearchPlaceIndexForPosition-response-Results"></a>
Returns a list of Places closest to the specified position. Each result contains additional information about the Places returned.
Type: Array of [SearchForPositionResult](API_SearchForPositionResult.md) objects

 ** [Summary](#API_SearchPlaceIndexForPosition_ResponseSyntax) **   <a name="location-SearchPlaceIndexForPosition-response-Summary"></a>
Contains a summary of the request. Echoes the input values for `Position`, `Language`, `MaxResults`, and the `DataSource` of the place index.
Type: [SearchPlaceIndexForPositionSummary](API_SearchPlaceIndexForPositionSummary.md) object

## Errors
<a name="API_SearchPlaceIndexForPosition_Errors"></a>

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
<a name="API_SearchPlaceIndexForPosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/SearchPlaceIndexForPosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchPlaceIndexForPosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
