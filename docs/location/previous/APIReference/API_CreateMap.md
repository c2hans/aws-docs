---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreateMap.html
---

# CreateMap
<a name="API_CreateMap"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require `Grab` data.
 `CreateMap` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Creates a map resource in your AWS account, which provides map tiles of different styles sourced from global location data providers.

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](http://aws.amazon.com/service-terms) for more details.

## Request Syntax
<a name="API_CreateMap_RequestSyntax"></a>

```
POST /maps/v0/maps HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "CustomLayers": [ "{{string}}" ],
      "PoliticalView": "{{string}}",
      "Style": "{{string}}"
   },
   "Description": "{{string}}",
   "MapName": "{{string}}",
   "PricingPlan": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMap_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMap_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configuration](#API_CreateMap_RequestSyntax) **   <a name="location-CreateMap-request-Configuration"></a>
Specifies the `MapConfiguration`, including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.
Type: [MapConfiguration](API_MapConfiguration.md) object
Required: Yes

 ** [Description](#API_CreateMap_RequestSyntax) **   <a name="location-CreateMap-request-Description"></a>
An optional description for the map resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [MapName](#API_CreateMap_RequestSyntax) **   <a name="location-CreateMap-request-MapName"></a>
The name for the map resource.
Requirements:
+ Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique map resource name.
+ No spaces allowed. For example, `ExampleMap`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [PricingPlan](#API_CreateMap_RequestSyntax) **   <a name="location-CreateMap-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [Tags](#API_CreateMap_RequestSyntax) **   <a name="location-CreateMap-request-Tags"></a>
Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
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
<a name="API_CreateMap_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "MapArn": "string",
   "MapName": "string"
}
```

## Response Elements
<a name="API_CreateMap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_CreateMap_ResponseSyntax) **   <a name="location-CreateMap-response-CreateTime"></a>
The timestamp for when the map resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [MapArn](#API_CreateMap_ResponseSyntax) **   <a name="location-CreateMap-response-MapArn"></a>
The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:map/ExampleMap`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [MapName](#API_CreateMap_ResponseSyntax) **   <a name="location-CreateMap-response-MapName"></a>
The name of the map resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

## Errors
<a name="API_CreateMap_Errors"></a>

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
<a name="API_CreateMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreateMap)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreateMap)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreateMap)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreateMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreateMap)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreateMap)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreateMap)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreateMap)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreateMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreateMap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
