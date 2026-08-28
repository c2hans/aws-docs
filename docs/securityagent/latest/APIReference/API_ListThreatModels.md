---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListThreatModels.html
---

# ListThreatModels
<a name="API_ListThreatModels"></a>

Returns a paginated list of threat model summaries for the specified agent space.

## Request Syntax
<a name="API_ListThreatModels_RequestSyntax"></a>

```
POST /ListThreatModels HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListThreatModels_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListThreatModels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListThreatModels_RequestSyntax) **   <a name="securityagent-ListThreatModels-request-agentSpaceId"></a>
The unique identifier of the agent space to list threat models for.
Type: String
Required: Yes

 ** [maxResults](#API_ListThreatModels_RequestSyntax) **   <a name="securityagent-ListThreatModels-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListThreatModels_RequestSyntax) **   <a name="securityagent-ListThreatModels-request-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String
Required: No

## Response Syntax
<a name="API_ListThreatModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "threatModelSummaries": [
      {
         "agentSpaceId": "string",
         "createdAt": "string",
         "threatModelId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThreatModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThreatModels_ResponseSyntax) **   <a name="securityagent-ListThreatModels-response-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String

 ** [threatModelSummaries](#API_ListThreatModels_ResponseSyntax) **   <a name="securityagent-ListThreatModels-response-threatModelSummaries"></a>
The list of threat model summaries.
Type: Array of [ThreatModelSummary](API_ThreatModelSummary.md) objects

## Errors
<a name="API_ListThreatModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListThreatModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListThreatModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListThreatModels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
