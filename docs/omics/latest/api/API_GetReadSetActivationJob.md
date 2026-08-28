---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetActivationJob.html
---

# GetReadSetActivationJob
<a name="API_GetReadSetActivationJob"></a>

Returns detailed information about the status of a read set activation job in JSON format.

## Request Syntax
<a name="API_GetReadSetActivationJob_RequestSyntax"></a>

```
GET /sequencestore/{{sequenceStoreId}}/activationjob/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReadSetActivationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReadSetActivationJob_RequestSyntax) **   <a name="omics-GetReadSetActivationJob-request-uri-id"></a>
The job's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [sequenceStoreId](#API_GetReadSetActivationJob_RequestSyntax) **   <a name="omics-GetReadSetActivationJob-request-uri-sequenceStoreId"></a>
The job's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReadSetActivationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReadSetActivationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completionTime": "string",
   "creationTime": "string",
   "id": "string",
   "sequenceStoreId": "string",
   "sources": [
      {
         "readSetId": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ],
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_GetReadSetActivationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completionTime](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-completionTime"></a>
When the job completed.
Type: Timestamp

 ** [creationTime](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [id](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sequenceStoreId](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-sequenceStoreId"></a>
The job's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sources](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-sources"></a>
The job's source files.
Type: Array of [ActivateReadSetSourceItem](API_ActivateReadSetSourceItem.md) objects

 ** [status](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

 ** [statusMessage](#API_GetReadSetActivationJob_ResponseSyntax) **   <a name="omics-GetReadSetActivationJob-response-statusMessage"></a>
The job's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetReadSetActivationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetReadSetActivationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReadSetActivationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReadSetActivationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
