---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetImportJob.html
---

# StartReadSetImportJob
<a name="API_StartReadSetImportJob"></a>

Imports a read set from the sequence store. Read set import jobs support a maximum of 100 read sets of different types. Monitor the progress of your read set import job by calling the `GetReadSetImportJob` API operation.

## Request Syntax
<a name="API_StartReadSetImportJob_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/importjob HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "roleArn": "{{string}}",
   "sources": [
      {
         "description": "{{string}}",
         "generatedFrom": "{{string}}",
         "name": "{{string}}",
         "referenceArn": "{{string}}",
         "sampleId": "{{string}}",
         "sourceFiles": {
            "source1": "{{string}}",
            "source2": "{{string}}"
         },
         "sourceFileType": "{{string}}",
         "subjectId": "{{string}}",
         "tags": {
            "{{string}}" : "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartReadSetImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_StartReadSetImportJob_RequestSyntax) **   <a name="omics-StartReadSetImportJob-request-uri-sequenceStoreId"></a>
The read set's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_StartReadSetImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartReadSetImportJob_RequestSyntax) **   <a name="omics-StartReadSetImportJob-request-clientToken"></a>
To ensure that jobs don't run multiple times, specify a unique token for each job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [roleArn](#API_StartReadSetImportJob_RequestSyntax) **   <a name="omics-StartReadSetImportJob-request-roleArn"></a>
A service role for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [sources](#API_StartReadSetImportJob_RequestSyntax) **   <a name="omics-StartReadSetImportJob-request-sources"></a>
The job's source files.
Type: Array of [StartReadSetImportJobSourceItem](API_StartReadSetImportJobSourceItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_StartReadSetImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "id": "string",
   "roleArn": "string",
   "sequenceStoreId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartReadSetImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_StartReadSetImportJob_ResponseSyntax) **   <a name="omics-StartReadSetImportJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [id](#API_StartReadSetImportJob_ResponseSyntax) **   <a name="omics-StartReadSetImportJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [roleArn](#API_StartReadSetImportJob_ResponseSyntax) **   <a name="omics-StartReadSetImportJob-response-roleArn"></a>
The job's service role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [sequenceStoreId](#API_StartReadSetImportJob_ResponseSyntax) **   <a name="omics-StartReadSetImportJob-response-sequenceStoreId"></a>
The read set's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [status](#API_StartReadSetImportJob_ResponseSyntax) **   <a name="omics-StartReadSetImportJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

## Errors
<a name="API_StartReadSetImportJob_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartReadSetImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/StartReadSetImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartReadSetImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
