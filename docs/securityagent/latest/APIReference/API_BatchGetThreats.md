---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetThreats.html
---

# BatchGetThreats
<a name="API_BatchGetThreats"></a>

Retrieves information about one or more threats.

## Request Syntax
<a name="API_BatchGetThreats_RequestSyntax"></a>

```
POST /BatchGetThreats HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetThreats_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetThreats_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetThreats_RequestSyntax) **   <a name="securityagent-BatchGetThreats-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [threatIds](#API_BatchGetThreats_RequestSyntax) **   <a name="securityagent-BatchGetThreats-request-threatIds"></a>
The list of threat identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetThreats_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notFound": [ "string" ],
   "threats": [
      {
         "anchor": {
            "id": "string",
            "kind": "string",
            "packageId": "string"
         },
         "comments": "string",
         "createdAt": "string",
         "createdBy": "string",
         "evidence": [
            {
               "packageId": "string",
               "path": "string"
            }
         ],
         "impactedAssets": [ "string" ],
         "impactedGoal": [ "string" ],
         "prerequisites": "string",
         "recommendation": "string",
         "severity": "string",
         "statement": "string",
         "status": "string",
         "stride": [ "string" ],
         "threatAction": "string",
         "threatId": "string",
         "threatImpact": "string",
         "threatJobId": "string",
         "threatSource": "string",
         "title": "string",
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetThreats_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notFound](#API_BatchGetThreats_ResponseSyntax) **   <a name="securityagent-BatchGetThreats-response-notFound"></a>
The list of threat identifiers that were not found.
Type: Array of strings

 ** [threats](#API_BatchGetThreats_ResponseSyntax) **   <a name="securityagent-BatchGetThreats-response-threats"></a>
The list of threats that were found.
Type: Array of [Threat](API_Threat.md) objects

## Errors
<a name="API_BatchGetThreats_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetThreats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetThreats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetThreats)
