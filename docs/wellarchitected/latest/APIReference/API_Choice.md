---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Choice.html
---

# Choice
<a name="API_Choice"></a>

A choice available to answer question.

## Contents
<a name="API_Choice_Contents"></a>

 ** AdditionalResources **   <a name="wellarchitected-Type-Choice-AdditionalResources"></a>
The additional resources for a choice in a custom lens.
A choice can have up to two additional resources: one of type `HELPFUL_RESOURCE`, one of type `IMPROVEMENT_PLAN`, or both.
Type: Array of [AdditionalResources](API_AdditionalResources.md) objects
Required: No

 ** ChoiceId **   <a name="wellarchitected-Type-Choice-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Description **   <a name="wellarchitected-Type-Choice-Description"></a>
The description of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** HelpfulResource **   <a name="wellarchitected-Type-Choice-HelpfulResource"></a>
The helpful resource (both text and URL) for a particular choice.
This field only applies to custom lenses. Each choice can have only one helpful resource.
Type: [ChoiceContent](API_ChoiceContent.md) object
Required: No

 ** ImprovementPlan **   <a name="wellarchitected-Type-Choice-ImprovementPlan"></a>
The improvement plan (both text and URL) for a particular choice.
This field only applies to custom lenses. Each choice can have only one improvement plan.
Type: [ChoiceContent](API_ChoiceContent.md) object
Required: No

 ** Title **   <a name="wellarchitected-Type-Choice-Title"></a>
The title of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_Choice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Choice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Choice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Choice)
