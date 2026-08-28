---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DisassociateTrackerConsumer.html
---

# DisassociateTrackerConsumer
<a name="API_WaypointTracking_DisassociateTrackerConsumer"></a>

Removes the association between a tracker resource and a geofence collection.

**Note**
Once you unlink a tracker resource from a geofence collection, the tracker positions will no longer be automatically evaluated against geofences.

## Request Syntax
<a name="API_WaypointTracking_DisassociateTrackerConsumer_RequestSyntax"></a>

```
DELETE /tracking/v0/trackers/{{TrackerName}}/consumers/{{ConsumerArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_WaypointTracking_DisassociateTrackerConsumer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConsumerArn](#API_WaypointTracking_DisassociateTrackerConsumer_RequestSyntax) **   <a name="location-WaypointTracking_DisassociateTrackerConsumer-request-uri-ConsumerArn"></a>
The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer`
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

 ** [TrackerName](#API_WaypointTracking_DisassociateTrackerConsumer_RequestSyntax) **   <a name="location-WaypointTracking_DisassociateTrackerConsumer-request-uri-TrackerName"></a>
The name of the tracker resource to be dissociated from the consumer.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_DisassociateTrackerConsumer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_WaypointTracking_DisassociateTrackerConsumer_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_WaypointTracking_DisassociateTrackerConsumer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_WaypointTracking_DisassociateTrackerConsumer_Errors"></a>

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
<a name="API_WaypointTracking_DisassociateTrackerConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/DisassociateTrackerConsumer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/DisassociateTrackerConsumer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
