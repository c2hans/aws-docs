---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateThreat.html
---

# UpdateThreat
<a name="API_UpdateThreat"></a>

Updates a threat.

## Request Syntax
<a name="API_UpdateThreat_RequestSyntax"></a>

```
POST /UpdateThreat HTTP/1.1
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
   "status": "{{string}}",
   "threatAction": "{{string}}",
   "threatId": "{{string}}",
   "threatImpact": "{{string}}",
   "threatSource": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateThreat_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateThreat_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [anchor](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-anchor"></a>
The updated DFD element this threat is anchored to.
Type: [ThreatAnchorShape](API_ThreatAnchorShape.md) object
Required: No

 ** [comments](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-comments"></a>
Optional customer comment.
Type: String
Required: No

 ** [evidence](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-evidence"></a>
The updated source code files supporting the threat.
Type: Array of [ThreatEvidenceShape](API_ThreatEvidenceShape.md) objects
Required: No

 ** [impactedAssets](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-impactedAssets"></a>
The updated list of specific assets affected by the threat.
Type: Array of strings
Required: No

 ** [impactedGoal](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-impactedGoal"></a>
The updated security goals affected by the threat.
Type: Array of strings
Required: No

 ** [prerequisites](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-prerequisites"></a>
The updated conditions required for the threat to be exploitable.
Type: String
Required: No

 ** [recommendation](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-recommendation"></a>
The updated recommended mitigation guidance for this threat.
Type: String
Required: No

 ** [severity](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-severity"></a>
The updated severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`
Required: No

 ** [statement](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-statement"></a>
The updated natural-language threat statement.
Type: String
Required: No

 ** [status](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-status"></a>
The updated status of the threat.
Type: String
Valid Values: `OPEN | RESOLVED | DISMISSED`
Required: No

 ** [threatAction](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-threatAction"></a>
The updated description of what the threat source can do.
Type: String
Required: No

 ** [threatId](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-threatId"></a>
The unique identifier of the threat to update.
Type: String
Required: Yes

 ** [threatImpact](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-threatImpact"></a>
The updated direct consequence of the threat action.
Type: String
Required: No

 ** [threatSource](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-threatSource"></a>
The updated actor or origin of the threat.
Type: String
Required: No

 ** [title](#API_UpdateThreat_RequestSyntax) **   <a name="securityagent-UpdateThreat-request-title"></a>
A short title summarizing the threat.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateThreat_ResponseSyntax"></a>

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
<a name="API_UpdateThreat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anchor](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-anchor"></a>
The DFD element this threat is anchored to.
Type: [ThreatAnchorShape](API_ThreatAnchorShape.md) object

 ** [comments](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-comments"></a>
Optional customer comment on the threat.
Type: String

 ** [createdAt](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-createdAt"></a>
The date and time the threat was created, in UTC format.
Type: Timestamp

 ** [createdBy](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-createdBy"></a>
Who created this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`

 ** [evidence](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-evidence"></a>
The source code files supporting the threat.
Type: Array of [ThreatEvidenceShape](API_ThreatEvidenceShape.md) objects

 ** [impactedAssets](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-impactedAssets"></a>
The specific assets affected by the threat.
Type: Array of strings

 ** [impactedGoal](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-impactedGoal"></a>
The security goals affected by the threat.
Type: Array of strings

 ** [prerequisites](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-prerequisites"></a>
The conditions required for the threat to be exploitable.
Type: String

 ** [recommendation](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-recommendation"></a>
The recommended mitigation guidance for this threat.
Type: String

 ** [severity](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-severity"></a>
The severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`

 ** [statement](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-statement"></a>
The natural-language threat statement.
Type: String

 ** [status](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-status"></a>
The current status of the threat.
Type: String
Valid Values: `OPEN | RESOLVED | DISMISSED`

 ** [stride](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-stride"></a>
The STRIDE categories applicable to this threat.
Type: Array of strings
Valid Values: `SPOOFING | TAMPERING | REPUDIATION | INFORMATION_DISCLOSURE | DENIAL_OF_SERVICE | ELEVATION_OF_PRIVILEGE`

 ** [threatAction](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-threatAction"></a>
What the threat source can do.
Type: String

 ** [threatId](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-threatId"></a>
The unique identifier of the threat.
Type: String

 ** [threatImpact](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-threatImpact"></a>
The direct consequence of the threat action.
Type: String

 ** [threatJobId](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-threatJobId"></a>
The unique identifier of the threat model job the threat belongs to.
Type: String

 ** [threatSource](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-threatSource"></a>
The actor or origin of the threat.
Type: String

 ** [title](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-title"></a>
A short title summarizing the threat.
Type: String

 ** [updatedAt](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-updatedAt"></a>
The date and time the threat was last updated, in UTC format.
Type: Timestamp

 ** [updatedBy](#API_UpdateThreat_ResponseSyntax) **   <a name="securityagent-UpdateThreat-response-updatedBy"></a>
Who last updated this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`

## Errors
<a name="API_UpdateThreat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateThreat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateThreat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateThreat)
