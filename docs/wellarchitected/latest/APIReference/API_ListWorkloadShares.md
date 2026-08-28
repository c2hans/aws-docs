---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloadShares.html
---

# ListWorkloadShares
<a name="API_ListWorkloadShares"></a>

List the workload shares associated with the workload.

## Request Syntax
<a name="API_ListWorkloadShares_RequestSyntax"></a>

```
GET /workloads/{{WorkloadId}}/shares?MaxResults={{MaxResults}}&NextToken={{NextToken}}&SharedWithPrefix={{SharedWithPrefix}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkloadShares_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListWorkloadShares_RequestSyntax) **   <a name="wellarchitected-ListWorkloadShares-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListWorkloadShares_RequestSyntax) **   <a name="wellarchitected-ListWorkloadShares-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

 ** [SharedWithPrefix](#API_ListWorkloadShares_RequestSyntax) **   <a name="wellarchitected-ListWorkloadShares-request-uri-SharedWithPrefix"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload is shared.
Length Constraints: Maximum length of 100.

 ** [Status](#API_ListWorkloadShares_RequestSyntax) **   <a name="wellarchitected-ListWorkloadShares-request-uri-Status"></a>
The status of the share request.
Valid Values: `ACCEPTED | REJECTED | PENDING | REVOKED | EXPIRED | ASSOCIATING | ASSOCIATED | FAILED`

 ** [WorkloadId](#API_ListWorkloadShares_RequestSyntax) **   <a name="wellarchitected-ListWorkloadShares-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_ListWorkloadShares_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkloadShares_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "WorkloadId": "string",
   "WorkloadShareSummaries": [
      {
         "PermissionType": "string",
         "SharedWith": "string",
         "ShareId": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkloadShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWorkloadShares_ResponseSyntax) **   <a name="wellarchitected-ListWorkloadShares-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [WorkloadId](#API_ListWorkloadShares_ResponseSyntax) **   <a name="wellarchitected-ListWorkloadShares-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

 ** [WorkloadShareSummaries](#API_ListWorkloadShares_ResponseSyntax) **   <a name="wellarchitected-ListWorkloadShares-response-WorkloadShareSummaries"></a>
A list of workload share summaries.
Type: Array of [WorkloadShareSummary](API_WorkloadShareSummary.md) objects

## Errors
<a name="API_ListWorkloadShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkloadShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListWorkloadShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListWorkloadShares)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
