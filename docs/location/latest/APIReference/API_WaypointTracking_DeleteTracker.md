---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeleteTracker.html
---

# DeleteTracker
<a name="API_WaypointTracking_DeleteTracker"></a>

Deletes a tracker resource from your AWS account.

**Note**
This operation deletes the resource permanently. If the tracker resource is in use, you may encounter an error. Make sure that the target resource isn't a dependency for your applications.

## Request Syntax
<a name="API_WaypointTracking_DeleteTracker_RequestSyntax"></a>

```
DELETE /tracking/v0/trackers/{{TrackerName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_WaypointTracking_DeleteTracker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_WaypointTracking_DeleteTracker_RequestSyntax) **   <a name="location-WaypointTracking_DeleteTracker-request-uri-TrackerName"></a>
The name of the tracker resource to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_DeleteTracker_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_WaypointTracking_DeleteTracker_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_WaypointTracking_DeleteTracker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_WaypointTracking_DeleteTracker_Errors"></a>

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
<a name="API_WaypointTracking_DeleteTracker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/DeleteTracker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/DeleteTracker)
