---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DeleteRunBatch.html
---

# DeleteRunBatch
<a name="API_DeleteRunBatch"></a>

Deletes the individual workflow runs within a batch. This operation is separate from `DeleteBatch`, which removes the batch metadata.

Delete is only allowed on batches in `PROCESSED` or `CANCELLED` state. Delete operations are non-atomic and may be partially successful. Use `GetBatch` to review `successfulDeleteSubmissionCount` and `failedDeleteSubmissionCount` in the `submissionSummary`. Only one cancel or delete operation per batch is allowed at a time.

## Request Syntax
<a name="API_DeleteRunBatch_RequestSyntax"></a>

```
POST /runBatch/delete HTTP/1.1
Content-type: application/json

{
   "batchId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteRunBatch_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteRunBatch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [batchId](#API_DeleteRunBatch_RequestSyntax) **   <a name="omics-DeleteRunBatch-request-batchId"></a>
The identifier portion of the run batch ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRunBatch_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteRunBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteRunBatch_Errors"></a>

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
<a name="API_DeleteRunBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/DeleteRunBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DeleteRunBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
