---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceImportJob.html
---

# GetReferenceImportJob
<a name="API_GetReferenceImportJob"></a>

Monitors the status of a reference import job. This operation can be called after calling the `StartReferenceImportJob` operation.

## Request Syntax
<a name="API_GetReferenceImportJob_RequestSyntax"></a>

```
GET /referencestore/{{referenceStoreId}}/importjob/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReferenceImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReferenceImportJob_RequestSyntax) **   <a name="omics-GetReferenceImportJob-request-uri-id"></a>
The job's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [referenceStoreId](#API_GetReferenceImportJob_RequestSyntax) **   <a name="omics-GetReferenceImportJob-request-uri-referenceStoreId"></a>
The job's reference store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReferenceImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReferenceImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completionTime": "string",
   "creationTime": "string",
   "id": "string",
   "referenceStoreId": "string",
   "roleArn": "string",
   "sources": [
      {
         "description": "string",
         "name": "string",
         "referenceId": "string",
         "sourceFile": "string",
         "status": "string",
         "statusMessage": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_GetReferenceImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completionTime](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-completionTime"></a>
When the job completed.
Type: Timestamp

 ** [creationTime](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [id](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [referenceStoreId](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-referenceStoreId"></a>
The job's reference store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [roleArn](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-roleArn"></a>
The job's service role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [sources](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-sources"></a>
The job's source files.
Type: Array of [ImportReferenceSourceItem](API_ImportReferenceSourceItem.md) objects

 ** [status](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

 ** [statusMessage](#API_GetReferenceImportJob_ResponseSyntax) **   <a name="omics-GetReferenceImportJob-response-statusMessage"></a>
The job's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetReferenceImportJob_Errors"></a>

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
<a name="API_GetReferenceImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReferenceImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReferenceImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
