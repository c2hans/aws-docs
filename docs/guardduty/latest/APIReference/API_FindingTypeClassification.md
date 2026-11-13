---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingTypeClassification.html
---

# FindingTypeClassification
<a name="API_FindingTypeClassification"></a>

Contains information about how a finding type compares with normal behavior.

## Contents
<a name="API_FindingTypeClassification_Contents"></a>

 ** classification **   <a name="guardduty-Type-FindingTypeClassification-classification"></a>
The classification of the finding type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** count **   <a name="guardduty-Type-FindingTypeClassification-count"></a>
The number of findings of this type.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** description **   <a name="guardduty-Type-FindingTypeClassification-description"></a>
A description of the classification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** findingType **   <a name="guardduty-Type-FindingTypeClassification-findingType"></a>
The finding type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** percentage **   <a name="guardduty-Type-FindingTypeClassification-percentage"></a>
The percentage of findings that are of this type, from 0 to 100.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_FindingTypeClassification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingTypeClassification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingTypeClassification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingTypeClassification)
