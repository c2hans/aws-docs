---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListDiscoveredEndpoints.html
---

# ListDiscoveredEndpoints
<a name="API_ListDiscoveredEndpoints"></a>

Returns a paginated list of endpoints discovered during a pentest job execution.

## Request Syntax
<a name="API_ListDiscoveredEndpoints_RequestSyntax"></a>

```
POST /ListDiscoveredEndpoints HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pentestJobId": "{{string}}",
   "prefix": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDiscoveredEndpoints_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDiscoveredEndpoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListDiscoveredEndpoints_RequestSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [maxResults](#API_ListDiscoveredEndpoints_RequestSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListDiscoveredEndpoints_RequestSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

 ** [pentestJobId](#API_ListDiscoveredEndpoints_RequestSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-request-pentestJobId"></a>
The unique identifier of the pentest job to list discovered endpoints for.
Type: String
Required: Yes

 ** [prefix](#API_ListDiscoveredEndpoints_RequestSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-request-prefix"></a>
A prefix to filter discovered endpoints by URI.
Type: String
Required: No

## Response Syntax
<a name="API_ListDiscoveredEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "discoveredEndpoints": [
      {
         "agentSpaceId": "string",
         "description": "string",
         "evidence": "string",
         "operation": "string",
         "pentestJobId": "string",
         "taskId": "string",
         "uri": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDiscoveredEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [discoveredEndpoints](#API_ListDiscoveredEndpoints_ResponseSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-response-discoveredEndpoints"></a>
The list of discovered endpoints.
Type: Array of [DiscoveredEndpoint](API_DiscoveredEndpoint.md) objects

 ** [nextToken](#API_ListDiscoveredEndpoints_ResponseSyntax) **   <a name="securityagent-ListDiscoveredEndpoints-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListDiscoveredEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListDiscoveredEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListDiscoveredEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListDiscoveredEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
