---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListThreatModelJobs.html
---

# ListThreatModelJobs
<a name="API_ListThreatModelJobs"></a>

Returns a paginated list of threat model job summaries for the specified threat model.

## Request Syntax
<a name="API_ListThreatModelJobs_RequestSyntax"></a>

```
POST /ListThreatModelJobs HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "threatModelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListThreatModelJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListThreatModelJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListThreatModelJobs_RequestSyntax) **   <a name="securityagent-ListThreatModelJobs-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [maxResults](#API_ListThreatModelJobs_RequestSyntax) **   <a name="securityagent-ListThreatModelJobs-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListThreatModelJobs_RequestSyntax) **   <a name="securityagent-ListThreatModelJobs-request-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String
Required: No

 ** [threatModelId](#API_ListThreatModelJobs_RequestSyntax) **   <a name="securityagent-ListThreatModelJobs-request-threatModelId"></a>
The unique identifier of the threat model to list jobs for.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListThreatModelJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "threatModelJobSummaries": [
      {
         "agentSpaceId": "string",
         "createdAt": "string",
         "status": "string",
         "threatModelId": "string",
         "threatModelJobId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThreatModelJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThreatModelJobs_ResponseSyntax) **   <a name="securityagent-ListThreatModelJobs-response-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String

 ** [threatModelJobSummaries](#API_ListThreatModelJobs_ResponseSyntax) **   <a name="securityagent-ListThreatModelJobs-response-threatModelJobSummaries"></a>
The list of threat model job summaries.
Type: Array of [ThreatModelJobSummary](API_ThreatModelJobSummary.md) objects

## Errors
<a name="API_ListThreatModelJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListThreatModelJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListThreatModelJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListThreatModelJobs)
