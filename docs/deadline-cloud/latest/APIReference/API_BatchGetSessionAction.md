---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionAction.html
---

# BatchGetSessionAction
<a name="API_BatchGetSessionAction"></a>

Retrieves multiple session actions in a single request. This is a batch version of the `GetSessionAction` API.

The result of getting each session action is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.

## Request Syntax
<a name="API_BatchGetSessionAction_RequestSyntax"></a>

```
POST /2023-10-12/batch-get-session-action HTTP/1.1
Content-type: application/json

{
   "identifiers": [
      {
         "farmId": "{{string}}",
         "jobId": "{{string}}",
         "queueId": "{{string}}",
         "sessionActionId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetSessionAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetSessionAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identifiers](#API_BatchGetSessionAction_RequestSyntax) **   <a name="deadlinecloud-BatchGetSessionAction-request-identifiers"></a>
The list of session action identifiers to retrieve. You can specify up to 100 identifiers per request.
Type: Array of [BatchGetSessionActionIdentifier](API_BatchGetSessionActionIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetSessionAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "farmId": "string",
         "jobId": "string",
         "message": "string",
         "queueId": "string",
         "sessionActionId": "string"
      }
   ],
   "sessionActions": [
      {
         "acquiredLimits": [
            {
               "count": number,
               "limitId": "string"
            }
         ],
         "definition": { ... },
         "endedAt": "string",
         "farmId": "string",
         "jobId": "string",
         "manifests": [
            {
               "outputManifestHash": "string",
               "outputManifestPath": "string"
            }
         ],
         "processExitCode": number,
         "progressMessage": "string",
         "progressPercent": number,
         "queueId": "string",
         "sessionActionId": "string",
         "sessionId": "string",
         "startedAt": "string",
         "status": "string",
         "workerUpdatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSessionAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetSessionAction_ResponseSyntax) **   <a name="deadlinecloud-BatchGetSessionAction-response-errors"></a>
A list of errors for session actions that could not be retrieved.
Type: Array of [BatchGetSessionActionError](API_BatchGetSessionActionError.md) objects

 ** [sessionActions](#API_BatchGetSessionAction_ResponseSyntax) **   <a name="deadlinecloud-BatchGetSessionAction-response-sessionActions"></a>
A list of session actions that were successfully retrieved.
Type: Array of [BatchGetSessionActionItem](API_BatchGetSessionActionItem.md) objects

## Errors
<a name="API_BatchGetSessionAction_Errors"></a>

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
<a name="API_BatchGetSessionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchGetSessionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
