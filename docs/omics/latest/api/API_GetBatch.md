---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetBatch.html
---

# GetBatch
<a name="API_GetBatch"></a>

Retrieves details and current status for a specific run batch, including submission progress and run execution counts.

## Request Syntax
<a name="API_GetBatch_RequestSyntax"></a>

```
GET /runBatch/{{batchId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchId](#API_GetBatch_RequestSyntax) **   <a name="omics-GetBatch-request-uri-batchId"></a>
The identifier portion of the run batch ARN.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetBatch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "defaultRunSetting": {
      "cacheBehavior": "string",
      "cacheId": "string",
      "configurationName": "string",
      "engineSettings": JSON value,
      "logLevel": "string",
      "name": "string",
      "networkingMode": "string",
      "outputBucketOwnerId": "string",
      "outputUri": "string",
      "parameters": JSON value,
      "priority": number,
      "retentionMode": "string",
      "roleArn": "string",
      "runGroupId": "string",
      "runTags": {
         "string" : "string"
      },
      "scratchStorageMode": "string",
      "sessionPolicy": "string",
      "storageCapacity": number,
      "storageType": "string",
      "workflowId": "string",
      "workflowOwnerId": "string",
      "workflowType": "string",
      "workflowVersionName": "string"
   },
   "failedTime": "string",
   "failureReason": "string",
   "id": "string",
   "name": "string",
   "processedTime": "string",
   "runSummary": {
      "cancelledRunCount": number,
      "completedRunCount": number,
      "deletedRunCount": number,
      "failedRunCount": number,
      "pendingRunCount": number,
      "runningRunCount": number,
      "startingRunCount": number,
      "stoppingRunCount": number
   },
   "status": "string",
   "submissionSummary": {
      "failedCancelSubmissionCount": number,
      "failedDeleteSubmissionCount": number,
      "failedStartSubmissionCount": number,
      "pendingStartSubmissionCount": number,
      "successfulCancelSubmissionCount": number,
      "successfulDeleteSubmissionCount": number,
      "successfulStartSubmissionCount": number
   },
   "submittedTime": "string",
   "tags": {
      "string" : "string"
   },
   "totalRuns": number,
   "uuid": "string"
}
```

## Response Elements
<a name="API_GetBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-arn"></a>
The unique ARN of the run batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [creationTime](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-creationTime"></a>
The timestamp when the batch was created.
Type: Timestamp

 ** [defaultRunSetting](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-defaultRunSetting"></a>
The shared configuration applied to all runs in the batch. See `DefaultRunSetting`.
Type: [DefaultRunSetting](API_DefaultRunSetting.md) object

 ** [failedTime](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-failedTime"></a>
The timestamp when the batch transitioned to a `FAILED` status.
Type: Timestamp

 ** [failureReason](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-failureReason"></a>
A description of the batch failure. Present only when status is `FAILED`.
Type: String

 ** [id](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-id"></a>
The identifier portion of the run batch ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [name](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-name"></a>
The optional user-friendly name of the batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [processedTime](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-processedTime"></a>
The timestamp when all run executions completed.
Type: Timestamp

 ** [runSummary](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-runSummary"></a>
A summary of run execution states. Run execution counts are eventually consistent and may lag behind actual run states. Final counts are accurate once the batch reaches `PROCESSED` status. See `RunSummary`.
Type: [RunSummary](API_RunSummary.md) object

 ** [status](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-status"></a>
The current status of the run batch. Possible values: `CREATING` (initial setup), `PENDING` (ready to submit runs), `SUBMITTING` (submitting runs), `INPROGRESS` (runs executing), `STOPPING` (cancellation in progress), `PROCESSED` (all runs completed), `CANCELLED` (batch cancelled), `FAILED` (batch failed), `RUNS_DELETING` (deleting runs), `RUNS_DELETE_FAILED` (run deletion failed for some or all runs), `RUNS_DELETED` (runs deleted).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | PENDING | SUBMITTING | INPROGRESS | STOPPING | CANCELLED | FAILED | PROCESSED | RUNS_DELETING | RUNS_DELETE_FAILED | RUNS_DELETED`

 ** [submissionSummary](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-submissionSummary"></a>
A summary of run submission outcomes. See `SubmissionSummary`.
Type: [SubmissionSummary](API_SubmissionSummary.md) object

 ** [submittedTime](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-submittedTime"></a>
The timestamp when all run submissions completed.
Type: Timestamp

 ** [tags](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-tags"></a>
 AWS tags associated with the run batch.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [totalRuns](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-totalRuns"></a>
The total number of runs in the batch.
Type: Integer

 ** [uuid](#API_GetBatch_ResponseSyntax) **   <a name="omics-GetBatch-response-uuid"></a>
The universally unique identifier (UUID) for the run batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetBatch_Errors"></a>

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
<a name="API_GetBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetBatch)
