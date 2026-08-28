---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForUser.html
---

# AssumeQueueRoleForUser
<a name="API_AssumeQueueRoleForUser"></a>

Allows a user to assume a role for a queue.

## Request Syntax
<a name="API_AssumeQueueRoleForUser_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/user-roles HTTP/1.1
```

## URI Request Parameters
<a name="API_AssumeQueueRoleForUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_AssumeQueueRoleForUser_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForUser-request-uri-farmId"></a>
The farm ID of the queue that the user assumes the role for.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_AssumeQueueRoleForUser_RequestSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForUser-request-uri-queueId"></a>
The queue ID of the queue that the user assumes the role for.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_AssumeQueueRoleForUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AssumeQueueRoleForUser_ResponseSyntax"></a>

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
<a name="API_AssumeQueueRoleForUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentials](#API_AssumeQueueRoleForUser_ResponseSyntax) **   <a name="deadlinecloud-AssumeQueueRoleForUser-response-credentials"></a>
The credentials for the queue role that a user has access to.
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_AssumeQueueRoleForUser_Errors"></a>

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
<a name="API_AssumeQueueRoleForUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssumeQueueRoleForUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssumeQueueRoleForUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
