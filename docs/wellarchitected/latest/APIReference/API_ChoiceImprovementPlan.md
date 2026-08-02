---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ChoiceImprovementPlan.html
---

# ChoiceImprovementPlan
<a name="API_ChoiceImprovementPlan"></a>

The choice level improvement plan.

This value is only applicable to custom lenses.

## Contents
<a name="API_ChoiceImprovementPlan_Contents"></a>

 ** ChoiceId **   <a name="wellarchitected-Type-ChoiceImprovementPlan-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** DisplayText **   <a name="wellarchitected-Type-ChoiceImprovementPlan-DisplayText"></a>
The display text for the improvement plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ImprovementPlanUrl **   <a name="wellarchitected-Type-ChoiceImprovementPlan-ImprovementPlanUrl"></a>
The improvement plan URL for a question in an AWS official lenses.
This value is only available if the question has been answered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ChoiceImprovementPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ChoiceImprovementPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ChoiceImprovementPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ChoiceImprovementPlan)
