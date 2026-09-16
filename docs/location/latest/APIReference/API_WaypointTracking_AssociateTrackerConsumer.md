---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_AssociateTrackerConsumer.html
---

# AssociateTrackerConsumer
<a name="API_WaypointTracking_AssociateTrackerConsumer"></a>

Creates an association between a geofence collection and a tracker resource. This allows the tracker resource to communicate location data to the linked geofence collection.

You can associate up to five geofence collections to each tracker resource.

**Note**
Currently not supported — Cross-account configurations, such as creating associations between a tracker resource in one account and a geofence collection in another account.

## Request Syntax
<a name="API_WaypointTracking_AssociateTrackerConsumer_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/consumers HTTP/1.1
Content-type: application/json

{
   "ConsumerArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_WaypointTracking_AssociateTrackerConsumer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_WaypointTracking_AssociateTrackerConsumer_RequestSyntax) **   <a name="location-WaypointTracking_AssociateTrackerConsumer-request-uri-TrackerName"></a>
The name of the tracker resource to be associated with a geofence collection.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_AssociateTrackerConsumer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConsumerArn](#API_WaypointTracking_AssociateTrackerConsumer_RequestSyntax) **   <a name="location-WaypointTracking_AssociateTrackerConsumer-request-ConsumerArn"></a>
The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

## Response Syntax
<a name="API_WaypointTracking_AssociateTrackerConsumer_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_WaypointTracking_AssociateTrackerConsumer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_WaypointTracking_AssociateTrackerConsumer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** ConflictException **

HTTP Status Code: 409

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ServiceQuotaExceededException **

HTTP Status Code: 402

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_WaypointTracking_AssociateTrackerConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/AssociateTrackerConsumer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/AssociateTrackerConsumer)
