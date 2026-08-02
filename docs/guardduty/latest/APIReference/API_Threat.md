---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Threat.html
---

# Threat
<a name="API_Threat"></a>

Information about the detected threats associated with the generated finding.

## Contents
<a name="API_Threat_Contents"></a>

 ** count **   <a name="guardduty-Type-Threat-count"></a>
The number of occurrences of this specific threat detected during the scan.
Type: Long
Required: No

 ** hash **   <a name="guardduty-Type-Threat-hash"></a>
The hash identifier of the detected malware threat.
Type: String
Required: No

 ** itemDetails **   <a name="guardduty-Type-Threat-itemDetails"></a>
Detailed information about the detected malware threat.
Type: Array of [ItemDetails](API_ItemDetails.md) objects
Required: No

 ** itemPaths **   <a name="guardduty-Type-Threat-itemPaths"></a>
Information about the nested item path and hash of the protected resource.
Type: Array of [ItemPath](API_ItemPath.md) objects
Required: No

 ** name **   <a name="guardduty-Type-Threat-name"></a>
Name of the detected threat that caused GuardDuty to generate this finding.
Type: String
Required: No

 ** source **   <a name="guardduty-Type-Threat-source"></a>
Source of the threat that generated this finding.
Type: String
Required: No

## See Also
<a name="API_Threat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Threat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Threat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Threat)
