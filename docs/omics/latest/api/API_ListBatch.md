---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListBatch.html
---

# ListBatch
<a name="API_ListBatch"></a>

Returns a list of run batches in your account, with optional filtering by status, name, or run group. Results are paginated. Only one filter per call is supported.

## Request Syntax
<a name="API_ListBatch_RequestSyntax"></a>

```
GET /runBatch?maxItems={{maxItems}}&name={{name}}&runGroupId={{runGroupId}}&startingToken={{startingToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxItems](#API_ListBatch_RequestSyntax) **   <a name="omics-ListBatch-request-uri-maxItems"></a>
The maximum number of batches to return. If not specified, defaults to 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListBatch_RequestSyntax) **   <a name="omics-ListBatch-request-uri-name"></a>
Filter batches by name.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [runGroupId](#API_ListBatch_RequestSyntax) **   <a name="omics-ListBatch-request-uri-runGroupId"></a>
Filter batches by run group ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [startingToken](#API_ListBatch_RequestSyntax) **   <a name="omics-ListBatch-request-uri-startingToken"></a>
A pagination token returned from a prior `ListBatch` call.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_ListBatch_RequestSyntax) **   <a name="omics-ListBatch-request-uri-status"></a>
Filter batches by status.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | PENDING | SUBMITTING | INPROGRESS | STOPPING | CANCELLED | FAILED | PROCESSED | RUNS_DELETING | RUNS_DELETE_FAILED | RUNS_DELETED`

## Request Body
<a name="API_ListBatch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "id": "string",
         "name": "string",
         "status": "string",
         "totalRuns": number,
         "workflowId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListBatch_ResponseSyntax) **   <a name="omics-ListBatch-response-items"></a>
A list of batch summary objects. See `BatchListItem`.
Type: Array of [BatchListItem](API_BatchListItem.md) objects

 ** [nextToken](#API_ListBatch_ResponseSyntax) **   <a name="omics-ListBatch-response-nextToken"></a>
A pagination token to retrieve the next page of results. Absent when no further results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListBatch_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
