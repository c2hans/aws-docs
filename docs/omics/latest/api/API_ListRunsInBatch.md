---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListRunsInBatch.html
---

# ListRunsInBatch
<a name="API_ListRunsInBatch"></a>

Returns a paginated list of individual workflow runs within a specific batch. Use this operation to map each `runSettingId` to its HealthOmics-generated `runId`, and to check the submission status of each run. Only one filter per call is supported.

## Request Syntax
<a name="API_ListRunsInBatch_RequestSyntax"></a>

```
GET /runBatch/{{batchId}}/run?maxItems={{maxItems}}&runId={{runId}}&runSettingId={{runSettingId}}&startingToken={{startingToken}}&submissionStatus={{submissionStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRunsInBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchId](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-batchId"></a>
The identifier portion of the run batch ARN.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [maxItems](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-maxItems"></a>
The maximum number of runs to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [runId](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-runId"></a>
Filter runs by the HealthOmics-generated run ID.

 ** [runSettingId](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-runSettingId"></a>
Filter runs by the customer-provided run setting ID.

 ** [startingToken](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-startingToken"></a>
A pagination token returned from a prior `ListRunsInBatch` call.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [submissionStatus](#API_ListRunsInBatch_RequestSyntax) **   <a name="omics-ListRunsInBatch-request-uri-submissionStatus"></a>
Filter runs by submission status.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `SUCCESS | FAILED | CANCEL_SUCCESS | CANCEL_FAILED | DELETE_SUCCESS | DELETE_FAILED`

## Request Body
<a name="API_ListRunsInBatch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRunsInBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "runs": [
      {
         "runArn": "string",
         "runId": "string",
         "runInternalUuid": "string",
         "runSettingId": "string",
         "submissionFailureMessage": "string",
         "submissionFailureReason": "string",
         "submissionStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRunsInBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRunsInBatch_ResponseSyntax) **   <a name="omics-ListRunsInBatch-response-nextToken"></a>
A pagination token to retrieve the next page of results. Absent when the last run has been returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [runs](#API_ListRunsInBatch_ResponseSyntax) **   <a name="omics-ListRunsInBatch-response-runs"></a>
A list of run entries in the batch. See `RunBatchListItem`.
Type: Array of [RunBatchListItem](API_RunBatchListItem.md) objects

## Errors
<a name="API_ListRunsInBatch_Errors"></a>

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
<a name="API_ListRunsInBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListRunsInBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListRunsInBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
