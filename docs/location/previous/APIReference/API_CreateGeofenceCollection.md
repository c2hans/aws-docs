---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreateGeofenceCollection.html
---

# CreateGeofenceCollection
<a name="API_CreateGeofenceCollection"></a>

Creates a geofence collection, which manages and stores geofences.

## Request Syntax
<a name="API_CreateGeofenceCollection_RequestSyntax"></a>

```
POST /geofencing/v0/collections HTTP/1.1
Content-type: application/json

{
   "CollectionName": "{{string}}",
   "Description": "{{string}}",
   "KmsKeyId": "{{string}}",
   "PricingPlan": "{{string}}",
   "PricingPlanDataSource": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGeofenceCollection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGeofenceCollection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CollectionName](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-CollectionName"></a>
A custom name for the geofence collection.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique geofence collection name.
+ No spaces allowed. For example, `ExampleGeofenceCollection`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Description](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-Description"></a>
An optional description for the geofence collection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [KmsKeyId](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-KmsKeyId"></a>
A key identifier for an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html). Enter a key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PricingPlan](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [PricingPlanDataSource](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
This parameter is no longer used.
Type: String
Required: No

 ** [Tags](#API_CreateGeofenceCollection_RequestSyntax) **   <a name="location-CreateGeofenceCollection-request-Tags"></a>
Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
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
<a name="API_CreateGeofenceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CollectionArn": "string",
   "CollectionName": "string",
   "CreateTime": "string"
}
```

## Response Elements
<a name="API_CreateGeofenceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CollectionArn](#API_CreateGeofenceCollection_ResponseSyntax) **   <a name="location-CreateGeofenceCollection-response-CollectionArn"></a>
The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [CollectionName](#API_CreateGeofenceCollection_ResponseSyntax) **   <a name="location-CreateGeofenceCollection-response-CollectionName"></a>
The name for the geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [CreateTime](#API_CreateGeofenceCollection_ResponseSyntax) **   <a name="location-CreateGeofenceCollection-response-CreateTime"></a>
The timestamp for when the geofence collection was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

## Errors
<a name="API_CreateGeofenceCollection_Errors"></a>

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
<a name="API_CreateGeofenceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreateGeofenceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreateGeofenceCollection)
