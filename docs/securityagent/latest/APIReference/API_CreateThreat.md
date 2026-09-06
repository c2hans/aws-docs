---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateThreat.html
---

# CreateThreat
<a name="API_CreateThreat"></a>

Creates a new threat under a threat model job.

## Request Syntax
<a name="API_CreateThreat_RequestSyntax"></a>

```
POST /CreateThreat HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "anchor": {
      "id": "{{string}}",
      "kind": "{{string}}",
      "packageId": "{{string}}"
   },
   "comments": "{{string}}",
   "evidence": [
      {
         "packageId": "{{string}}",
         "path": "{{string}}"
      }
   ],
   "impactedAssets": [ "{{string}}" ],
   "impactedGoal": [ "{{string}}" ],
   "prerequisites": "{{string}}",
   "recommendation": "{{string}}",
   "severity": "{{string}}",
   "statement": "{{string}}",
   "stride": [ "{{string}}" ],
   "threatAction": "{{string}}",
   "threatImpact": "{{string}}",
   "threatJobId": "{{string}}",
   "threatSource": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateThreat_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateThreat_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [anchor](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-anchor"></a>
The DFD element this threat is anchored to.
Type: [ThreatAnchorShape](API_ThreatAnchorShape.md) object
Required: No

 ** [comments](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-comments"></a>
Optional customer comment on the threat.
Type: String
Required: No

 ** [evidence](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-evidence"></a>
The source code files supporting the threat.
Type: Array of [ThreatEvidenceShape](API_ThreatEvidenceShape.md) objects
Required: No

 ** [impactedAssets](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-impactedAssets"></a>
The specific assets affected by the threat.
Type: Array of strings
Required: No

 ** [impactedGoal](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-impactedGoal"></a>
The security goals affected by the threat.
Type: Array of strings
Required: No

 ** [prerequisites](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-prerequisites"></a>
The conditions required for the threat to be exploitable.
Type: String
Required: No

 ** [recommendation](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-recommendation"></a>
The recommended mitigation guidance for this threat.
Type: String
Required: No

 ** [severity](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-severity"></a>
The severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`
Required: No

 ** [statement](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-statement"></a>
The natural-language threat statement.
Type: String
Required: No

 ** [stride](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-stride"></a>
The STRIDE categories applicable to this threat.
Type: Array of strings
Valid Values: `SPOOFING | TAMPERING | REPUDIATION | INFORMATION_DISCLOSURE | DENIAL_OF_SERVICE | ELEVATION_OF_PRIVILEGE`
Required: No

 ** [threatAction](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-threatAction"></a>
What the threat source can do.
Type: String
Required: No

 ** [threatImpact](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-threatImpact"></a>
The direct consequence of the threat action.
Type: String
Required: No

 ** [threatJobId](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-threatJobId"></a>
The unique identifier of the threat model job the threat belongs to.
Type: String
Required: Yes

 ** [threatSource](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-threatSource"></a>
The actor or origin of the threat.
Type: String
Required: No

 ** [title](#API_CreateThreat_RequestSyntax) **   <a name="securityagent-CreateThreat-request-title"></a>
A short title summarizing the threat.
Type: String
Required: No

## Response Syntax
<a name="API_CreateThreat_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_CreateThreat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anchor](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-anchor"></a>
The DFD element this threat is anchored to.
Type: [ThreatAnchorShape](API_ThreatAnchorShape.md) object

 ** [comments](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-comments"></a>
Optional customer comment on the threat.
Type: String

 ** [createdAt](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-createdAt"></a>
The date and time the threat was created, in UTC format.
Type: Timestamp

 ** [createdBy](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-createdBy"></a>
Who created this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`

 ** [evidence](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-evidence"></a>
The source code files supporting the threat.
Type: Array of [ThreatEvidenceShape](API_ThreatEvidenceShape.md) objects

 ** [impactedAssets](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-impactedAssets"></a>
The specific assets affected by the threat.
Type: Array of strings

 ** [impactedGoal](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-impactedGoal"></a>
The security goals affected by the threat.
Type: Array of strings

 ** [prerequisites](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-prerequisites"></a>
The conditions required for the threat to be exploitable.
Type: String

 ** [recommendation](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-recommendation"></a>
The recommended mitigation guidance for this threat.
Type: String

 ** [severity](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-severity"></a>
The severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`

 ** [statement](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-statement"></a>
The natural-language threat statement.
Type: String

 ** [status](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-status"></a>
The current status of the threat.
Type: String
Valid Values: `OPEN | RESOLVED | DISMISSED`

 ** [stride](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-stride"></a>
The STRIDE categories applicable to this threat.
Type: Array of strings
Valid Values: `SPOOFING | TAMPERING | REPUDIATION | INFORMATION_DISCLOSURE | DENIAL_OF_SERVICE | ELEVATION_OF_PRIVILEGE`

 ** [threatAction](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-threatAction"></a>
What the threat source can do.
Type: String

 ** [threatId](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-threatId"></a>
The unique identifier of the created threat.
Type: String

 ** [threatImpact](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-threatImpact"></a>
The direct consequence of the threat action.
Type: String

 ** [threatJobId](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-threatJobId"></a>
The unique identifier of the threat model job the threat belongs to.
Type: String

 ** [threatSource](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-threatSource"></a>
The actor or origin of the threat.
Type: String

 ** [title](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-title"></a>
A short title summarizing the threat.
Type: String

 ** [updatedAt](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-updatedAt"></a>
The date and time the threat was last updated, in UTC format.
Type: Timestamp

 ** [updatedBy](#API_CreateThreat_ResponseSyntax) **   <a name="securityagent-CreateThreat-response-updatedBy"></a>
Who last updated this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`

## Errors
<a name="API_CreateThreat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateThreat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateThreat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateThreat)
