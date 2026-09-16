---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListThreats.html
---

# ListThreats
<a name="API_ListThreats"></a>

Returns a paginated list of threats for a threat model job.

## Request Syntax
<a name="API_ListThreats_RequestSyntax"></a>

```
POST /ListThreats HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "threatJobId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListThreats_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListThreats_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListThreats_RequestSyntax) **   <a name="securityagent-ListThreats-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [maxResults](#API_ListThreats_RequestSyntax) **   <a name="securityagent-ListThreats-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListThreats_RequestSyntax) **   <a name="securityagent-ListThreats-request-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String
Required: No

 ** [threatJobId](#API_ListThreats_RequestSyntax) **   <a name="securityagent-ListThreats-request-threatJobId"></a>
The unique identifier of the threat model job to list threats for.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListThreats_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "threats": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "severity": "string",
         "statement": "string",
         "status": "string",
         "stride": [ "string" ],
         "threatId": "string",
         "threatJobId": "string",
         "title": "string",
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThreats_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThreats_ResponseSyntax) **   <a name="securityagent-ListThreats-response-nextToken"></a>
A token to use for paginating results that are returned in the response.
Type: String

 ** [threats](#API_ListThreats_ResponseSyntax) **   <a name="securityagent-ListThreats-response-threats"></a>
The list of threat summaries.
Type: Array of [ThreatSummary](API_ThreatSummary.md) objects

## Errors
<a name="API_ListThreats_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListThreats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListThreats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListThreats)
