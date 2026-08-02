---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html
---

# PutRumEvents
<a name="API_PutRumEvents"></a>

Sends telemetry events about your application performance and user behavior to CloudWatch RUM. The code snippet that RUM generates for you to add to your application includes `PutRumEvents` operations to send this data to RUM.

Each `PutRumEvents` operation can send a batch of events from one user session.

## Request Syntax
<a name="API_PutRumEvents_RequestSyntax"></a>

```
POST /appmonitors/{{Id}}/ HTTP/1.1
Content-type: application/json

{
   "Alias": "{{string}}",
   "AppMonitorDetails": {
      "id": "{{string}}",
      "name": "{{string}}",
      "version": "{{string}}"
   },
   "BatchId": "{{string}}",
   "RumEvents": [
      {
         "details": "{{string}}",
         "id": "{{string}}",
         "metadata": "{{string}}",
         "timestamp": {{number}},
         "type": "{{string}}"
      }
   ],
   "UserDetails": {
      "sessionId": "{{string}}",
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutRumEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-uri-Id"></a>
The ID of the app monitor that is sending this data.
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_PutRumEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Alias](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-Alias"></a>
If the app monitor uses a resource-based policy that requires `PutRumEvents` requests to specify a certain alias, specify that alias here. This alias will be compared to the `rum:alias` context key in the resource-based policy. For more information, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [AppMonitorDetails](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-AppMonitorDetails"></a>
A structure that contains information about the app monitor that collected this telemetry information.
Type: [AppMonitorDetails](API_AppMonitorDetails.md) object
Required: Yes

 ** [BatchId](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-BatchId"></a>
A unique identifier for this batch of RUM event data.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [RumEvents](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-RumEvents"></a>
An array of structures that contain the telemetry event data.
Type: Array of [RumEvent](API_RumEvent.md) objects
Required: Yes

 ** [UserDetails](#API_PutRumEvents_RequestSyntax) **   <a name="cloudwatchrum-PutRumEvents-request-UserDetails"></a>
A structure that contains information about the user session that this batch of events was collected from.
Type: [UserDetails](API_UserDetails.md) object
Required: Yes

## Response Syntax
<a name="API_PutRumEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutRumEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutRumEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutRumEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/PutRumEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/PutRumEvents)
