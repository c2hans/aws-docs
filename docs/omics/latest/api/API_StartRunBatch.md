---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartRunBatch.html
---

# StartRunBatch
<a name="API_StartRunBatch"></a>

Starts a batch of workflow runs. You can group up to 100,000 runs into a single batch that share a common configuration defined in `defaultRunSetting`. Per-run overrides can be provided either inline via `inlineSettings` (up to 100 runs) or via a JSON file stored in Amazon S3 via `s3UriSettings` (up to 100,000 runs).

 `StartRunBatch` validates common fields synchronously and returns immediately with a batch ID and status `CREATING`. The batch transitions to `PENDING` once initial setup completes. Runs are then submitted gradually and asynchronously at a rate governed by your `StartRun` throughput quota.

## Request Syntax
<a name="API_StartRunBatch_RequestSyntax"></a>

```
POST /runBatch HTTP/1.1
Content-type: application/json

{
   "batchName": "{{string}}",
   "batchRunSettings": { ... },
   "defaultRunSetting": {
      "cacheBehavior": "{{string}}",
      "cacheId": "{{string}}",
      "configurationName": "{{string}}",
      "engineSettings": {{JSON value}},
      "logLevel": "{{string}}",
      "name": "{{string}}",
      "networkingMode": "{{string}}",
      "outputBucketOwnerId": "{{string}}",
      "outputUri": "{{string}}",
      "parameters": {{JSON value}},
      "priority": {{number}},
      "retentionMode": "{{string}}",
      "roleArn": "{{string}}",
      "runGroupId": "{{string}}",
      "runTags": {
         "{{string}}" : "{{string}}"
      },
      "scratchStorageMode": "{{string}}",
      "storageCapacity": {{number}},
      "storageType": "{{string}}",
      "workflowId": "{{string}}",
      "workflowOwnerId": "{{string}}",
      "workflowType": "{{string}}",
      "workflowVersionName": "{{string}}"
   },
   "requestId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartRunBatch_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRunBatch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [batchName](#API_StartRunBatch_RequestSyntax) **   <a name="omics-StartRunBatch-request-batchName"></a>
An optional user-friendly name for the run batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [batchRunSettings](#API_StartRunBatch_RequestSyntax) **   <a name="omics-StartRunBatch-request-batchRunSettings"></a>
The individual run configurations. Specify exactly one of `inlineSettings` or `s3UriSettings`. See `BatchRunSettings`.
Type: [BatchRunSettings](API_BatchRunSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [defaultRunSetting](#API_StartRunBatch_RequestSyntax) **   <a name="omics-StartRunBatch-request-defaultRunSetting"></a>
Shared configuration applied to all runs in the batch. See `DefaultRunSetting`.
Type: [DefaultRunSetting](API_DefaultRunSetting.md) object
Required: Yes

 ** [requestId](#API_StartRunBatch_RequestSyntax) **   <a name="omics-StartRunBatch-request-requestId"></a>
A client token used to deduplicate retry requests and prevent duplicate batches from being created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [tags](#API_StartRunBatch_RequestSyntax) **   <a name="omics-StartRunBatch-request-tags"></a>
 AWS tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use `defaultRunSetting.runTags`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartRunBatch_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string"
}
```

## Response Elements
<a name="API_StartRunBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StartRunBatch_ResponseSyntax) **   <a name="omics-StartRunBatch-response-arn"></a>
The unique ARN of the run batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [id](#API_StartRunBatch_ResponseSyntax) **   <a name="omics-StartRunBatch-response-id"></a>
The identifier portion of the run batch ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [status](#API_StartRunBatch_ResponseSyntax) **   <a name="omics-StartRunBatch-response-status"></a>
The initial status of the run batch. Returns `CREATING` while the batch is being initialized.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | PENDING | SUBMITTING | INPROGRESS | STOPPING | CANCELLED | FAILED | PROCESSED | RUNS_DELETING | RUNS_DELETE_FAILED | RUNS_DELETED`

 ** [tags](#API_StartRunBatch_ResponseSyntax) **   <a name="omics-StartRunBatch-response-tags"></a>
 AWS tags associated with the run batch.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_StartRunBatch_ResponseSyntax) **   <a name="omics-StartRunBatch-response-uuid"></a>
The universally unique identifier (UUID) for the run batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_StartRunBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

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
<a name="API_StartRunBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/StartRunBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartRunBatch)
