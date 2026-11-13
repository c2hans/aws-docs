---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_TechniqueCoverage.html
---

# TechniqueCoverage
<a name="API_TechniqueCoverage"></a>

Contains information about the findings associated with a MITRE ATT&CK technique.

## Contents
<a name="API_TechniqueCoverage_Contents"></a>

 ** findingCount **   <a name="guardduty-Type-TechniqueCoverage-findingCount"></a>
The number of findings associated with the technique.
Type: Integer
Required: No

 ** findingTypes **   <a name="guardduty-Type-TechniqueCoverage-findingTypes"></a>
The finding types associated with the technique.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** technique **   <a name="guardduty-Type-TechniqueCoverage-technique"></a>
The technique.
Type: [ThreatReference](API_ThreatReference.md) object
Required: No

## See Also
<a name="API_TechniqueCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/TechniqueCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/TechniqueCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/TechniqueCoverage)
