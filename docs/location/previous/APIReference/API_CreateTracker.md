---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CreateTracker.html
---

# CreateTracker
<a name="API_CreateTracker"></a>

Creates a tracker resource in your AWS account, which lets you retrieve current and historical location of devices.

## Request Syntax
<a name="API_CreateTracker_RequestSyntax"></a>

```
POST /tracking/v0/trackers HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "EventBridgeEnabled": {{boolean}},
   "KmsKeyEnableGeospatialQueries": {{boolean}},
   "KmsKeyId": "{{string}}",
   "PositionFiltering": "{{string}}",
   "PricingPlan": "{{string}}",
   "PricingPlanDataSource": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TrackerName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTracker_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTracker_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-Description"></a>
An optional description for the tracker resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [EventBridgeEnabled](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-EventBridgeEnabled"></a>
Whether to enable position `UPDATE` events from this tracker to be sent to EventBridge.
You do not need enable this feature to get `ENTER` and `EXIT` events for geofences with this tracker. Those events are always sent to EventBridge.
Type: Boolean
Required: No

 ** [KmsKeyEnableGeospatialQueries](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-KmsKeyEnableGeospatialQueries"></a>
Enables `GeospatialQueries` for a tracker that uses a [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).
This parameter is only used if you are using a KMS customer managed key.
If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.
You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.
Type: Boolean
Required: No

 ** [KmsKeyId](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-KmsKeyId"></a>
A key identifier for an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html). Enter a key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PositionFiltering](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-PositionFiltering"></a>
Specifies the position filtering for the tracker resource.
Valid values:
+  `TimeBased` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.
+  `DistanceBased` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map.
+  `AccuracyBased` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations.
This field is optional. If not specified, the default value is `TimeBased`.
Type: String
Valid Values: `TimeBased | DistanceBased | AccuracyBased`
Required: No

 ** [PricingPlan](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [PricingPlanDataSource](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
This parameter is no longer used.
Type: String
Required: No

 ** [Tags](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-Tags"></a>
Applies one or more tags to the tracker resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
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

 ** [TrackerName](#API_CreateTracker_RequestSyntax) **   <a name="location-CreateTracker-request-TrackerName"></a>
The name for the tracker resource.
Requirements:
+ Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (\_).
+ Must be a unique tracker resource name.
+ No spaces allowed. For example, `ExampleTracker`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Response Syntax
<a name="API_CreateTracker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "TrackerArn": "string",
   "TrackerName": "string"
}
```

## Response Elements
<a name="API_CreateTracker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_CreateTracker_ResponseSyntax) **   <a name="location-CreateTracker-response-CreateTime"></a>
The timestamp for when the tracker resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [TrackerArn](#API_CreateTracker_ResponseSyntax) **   <a name="location-CreateTracker-response-TrackerArn"></a>
The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:tracker/ExampleTracker`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [TrackerName](#API_CreateTracker_ResponseSyntax) **   <a name="location-CreateTracker-response-TrackerName"></a>
The name of the tracker resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

## Errors
<a name="API_CreateTracker_Errors"></a>

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
<a name="API_CreateTracker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CreateTracker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CreateTracker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CreateTracker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CreateTracker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CreateTracker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CreateTracker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CreateTracker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CreateTracker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CreateTracker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CreateTracker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
