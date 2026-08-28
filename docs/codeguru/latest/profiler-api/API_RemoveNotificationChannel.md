---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemoveNotificationChannel.html
---

# RemoveNotificationChannel
<a name="API_RemoveNotificationChannel"></a>

Remove one anomaly notifications channel for a profiling group.

## Request Syntax
<a name="API_RemoveNotificationChannel_RequestSyntax"></a>

```
DELETE /profilingGroups/{{profilingGroupName}}/notificationConfiguration/{{channelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveNotificationChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelId](#API_RemoveNotificationChannel_RequestSyntax) **   <a name="profiler-RemoveNotificationChannel-request-uri-channelId"></a>
The id of the channel that we want to stop receiving notifications.
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: Yes

 ** [profilingGroupName](#API_RemoveNotificationChannel_RequestSyntax) **   <a name="profiler-RemoveNotificationChannel-request-uri-profilingGroupName"></a>
The name of the profiling group we want to change notification configuration for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_RemoveNotificationChannel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveNotificationChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notificationConfiguration": {
      "channels": [
         {
            "eventPublishers": [ "string" ],
            "id": "string",
            "uri": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_RemoveNotificationChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notificationConfiguration](#API_RemoveNotificationChannel_ResponseSyntax) **   <a name="profiler-RemoveNotificationChannel-response-notificationConfiguration"></a>
The new notification configuration for this profiling group.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object

## Errors
<a name="API_RemoveNotificationChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_RemoveNotificationChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/RemoveNotificationChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/RemoveNotificationChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
