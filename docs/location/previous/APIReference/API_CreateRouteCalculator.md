---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreateRouteCalculator.html
---

# CreateRouteCalculator
<a name="API_CreateRouteCalculator"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.
 `CreateRouteCalculator` is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.
If you are using an AWS SDK or the AWS CLI, note that the Routes API version 2 is found under `geo-routes` or `geo_routes`, not under `location`.
Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Routes V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html) or the [Developer Guide](/location/latest/developerguide/routes.html).

Creates a route calculator resource in your AWS account.

You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](http://aws.amazon.com/service-terms) for more details.

## Request Syntax
<a name="API_CreateRouteCalculator_RequestSyntax"></a>

```
POST /routes/v0/calculators HTTP/1.1
Content-type: application/json

{
   "CalculatorName": "{{string}}",
   "DataSource": "{{string}}",
   "Description": "{{string}}",
   "PricingPlan": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRouteCalculator_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRouteCalculator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CalculatorName](#API_CreateRouteCalculator_RequestSyntax) **   <a name="location-CreateRouteCalculator-request-CalculatorName"></a>
The name of the route calculator resource.
Requirements:
+ Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (\_).
+ Must be a unique Route calculator resource name.
+ No spaces allowed. For example, `ExampleRouteCalculator`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [DataSource](#API_CreateRouteCalculator_RequestSyntax) **   <a name="location-CreateRouteCalculator-request-DataSource"></a>
Specifies the data provider of traffic and road network data.
This field is case-sensitive. Enter the valid values as shown. For example, entering `HERE` returns an error.
Valid values include:
+  `Esri` – For additional information about [Esri](https://docs.aws.amazon.com/location/previous/developerguide/esri.html)'s coverage in your region of interest, see [Esri details on street networks and traffic coverage](https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm).

  Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.
+  `Grab` – Grab provides routing functionality for Southeast Asia. For additional information about [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html)' coverage, see [GrabMaps countries and areas covered](https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area).
+  `Here` – For additional information about [HERE Technologies](https://docs.aws.amazon.com/location/previous/developerguide/HERE.html)' coverage in your region of interest, see [HERE car routing coverage](https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html) and [HERE truck routing coverage](https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html).
For additional information , see [Data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html) on the *Amazon Location Service Developer Guide*.
Type: String
Required: Yes

 ** [Description](#API_CreateRouteCalculator_RequestSyntax) **   <a name="location-CreateRouteCalculator-request-Description"></a>
The optional description for the route calculator resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [PricingPlan](#API_CreateRouteCalculator_RequestSyntax) **   <a name="location-CreateRouteCalculator-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [Tags](#API_CreateRouteCalculator_RequestSyntax) **   <a name="location-CreateRouteCalculator-request-Tags"></a>
Applies one or more tags to the route calculator resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
+ For example: { `"tag1" : "value1"`, `"tag2" : "value2"`}
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource
+ Each resource tag must be unique with a maximum of one value.
+ Maximum key length: 128 Unicode characters in UTF-8
+ Maximum value length: 256 Unicode characters in UTF-8
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @.
+ Cannot use "aws:" as a prefix for a key.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateRouteCalculator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CalculatorArn": "string",
   "CalculatorName": "string",
   "CreateTime": "string"
}
```

## Response Elements
<a name="API_CreateRouteCalculator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculatorArn](#API_CreateRouteCalculator_ResponseSyntax) **   <a name="location-CreateRouteCalculator-response-CalculatorArn"></a>
The Amazon Resource Name (ARN) for the route calculator resource. Use the ARN when you specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:route-calculator/ExampleCalculator`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [CalculatorName](#API_CreateRouteCalculator_ResponseSyntax) **   <a name="location-CreateRouteCalculator-response-CalculatorName"></a>
The name of the route calculator resource.
+ For example, `ExampleRouteCalculator`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [CreateTime](#API_CreateRouteCalculator_ResponseSyntax) **   <a name="location-CreateRouteCalculator-response-CreateTime"></a>
The timestamp when the route calculator resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
+ For example, `2020–07-2T12:15:20.000Z+01:00`
Type: Timestamp

## Errors
<a name="API_CreateRouteCalculator_Errors"></a>

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
<a name="API_CreateRouteCalculator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreateRouteCalculator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreateRouteCalculator)
