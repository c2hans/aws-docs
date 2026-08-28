---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueEnvironment.html
---

# UpdateQueueEnvironment
<a name="API_UpdateQueueEnvironment"></a>

Updates the queue environment.

## Request Syntax
<a name="API_UpdateQueueEnvironment_RequestSyntax"></a>

```
PATCH /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/environments/{{queueEnvironmentId}} HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "priority": {{number}},
   "template": "{{string}}",
   "templateType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateQueueEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [farmId](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-uri-farmId"></a>
The farm ID of the queue environment to update.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [queueEnvironmentId](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-uri-queueEnvironmentId"></a>
The queue environment ID to update.
Pattern: `queueenv-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-uri-queueId"></a>
The queue ID of the queue environment to update.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateQueueEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [priority](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-priority"></a>
The priority to update.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** [template](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-template"></a>
The template to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15000.
Required: No

 ** [templateType](#API_UpdateQueueEnvironment_RequestSyntax) **   <a name="deadlinecloud-UpdateQueueEnvironment-request-templateType"></a>
The template type to update.
Type: String
Valid Values: `JSON | YAML`
Required: No

## Response Syntax
<a name="API_UpdateQueueEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateQueueEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateQueueEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateQueueEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueueEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueueEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
