---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_TypeDistribution.html
---

# TypeDistribution
<a name="API_TypeDistribution"></a>

Contains the number and percentage of findings of a finding type.

## Contents
<a name="API_TypeDistribution_Contents"></a>

 ** count **   <a name="guardduty-Type-TypeDistribution-count"></a>
The number of findings of this type.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** dominantSeverity **   <a name="guardduty-Type-TypeDistribution-dominantSeverity"></a>
The most common severity among findings of this type.
Type: String
Required: No

 ** findingType **   <a name="guardduty-Type-TypeDistribution-findingType"></a>
The finding type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** percentage **   <a name="guardduty-Type-TypeDistribution-percentage"></a>
The percentage of findings that are of this type, from 0 to 100.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_TypeDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/TypeDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/TypeDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/TypeDistribution)
