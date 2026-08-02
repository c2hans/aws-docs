---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatSummary.html
---

# ThreatSummary
<a name="API_ThreatSummary"></a>

Contains summary information about a threat.

## Contents
<a name="API_ThreatSummary_Contents"></a>

 ** createdAt **   <a name="securityagent-Type-ThreatSummary-createdAt"></a>
The date and time the threat was created, in UTC format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="securityagent-Type-ThreatSummary-createdBy"></a>
Who created this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`
Required: No

 ** severity **   <a name="securityagent-Type-ThreatSummary-severity"></a>
The severity level of the threat.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFO`
Required: No

 ** statement **   <a name="securityagent-Type-ThreatSummary-statement"></a>
The natural-language threat statement.
Type: String
Required: No

 ** status **   <a name="securityagent-Type-ThreatSummary-status"></a>
The current status of the threat.
Type: String
Valid Values: `OPEN | RESOLVED | DISMISSED`
Required: No

 ** stride **   <a name="securityagent-Type-ThreatSummary-stride"></a>
The STRIDE categories applicable to this threat.
Type: Array of strings
Valid Values: `SPOOFING | TAMPERING | REPUDIATION | INFORMATION_DISCLOSURE | DENIAL_OF_SERVICE | ELEVATION_OF_PRIVILEGE`
Required: No

 ** threatId **   <a name="securityagent-Type-ThreatSummary-threatId"></a>
The unique identifier of the threat.
Type: String
Required: No

 ** threatJobId **   <a name="securityagent-Type-ThreatSummary-threatJobId"></a>
The unique identifier of the threat model job that produced the threat.
Type: String
Required: No

 ** title **   <a name="securityagent-Type-ThreatSummary-title"></a>
A short title summarizing the threat.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatSummary-updatedAt"></a>
The date and time the threat was last updated, in UTC format.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="securityagent-Type-ThreatSummary-updatedBy"></a>
Who last updated this threat.
Type: String
Valid Values: `CUSTOMER | AGENT`
Required: No

## See Also
<a name="API_ThreatSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatSummary)
