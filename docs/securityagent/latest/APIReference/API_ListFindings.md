---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListFindings.html
---

# ListFindings
<a name="API_ListFindings"></a>

Lists the security findings for a pentest job.

## Request Syntax
<a name="API_ListFindings_RequestSyntax"></a>

```
POST /ListFindings HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewJobId": "{{string}}",
   "confidence": "{{string}}",
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}",
   "pentestJobId": "{{string}}",
   "riskLevel": "{{string}}",
   "riskType": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [codeReviewJobId](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-codeReviewJobId"></a>
The unique identifier of the code review job to list findings for. Mutually exclusive with pentestJobId.
Type: String
Required: No

 ** [confidence](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-confidence"></a>
Filter findings by confidence level.
Type: String
Valid Values: `FALSE_POSITIVE | UNCONFIRMED | LOW | MEDIUM | HIGH`
Required: No

 ** [maxResults](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [name](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-name"></a>
Filter findings by name.
Type: String
Required: No

 ** [nextToken](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

 ** [pentestJobId](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-pentestJobId"></a>
The unique identifier of the pentest job to list findings for.
Type: String
Required: No

 ** [riskLevel](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-riskLevel"></a>
Filter findings by risk level.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** [riskType](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-riskType"></a>
Filter findings by risk type.
Type: String
Required: No

 ** [status](#API_ListFindings_RequestSyntax) **   <a name="securityagent-ListFindings-request-status"></a>
Filter findings by status.
Type: String
Valid Values: `ACTIVE | RESOLVED | ACCEPTED | FALSE_POSITIVE`
Required: No

## Response Syntax
<a name="API_ListFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingsSummaries": [
      {
         "agentSpaceId": "string",
         "codeReviewId": "string",
         "codeReviewJobId": "string",
         "confidence": "string",
         "createdAt": "string",
         "findingId": "string",
         "name": "string",
         "pentestId": "string",
         "pentestJobId": "string",
         "riskLevel": "string",
         "riskType": "string",
         "status": "string",
         "updatedAt": "string",
         "validationStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingsSummaries](#API_ListFindings_ResponseSyntax) **   <a name="securityagent-ListFindings-response-findingsSummaries"></a>
The list of finding summaries.
Type: Array of [FindingSummary](API_FindingSummary.md) objects

 ** [nextToken](#API_ListFindings_ResponseSyntax) **   <a name="securityagent-ListFindings-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
