---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DeleteAgentSpace.html
---

# DeleteAgentSpace
<a name="API_DeleteAgentSpace"></a>

Deletes an agent space and all of its associated resources, including pentests, findings, and artifacts.

## Request Syntax
<a name="API_DeleteAgentSpace_RequestSyntax"></a>

```
POST /DeleteAgentSpace HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteAgentSpace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAgentSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_DeleteAgentSpace_RequestSyntax) **   <a name="securityagent-DeleteAgentSpace-request-agentSpaceId"></a>
The unique identifier of the agent space to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteAgentSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string"
}
```

## Response Elements
<a name="API_DeleteAgentSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_DeleteAgentSpace_ResponseSyntax) **   <a name="securityagent-DeleteAgentSpace-response-agentSpaceId"></a>
The unique identifier of the deleted agent space.
Type: String

## Errors
<a name="API_DeleteAgentSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteAgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/DeleteAgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DeleteAgentSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
