---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html
---

# DescribeMap
<a name="API_DescribeMap"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require `Grab` data.
 `DescribeMap` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Retrieves the map resource details.

## Request Syntax
<a name="API_DescribeMap_RequestSyntax"></a>

```
GET /maps/v0/maps/{{MapName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeMap_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MapName](#API_DescribeMap_RequestSyntax) **   <a name="location-DescribeMap-request-uri-MapName"></a>
The name of the map resource.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_DescribeMap_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeMap_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Configuration": {
      "CustomLayers": [ "string" ],
      "PoliticalView": "string",
      "Style": "string"
   },
   "CreateTime": "string",
   "DataSource": "string",
   "Description": "string",
   "MapArn": "string",
   "MapName": "string",
   "PricingPlan": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_DescribeMap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-Configuration"></a>
Specifies the map tile style selected from a partner data provider.
Type: [MapConfiguration](API_MapConfiguration.md) object

 ** [CreateTime](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-CreateTime"></a>
The timestamp for when the map resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [DataSource](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-DataSource"></a>
Specifies the data provider for the associated map tiles.
Type: String

 ** [Description](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-Description"></a>
The optional description for the map resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [MapArn](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-MapArn"></a>
The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:map/ExampleMap`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [MapName](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-MapName"></a>
The map style selected from an available provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [PricingPlan](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`

 ** [Tags](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-Tags"></a>
Tags associated with the map resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdateTime](#API_DescribeMap_ResponseSyntax) **   <a name="location-DescribeMap-response-UpdateTime"></a>
The timestamp for when the map resource was last update in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_DescribeMap_Errors"></a>

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
<a name="API_DescribeMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/DescribeMap)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/DescribeMap)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DescribeMap)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/DescribeMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DescribeMap)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/DescribeMap)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/DescribeMap)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/DescribeMap)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/DescribeMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DescribeMap)
