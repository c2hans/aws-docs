---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ThreatIntelligenceDetail.html
---

# ThreatIntelligenceDetail
<a name="API_ThreatIntelligenceDetail"></a>

An instance of a threat intelligence detail that constitutes evidence for the finding.

## Contents
<a name="API_ThreatIntelligenceDetail_Contents"></a>

 ** threatFileSha256 **   <a name="guardduty-Type-ThreatIntelligenceDetail-threatFileSha256"></a>
SHA256 of the file that generated the finding.
Type: String
Required: No

 ** threatListName **   <a name="guardduty-Type-ThreatIntelligenceDetail-threatListName"></a>
The name of the threat intelligence list that triggered the finding.
Type: String
Required: No

 ** threatNames **   <a name="guardduty-Type-ThreatIntelligenceDetail-threatNames"></a>
A list of names of the threats in the threat intelligence list that triggered the finding.
Type: Array of strings
Required: No

## See Also
<a name="API_ThreatIntelligenceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ThreatIntelligenceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ThreatIntelligenceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ThreatIntelligenceDetail)
