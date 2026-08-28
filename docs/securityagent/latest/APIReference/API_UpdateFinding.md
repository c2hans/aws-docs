---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateFinding.html
---

# UpdateFinding
<a name="API_UpdateFinding"></a>

Updates the status or risk level of a security finding.

## Request Syntax
<a name="API_UpdateFinding_RequestSyntax"></a>

```
POST /UpdateFinding HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "attackScript": "{{string}}",
   "customerNote": "{{string}}",
   "description": "{{string}}",
   "findingId": "{{string}}",
   "name": "{{string}}",
   "reasoning": "{{string}}",
   "riskLevel": "{{string}}",
   "riskScore": "{{string}}",
   "riskType": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFinding_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFinding_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the finding.
Type: String
Required: Yes

 ** [attackScript](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-attackScript"></a>
The updated attack script for the finding.
Type: String
Required: No

 ** [customerNote](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-customerNote"></a>
A customer-provided note on the finding.
Type: String
Required: No

 ** [description](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-description"></a>
The updated description for the finding.
Type: String
Required: No

 ** [findingId](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-findingId"></a>
The unique identifier of the finding to update.
Type: String
Required: Yes

 ** [name](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-name"></a>
The updated name for the finding.
Type: String
Required: No

 ** [reasoning](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-reasoning"></a>
The updated reasoning for the finding.
Type: String
Required: No

 ** [riskLevel](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-riskLevel"></a>
The updated risk level for the finding.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** [riskScore](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-riskScore"></a>
The updated numerical risk score for the finding.
Type: String
Required: No

 ** [riskType](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-riskType"></a>
The updated risk type for the finding.
Type: String
Required: No

 ** [status](#API_UpdateFinding_RequestSyntax) **   <a name="securityagent-UpdateFinding-request-status"></a>
The updated status for the finding.
Type: String
Valid Values: `ACTIVE | RESOLVED | ACCEPTED | FALSE_POSITIVE`
Required: No

## Response Syntax
<a name="API_UpdateFinding_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFinding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFinding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
