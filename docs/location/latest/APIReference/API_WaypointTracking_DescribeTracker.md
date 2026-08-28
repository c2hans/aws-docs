---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DescribeTracker.html
---

# DescribeTracker
<a name="API_WaypointTracking_DescribeTracker"></a>

Retrieves the tracker resource details.

## Request Syntax
<a name="API_WaypointTracking_DescribeTracker_RequestSyntax"></a>

```
GET /tracking/v0/trackers/{{TrackerName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_WaypointTracking_DescribeTracker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_WaypointTracking_DescribeTracker_RequestSyntax) **   <a name="location-WaypointTracking_DescribeTracker-request-uri-TrackerName"></a>
The name of the tracker resource.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_DescribeTracker_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_WaypointTracking_DescribeTracker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "Description": "string",
   "EventBridgeEnabled": boolean,
   "KmsKeyEnableGeospatialQueries": boolean,
   "KmsKeyId": "string",
   "PositionFiltering": "string",
   "PricingPlan": "string",
   "PricingPlanDataSource": "string",
   "Tags": {
      "string" : "string"
   },
   "TrackerArn": "string",
   "TrackerName": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_WaypointTracking_DescribeTracker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-CreateTime"></a>
The timestamp for when the tracker resource was created in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [Description](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-Description"></a>
The optional description for the tracker resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [EventBridgeEnabled](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-EventBridgeEnabled"></a>
Whether `UPDATE` events from this tracker in EventBridge are enabled. If set to `true` these events will be sent to EventBridge.
Type: Boolean

 ** [KmsKeyEnableGeospatialQueries](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-KmsKeyEnableGeospatialQueries"></a>
Enables `GeospatialQueries` for a tracker that uses a [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).
This parameter is only used if you are using a KMS customer managed key.
If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.
You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.
Type: Boolean

 ** [KmsKeyId](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-KmsKeyId"></a>
A key identifier for an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) assigned to the Amazon Location resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [PositionFiltering](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-PositionFiltering"></a>
The position filtering method of the tracker resource.
Type: String
Valid Values: `TimeBased | DistanceBased | AccuracyBased`

 ** [PricingPlan](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-PricingPlan"></a>
 *This parameter has been deprecated.*
Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`

 ** [PricingPlanDataSource](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
No longer used. Always returns an empty string.
Type: String

 ** [Tags](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-Tags"></a>
The tags associated with the tracker resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [TrackerArn](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-TrackerArn"></a>
The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:tracker/ExampleTracker`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [TrackerName](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-TrackerName"></a>
The name of the tracker resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [UpdateTime](#API_WaypointTracking_DescribeTracker_ResponseSyntax) **   <a name="location-WaypointTracking_DescribeTracker-response-UpdateTime"></a>
The timestamp for when the tracker resource was last updated in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

## Errors
<a name="API_WaypointTracking_DescribeTracker_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_WaypointTracking_DescribeTracker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/DescribeTracker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/DescribeTracker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
