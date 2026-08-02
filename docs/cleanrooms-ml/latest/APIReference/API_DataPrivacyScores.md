---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DataPrivacyScores.html
---

# DataPrivacyScores
<a name="API_DataPrivacyScores"></a>

Privacy evaluation scores that measure the privacy characteristics of the generated synthetic data, including assessments of potential privacy risks such as membership inference attacks.

## Contents
<a name="API_DataPrivacyScores_Contents"></a>

 ** membershipInferenceAttackScores **   <a name="API-Type-DataPrivacyScores-membershipInferenceAttackScores"></a>
Scores that evaluate the vulnerability of the synthetic data to membership inference attacks, which attempt to determine whether a specific individual was a member of the original dataset.
Type: Array of [MembershipInferenceAttackScore](API_MembershipInferenceAttackScore.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_DataPrivacyScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/DataPrivacyScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/DataPrivacyScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/DataPrivacyScores)
