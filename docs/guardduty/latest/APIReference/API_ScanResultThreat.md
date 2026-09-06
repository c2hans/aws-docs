---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanResultThreat.html
---

# ScanResultThreat
<a name="API_ScanResultThreat"></a>

Contains information about a specific threat that was detected during the malware scan.

## Contents
<a name="API_ScanResultThreat_Contents"></a>

 ** count **   <a name="guardduty-Type-ScanResultThreat-count"></a>
The number of instances of this threat that were detected.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** hash **   <a name="guardduty-Type-ScanResultThreat-hash"></a>
The hash value associated with the detected threat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** itemDetails **   <a name="guardduty-Type-ScanResultThreat-itemDetails"></a>
Additional information about where this threat was detected.
Type: Array of [ItemDetails](API_ItemDetails.md) objects
Required: No

 ** name **   <a name="guardduty-Type-ScanResultThreat-name"></a>
The name of the detected threat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** source **   <a name="guardduty-Type-ScanResultThreat-source"></a>
The source that detected this threat.
Type: String
Valid Values: `AMAZON | BITDEFENDER`
Required: No

## See Also
<a name="API_ScanResultThreat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanResultThreat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanResultThreat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanResultThreat)
