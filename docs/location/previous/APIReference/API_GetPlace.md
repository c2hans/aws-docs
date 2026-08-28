---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html
---

# GetPlace
<a name="API_GetPlace"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the [V2 `GetPlace`](/location/latest/APIReference/API_geoplaces_GetPlace.html) operation unless you require Grab data.
This version of `GetPlace` is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
Version 2 of the `GetPlace` operation interoperates with the rest of the Places V2 API, while this version does not.
If you are using an AWS SDK or the AWS CLI, note that the Places API version 2 is found under `geo-places` or `geo_places`, not under `location`.
Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Places V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html) or the [Developer Guide](/location/latest/developerguide/places.html).

Finds a place by its unique ID. A `PlaceId` is returned by other search operations.

**Note**
A PlaceId is valid only if all of the following are the same in the original search request and the call to `GetPlace`.
Customer AWS account
 AWS Region
Data provider specified in the place index resource

**Note**
If your Place index resource is configured with Grab as your geolocation provider and Storage as Intended use, the GetPlace operation is unavailable. For more information, see [AWS service terms](http://aws.amazon.com/service-terms).

## Request Syntax
<a name="API_GetPlace_RequestSyntax"></a>

```
GET /places/v0/indexes/{{IndexName}}/places/{{PlaceId}}?key={{Key}}&language={{Language}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPlace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IndexName](#API_GetPlace_RequestSyntax) **   <a name="location-GetPlace-request-uri-IndexName"></a>
The name of the place index resource that you want to use for the search.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Key](#API_GetPlace_RequestSyntax) **   <a name="location-GetPlace-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [Language](#API_GetPlace_RequestSyntax) **   <a name="location-GetPlace-request-uri-Language"></a>
The preferred language used to return results. The value must be a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.
This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.
For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the `language` parameter set to `en`. The `city` in the results will most likely be returned as `Athens`.
If you set the `language` parameter to `el`, for Greek, then the `city` in the results will more likely be returned as `Αθήνα`.
If the data provider does not have a value for Greek, the result will be in a language that the provider does support.
Length Constraints: Minimum length of 2. Maximum length of 35.

 ** [PlaceId](#API_GetPlace_RequestSyntax) **   <a name="location-GetPlace-request-uri-PlaceId"></a>
The identifier of the place to find.
Required: Yes

## Request Body
<a name="API_GetPlace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPlace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
   }
}
```

## Response Elements
<a name="API_GetPlace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Place](#API_GetPlace_ResponseSyntax) **   <a name="location-GetPlace-response-Place"></a>
Details about the result, such as its address and position.
Type: [Place](API_Place.md) object

## Errors
<a name="API_GetPlace_Errors"></a>

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
<a name="API_GetPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetPlace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetPlace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetPlace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetPlace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetPlace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetPlace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetPlace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetPlace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
