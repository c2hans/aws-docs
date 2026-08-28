---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AddNotificationChannels.html
---

# AddNotificationChannels
<a name="API_AddNotificationChannels"></a>

Add up to 2 anomaly notifications channels for a profiling group.

## Request Syntax
<a name="API_AddNotificationChannels_RequestSyntax"></a>

```
POST /profilingGroups/{{profilingGroupName}}/notificationConfiguration HTTP/1.1
Content-type: application/json

{
   "channels": [
      {
         "eventPublishers": [ "{{string}}" ],
         "id": "{{string}}",
         "uri": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_AddNotificationChannels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profilingGroupName](#API_AddNotificationChannels_RequestSyntax) **   <a name="profiler-AddNotificationChannels-request-uri-profilingGroupName"></a>
The name of the profiling group that we are setting up notifications for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_AddNotificationChannels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channels](#API_AddNotificationChannels_RequestSyntax) **   <a name="profiler-AddNotificationChannels-request-channels"></a>
One or 2 channels to report to when anomalies are detected.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## Response Syntax
<a name="API_AddNotificationChannels_ResponseSyntax"></a>

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
<a name="API_AddNotificationChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notificationConfiguration](#API_AddNotificationChannels_ResponseSyntax) **   <a name="profiler-AddNotificationChannels-response-notificationConfiguration"></a>
The new notification configuration for this profiling group.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object

## Errors
<a name="API_AddNotificationChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_AddNotificationChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/AddNotificationChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/AddNotificationChannels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
