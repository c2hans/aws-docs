---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Baseline.html
---

# Baseline
<a name="API_Baseline"></a>

Contains a comparison of findings against the normal behavior of an account.

## Contents
<a name="API_Baseline_Contents"></a>

 ** anomalousFindings **   <a name="guardduty-Type-Baseline-anomalousFindings"></a>
The finding types that deviate from normal behavior.
Type: Array of [FindingTypeClassification](API_FindingTypeClassification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** baselineFindings **   <a name="guardduty-Type-Baseline-baselineFindings"></a>
The finding types that are consistent with normal behavior.
Type: Array of [FindingTypeClassification](API_FindingTypeClassification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** totalFindings **   <a name="guardduty-Type-Baseline-totalFindings"></a>
The total number of findings.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Baseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Baseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Baseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Baseline)
