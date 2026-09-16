---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetExportJob.html
---

# StartReadSetExportJob
<a name="API_StartReadSetExportJob"></a>

Starts a read set export job. When the export job is finished, the read set is exported to an Amazon S3 bucket which can be retrieved using the `GetReadSetExportJob` API operation.

To monitor the status of the export job, use the `ListReadSetExportJobs` API operation.

## Request Syntax
<a name="API_StartReadSetExportJob_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/exportjob HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "destination": "{{string}}",
   "roleArn": "{{string}}",
   "sources": [
      {
         "readSetId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartReadSetExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_StartReadSetExportJob_RequestSyntax) **   <a name="omics-StartReadSetExportJob-request-uri-sequenceStoreId"></a>
The read set's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_StartReadSetExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartReadSetExportJob_RequestSyntax) **   <a name="omics-StartReadSetExportJob-request-clientToken"></a>
To ensure that jobs don't run multiple times, specify a unique token for each job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [destination](#API_StartReadSetExportJob_RequestSyntax) **   <a name="omics-StartReadSetExportJob-request-destination"></a>
A location for exported files in Amazon S3.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`
Required: Yes

 ** [roleArn](#API_StartReadSetExportJob_RequestSyntax) **   <a name="omics-StartReadSetExportJob-request-roleArn"></a>
A service role for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [sources](#API_StartReadSetExportJob_RequestSyntax) **   <a name="omics-StartReadSetExportJob-request-sources"></a>
The job's source files.
Type: Array of [ExportReadSet](API_ExportReadSet.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_StartReadSetExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "destination": "string",
   "id": "string",
   "sequenceStoreId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartReadSetExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_StartReadSetExportJob_ResponseSyntax) **   <a name="omics-StartReadSetExportJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [destination](#API_StartReadSetExportJob_ResponseSyntax) **   <a name="omics-StartReadSetExportJob-response-destination"></a>
The job's output location.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`

 ** [id](#API_StartReadSetExportJob_ResponseSyntax) **   <a name="omics-StartReadSetExportJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sequenceStoreId](#API_StartReadSetExportJob_ResponseSyntax) **   <a name="omics-StartReadSetExportJob-response-sequenceStoreId"></a>
The read set's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [status](#API_StartReadSetExportJob_ResponseSyntax) **   <a name="omics-StartReadSetExportJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

## Errors
<a name="API_StartReadSetExportJob_Errors"></a>

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
<a name="API_StartReadSetExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/StartReadSetExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartReadSetExportJob)
