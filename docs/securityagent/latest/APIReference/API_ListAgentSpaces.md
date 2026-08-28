---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListAgentSpaces.html
---

# ListAgentSpaces
<a name="API_ListAgentSpaces"></a>

Returns a paginated list of agent space summaries in your account.

## Request Syntax
<a name="API_ListAgentSpaces_RequestSyntax"></a>

```
POST /ListAgentSpaces HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAgentSpaces_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAgentSpaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListAgentSpaces_RequestSyntax) **   <a name="securityagent-ListAgentSpaces-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListAgentSpaces_RequestSyntax) **   <a name="securityagent-ListAgentSpaces-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListAgentSpaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceSummaries": [
      {
         "agentSpaceId": "string",
         "createdAt": "string",
         "name": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentSpaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceSummaries](#API_ListAgentSpaces_ResponseSyntax) **   <a name="securityagent-ListAgentSpaces-response-agentSpaceSummaries"></a>
The list of agent space summaries.
Type: Array of [AgentSpaceSummary](API_AgentSpaceSummary.md) objects

 ** [nextToken](#API_ListAgentSpaces_ResponseSyntax) **   <a name="securityagent-ListAgentSpaces-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListAgentSpaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAgentSpaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListAgentSpaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListAgentSpaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
