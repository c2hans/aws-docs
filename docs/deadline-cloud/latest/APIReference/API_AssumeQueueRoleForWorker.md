---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForWorker.html
---

# AssumeQueueRoleForWorker
<a name="API_AssumeQueueRoleForWorker"></a>

Allows a worker to assume a queue role.

## Request Syntax
<a name="API_AssumeQueueRoleForWorker_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/fleets/{{fleetId}}/workers/{{workerId}}/queue-roles?queueId={{queueId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_AssumeQueueRoleForWorker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_AssumeQueueRoleForWorker_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForWorker-request-uri-farmId"></a>
The farm ID of the worker assuming the queue role.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [fleetId](#API_AssumeQueueRoleForWorker_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForWorker-request-uri-fleetId"></a>
The fleet ID of the worker assuming the queue role.
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_AssumeQueueRoleForWorker_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForWorker-request-uri-queueId"></a>
The queue ID of the worker assuming the queue role.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** [workerId](#API_AssumeQueueRoleForWorker_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForWorker-request-uri-workerId"></a>
The worker ID of the worker assuming the queue role.
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_AssumeQueueRoleForWorker_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AssumeQueueRoleForWorker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "credentials": {
      "accessKeyId": "string",
      "expiration": "string",
      "secretAccessKey": "string",
      "sessionToken": "string"
   }
}
```

## Response Elements
<a name="API_AssumeQueueRoleForWorker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentials](#API_AssumeQueueRoleForWorker_ResponseSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForWorker-response-credentials"></a>
The AWS credentials for the role that the worker is assuming.
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_AssumeQueueRoleForWorker_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** context **
Information about the resources in use when the exception was thrown.
 ** reason **
A description of the error.
 ** resourceId **
The identifier of the resource in use.
 ** resourceType **
The type of the resource in use.
HTTP Status Code: 409

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
<a name="API_AssumeQueueRoleForWorker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssumeQueueRoleForWorker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssumeQueueRoleForWorker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
