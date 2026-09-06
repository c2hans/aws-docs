---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Threat.html
---

# Threat
<a name="API_Threat"></a>

Represents a threat identified during threat modeling.

## Contents
<a name="API_Threat_Contents"></a>

 ** anchor **   <a name="securityagent-Type-Threat-anchor"></a>
The DFD element this threat is anchored to.
Type: [ThreatAnchorShape](API_ThreatAnchorShape.md) object
Required: No

 ** comments **   <a name="securityagent-Type-Threat-comments"></a>
Optional customer comment on the threat.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-Threat-createdAt"></a>
The date and time the threat was created, in UTC format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="securityagent-Type-Threat-createdBy"></a>
Who created this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`
Required: No

 ** evidence **   <a name="securityagent-Type-Threat-evidence"></a>
The source code files supporting the threat.
Type: Array of [ThreatEvidenceShape](API_ThreatEvidenceShape.md) objects
Required: No

 ** impactedAssets **   <a name="securityagent-Type-Threat-impactedAssets"></a>
The specific assets affected by the threat.
Type: Array of strings
Required: No

 ** impactedGoal **   <a name="securityagent-Type-Threat-impactedGoal"></a>
The security goals affected by the threat.
Type: Array of strings
Required: No

 ** prerequisites **   <a name="securityagent-Type-Threat-prerequisites"></a>
The conditions required for the threat to be exploitable.
Type: String
Required: No

 ** recommendation **   <a name="securityagent-Type-Threat-recommendation"></a>
The recommended mitigation guidance for this threat.
Type: String
Required: No

 ** severity **   <a name="securityagent-Type-Threat-severity"></a>
The severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`
Required: No

 ** statement **   <a name="securityagent-Type-Threat-statement"></a>
The natural-language threat statement.
Type: String
Required: No

 ** status **   <a name="securityagent-Type-Threat-status"></a>
The current status of the threat.
Type: String
Valid Values: `OPEN | RESOLVED | DISMISSED`
Required: No

 ** stride **   <a name="securityagent-Type-Threat-stride"></a>
The STRIDE categories applicable to this threat.
Type: Array of strings
Valid Values: `SPOOFING | TAMPERING | REPUDIATION | INFORMATION_DISCLOSURE | DENIAL_OF_SERVICE | ELEVATION_OF_PRIVILEGE`
Required: No

 ** threatAction **   <a name="securityagent-Type-Threat-threatAction"></a>
What the threat source can do.
Type: String
Required: No

 ** threatId **   <a name="securityagent-Type-Threat-threatId"></a>
The unique identifier of the threat.
Type: String
Required: No

 ** threatImpact **   <a name="securityagent-Type-Threat-threatImpact"></a>
The direct consequence of the threat action.
Type: String
Required: No

 ** threatJobId **   <a name="securityagent-Type-Threat-threatJobId"></a>
The unique identifier of the threat model job that produced the threat.
Type: String
Required: No

 ** threatSource **   <a name="securityagent-Type-Threat-threatSource"></a>
The actor or origin of the threat.
Type: String
Required: No

 ** title **   <a name="securityagent-Type-Threat-title"></a>
A short title summarizing the threat.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-Threat-updatedAt"></a>
The date and time the threat was last updated, in UTC format.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="securityagent-Type-Threat-updatedBy"></a>
Who last updated this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`
Required: No

## See Also
<a name="API_Threat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Threat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Threat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Threat)
