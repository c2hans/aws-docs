---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetWorker.html
---

# BatchGetWorker
<a name="API_BatchGetWorker"></a>

Retrieves multiple workers in a single request. This is a batch version of the `GetWorker` API.

The result of getting each worker is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.

## Request Syntax
<a name="API_BatchGetWorker_RequestSyntax"></a>

```
POST /2023-10-12/batch-get-worker HTTP/1.1
Content-type: application/json

{
   "identifiers": [
      {
         "farmId": "{{string}}",
         "fleetId": "{{string}}",
         "workerId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetWorker_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetWorker_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identifiers](#API_BatchGetWorker_RequestSyntax) **   <a name="deadlinecloud-BatchGetWorker-request-identifiers"></a>
The list of worker identifiers to retrieve. You can specify up to 100 identifiers per request.
Type: Array of [BatchGetWorkerIdentifier](API_BatchGetWorkerIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetWorker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "farmId": "string",
         "fleetId": "string",
         "message": "string",
         "workerId": "string"
      }
   ],
   "workers": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "farmId": "string",
         "fleetId": "string",
         "hostProperties": {
            "ec2InstanceArn": "string",
            "ec2InstanceType": "string",
            "hostName": "string",
            "ipAddresses": {
               "ipV4Addresses": [ "string" ],
               "ipV6Addresses": [ "string" ]
            }
         },
         "log": {
            "error": "string",
            "logDriver": "string",
            "options": {
               "string" : "string"
            },
            "parameters": {
               "string" : "string"
            }
         },
         "status": "string",
         "updatedAt": "string",
         "updatedBy": "string",
         "workerId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetWorker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetWorker_ResponseSyntax) **   <a name="deadlinecloud-BatchGetWorker-response-errors"></a>
A list of errors for workers that could not be retrieved.
Type: Array of [BatchGetWorkerError](API_BatchGetWorkerError.md) objects

 ** [workers](#API_BatchGetWorker_ResponseSyntax) **   <a name="deadlinecloud-BatchGetWorker-response-workers"></a>
A list of workers that were successfully retrieved.
Type: Array of [BatchGetWorkerItem](API_BatchGetWorkerItem.md) objects

## Errors
<a name="API_BatchGetWorker_Errors"></a>

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
<a name="API_BatchGetWorker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchGetWorker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetWorker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
