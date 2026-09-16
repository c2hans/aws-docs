---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreatePlaceIndex.html
---

# CreatePlaceIndex
<a name="API_CreatePlaceIndex"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.
 `CreatePlaceIndex` is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.
If you are using an AWS SDK or the AWS CLI, note that the Places API version 2 is found under `geo-places` or `geo_places`, not under `location`.
Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Places V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html) or the [Developer Guide](/location/latest/developerguide/places.html).

Creates a place index resource in your AWS account. Use a place index resource to geocode addresses and other text queries by using the `SearchPlaceIndexForText` operation, and reverse geocode coordinates by using the `SearchPlaceIndexForPosition` operation, and enable autosuggestions by using the `SearchPlaceIndexForSuggestions` operation.

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](http://aws.amazon.com/service-terms) for more details.

## Request Syntax
<a name="API_CreatePlaceIndex_RequestSyntax"></a>

```
POST /places/v0/indexes HTTP/1.1
Content-type: application/json

{
   "DataSource": "{{string}}",
   "DataSourceConfiguration": {
      "IntendedUse": "{{string}}"
   },
   "Description": "{{string}}",
   "IndexName": "{{string}}",
   "PricingPlan": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePlaceIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePlaceIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSource](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-DataSource"></a>
Specifies the geospatial data provider for the new place index.
This field is case-sensitive. Enter the valid values as shown. For example, entering `HERE` returns an error.
Valid values include:
+  `Esri` – For additional information about [Esri](https://docs.aws.amazon.com/location/previous/developerguide/esri.html)'s coverage in your region of interest, see [Esri details on geocoding coverage](https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm).
+  `Grab` – Grab provides place index functionality for Southeast Asia. For additional information about [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html)' coverage, see [GrabMaps countries and areas covered](https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area).
+  `Here` – For additional information about [HERE Technologies](https://docs.aws.amazon.com/location/previous/developerguide/HERE.html)' coverage in your region of interest, see [HERE details on goecoding coverage](https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html).
**Important**
If you specify HERE Technologies (`Here`) as the data provider, you may not [store results](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html) for locations in Japan. For more information, see the [AWS service terms](http://aws.amazon.com/service-terms/) for Amazon Location Service.
For additional information , see [Data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html) on the *Amazon Location Service developer guide*.
Type: String
Required: Yes

 ** [DataSourceConfiguration](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-DataSourceConfiguration"></a>
Specifies the data storage option requesting Places.
Type: [DataSourceConfiguration](API_DataSourceConfiguration.md) object
Required: No

 ** [Description](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-Description"></a>
The optional description for the place index resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [IndexName](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-IndexName"></a>
The name of the place index resource.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique place index resource name.
+ No spaces allowed. For example, `ExamplePlaceIndex`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [PricingPlan](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [Tags](#API_CreatePlaceIndex_RequestSyntax) **   <a name="location-CreatePlaceIndex-request-Tags"></a>
Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource.
+ Each tag key must be unique and must have exactly one associated value.
+ Maximum key length: 128 Unicode characters in UTF-8.
+ Maximum value length: 256 Unicode characters in UTF-8.
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @
+ Cannot use "aws:" as a prefix for a key.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreatePlaceIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "IndexArn": "string",
   "IndexName": "string"
}
```

## Response Elements
<a name="API_CreatePlaceIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_CreatePlaceIndex_ResponseSyntax) **   <a name="location-CreatePlaceIndex-response-CreateTime"></a>
The timestamp for when the place index resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [IndexArn](#API_CreatePlaceIndex_ResponseSyntax) **   <a name="location-CreatePlaceIndex-response-IndexArn"></a>
The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across AWS.
+ Format example: `arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [IndexName](#API_CreatePlaceIndex_ResponseSyntax) **   <a name="location-CreatePlaceIndex-response-IndexName"></a>
The name for the place index resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

## Errors
<a name="API_CreatePlaceIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** ConflictException **
The request was unsuccessful because of a conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The operation was denied because the request would exceed the maximum [quota](https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html) set for Amazon Location Service.
 ** Message **
A message with the reason for the service quota exceeded exception error.
HTTP Status Code: 402

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
<a name="API_CreatePlaceIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreatePlaceIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreatePlaceIndex)
