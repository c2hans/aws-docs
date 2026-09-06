---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateTracker.html
---

# UpdateTracker
<a name="API_UpdateTracker"></a>

Updates the specified properties of a given tracker resource.

## Request Syntax
<a name="API_UpdateTracker_RequestSyntax"></a>

```
PATCH /tracking/v0/trackers/{{TrackerName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "EventBridgeEnabled": {{boolean}},
   "KmsKeyEnableGeospatialQueries": {{boolean}},
   "PositionFiltering": "{{string}}",
   "PricingPlan": "{{string}}",
   "PricingPlanDataSource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTracker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-uri-TrackerName"></a>
The name of the tracker resource to update.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_UpdateTracker_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-Description"></a>
Updates the description for the tracker resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [EventBridgeEnabled](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-EventBridgeEnabled"></a>
Whether to enable position `UPDATE` events from this tracker to be sent to EventBridge.
You do not need enable this feature to get `ENTER` and `EXIT` events for geofences with this tracker. Those events are always sent to EventBridge.
Type: Boolean
Required: No

 ** [KmsKeyEnableGeospatialQueries](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-KmsKeyEnableGeospatialQueries"></a>
Enables `GeospatialQueries` for a tracker that uses a [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).
This parameter is only used if you are using a KMS customer managed key.
Type: Boolean
Required: No

 ** [PositionFiltering](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-PositionFiltering"></a>
Updates the position filtering for the tracker resource.
Valid values:
+  `TimeBased` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.
+  `DistanceBased` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this distance are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map.
+  `AccuracyBased` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This helps educe the effects of GPS noise when displaying device trajectories on a map, and can help control costs by reducing the number of geofence evaluations.
Type: String
Valid Values: `TimeBased | DistanceBased | AccuracyBased`
Required: No

 ** [PricingPlan](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [PricingPlanDataSource](#API_UpdateTracker_RequestSyntax) **   <a name="location-UpdateTracker-request-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
This parameter is no longer used.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateTracker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TrackerArn": "string",
   "TrackerName": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_UpdateTracker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrackerArn](#API_UpdateTracker_ResponseSyntax) **   <a name="location-UpdateTracker-response-TrackerArn"></a>
The Amazon Resource Name (ARN) of the updated tracker resource. Used to specify a resource across AWS.
+ Format example: `arn:aws:geo:region:account-id:tracker/ExampleTracker`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [TrackerName](#API_UpdateTracker_ResponseSyntax) **   <a name="location-UpdateTracker-response-TrackerName"></a>
The name of the updated tracker resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [UpdateTime](#API_UpdateTracker_ResponseSyntax) **   <a name="location-UpdateTracker-response-UpdateTime"></a>
The timestamp for when the tracker resource was last updated in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_UpdateTracker_Errors"></a>

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
<a name="API_UpdateTracker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/UpdateTracker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/UpdateTracker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/UpdateTracker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/UpdateTracker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/UpdateTracker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/UpdateTracker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/UpdateTracker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/UpdateTracker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/UpdateTracker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/UpdateTracker)
