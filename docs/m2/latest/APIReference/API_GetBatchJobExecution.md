---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetBatchJobExecution.html
---

# GetBatchJobExecution
<a name="API_GetBatchJobExecution"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Gets the details of a specific batch job execution for a specific application.

## Request Syntax
<a name="API_GetBatchJobExecution_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/batch-job-executions/{{executionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBatchJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetBatchJobExecution_RequestSyntax) **   <a name="m2-GetBatchJobExecution-request-uri-applicationId"></a>
The identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [executionId](#API_GetBatchJobExecution_RequestSyntax) **   <a name="m2-GetBatchJobExecution-request-uri-executionId"></a>
The unique identifier of the batch job execution.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_GetBatchJobExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBatchJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "batchJobIdentifier": { ... },
   "endTime": number,
   "executionId": "string",
   "jobId": "string",
   "jobName": "string",
   "jobStepRestartMarker": {
      "fromProcStep": "string",
      "fromStep": "string",
      "skip": boolean,
      "stepCheckpoint": number,
      "toProcStep": "string",
      "toStep": "string"
   },
   "jobType": "string",
   "jobUser": "string",
   "returnCode": "string",
   "startTime": number,
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetBatchJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-applicationId"></a>
The identifier of the application.
Type: String
Pattern: `\S{1,80}`

 ** [batchJobIdentifier](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-batchJobIdentifier"></a>
The unique identifier of this batch job.
Type: [BatchJobIdentifier](API_BatchJobIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [endTime](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-endTime"></a>
The timestamp when the batch job execution ended.
Type: Timestamp

 ** [executionId](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-executionId"></a>
The unique identifier for this batch job execution.
Type: String
Pattern: `\S{1,80}`

 ** [jobId](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-jobId"></a>
The unique identifier for this batch job.
Type: String
Pattern: `\S{1,100}`

 ** [jobName](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-jobName"></a>
The name of this batch job.
Type: String
Pattern: `\S{1,100}`

 ** [jobStepRestartMarker](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-jobStepRestartMarker"></a>
The step/procedure step information for the restart batch job operation.
Type: [JobStepRestartMarker](API_JobStepRestartMarker.md) object

 ** [jobType](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-jobType"></a>
The type of job.
Type: String
Valid Values: `VSE | JES2 | JES3`

 ** [jobUser](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-jobUser"></a>
The user for the job.
Type: String
Pattern: `\S{1,100}`

 ** [returnCode](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-returnCode"></a>
The batch job return code from either the Blu Age or Micro Focus runtime engines. For more information, see [Batch return codes](https://www.ibm.com/docs/en/was/8.5.5?topic=model-batch-return-codes) in the *IBM WebSphere Application Server* documentation.
Type: String

 ** [startTime](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-startTime"></a>
The timestamp when the batch job execution started.
Type: Timestamp

 ** [status](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-status"></a>
The status of the batch job execution.
Type: String
Valid Values: `Submitting | Holding | Dispatching | Running | Cancelling | Cancelled | Succeeded | Failed | Purged | Succeeded With Warning`

 ** [statusReason](#API_GetBatchJobExecution_ResponseSyntax) **   <a name="m2-GetBatchJobExecution-response-statusReason"></a>
The reason for the reported status.
Type: String

## Errors
<a name="API_GetBatchJobExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_GetBatchJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetBatchJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetBatchJobExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
