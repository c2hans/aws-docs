---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingTypeDocumentation.html
---

# FindingTypeDocumentation
<a name="API_FindingTypeDocumentation"></a>

Contains information about a finding type from the GuardDuty documentation.

## Contents
<a name="API_FindingTypeDocumentation_Contents"></a>

 ** description **   <a name="guardduty-Type-FindingTypeDocumentation-description"></a>
A short description of the finding type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** feature **   <a name="guardduty-Type-FindingTypeDocumentation-feature"></a>
The label that the documentation uses for the GuardDuty capability associated with the finding type. This value isn't a detector feature name.
Type: String
Required: No

 ** fullDescription **   <a name="guardduty-Type-FindingTypeDocumentation-fullDescription"></a>
The full description of the finding type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** learnMoreLinks **   <a name="guardduty-Type-FindingTypeDocumentation-learnMoreLinks"></a>
Links to more information about the finding type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** remediation **   <a name="guardduty-Type-FindingTypeDocumentation-remediation"></a>
The recommended steps to remediate the finding type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** severity **   <a name="guardduty-Type-FindingTypeDocumentation-severity"></a>
The severity of the finding type, as stated in the documentation.
Type: String
Required: No

## See Also
<a name="API_FindingTypeDocumentation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingTypeDocumentation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingTypeDocumentation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingTypeDocumentation)
