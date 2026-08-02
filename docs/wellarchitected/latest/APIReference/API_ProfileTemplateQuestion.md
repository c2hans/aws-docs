---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ProfileTemplateQuestion.html
---

# ProfileTemplateQuestion
<a name="API_ProfileTemplateQuestion"></a>

A profile template question.

## Contents
<a name="API_ProfileTemplateQuestion_Contents"></a>

 ** MaxSelectedChoices **   <a name="wellarchitected-Type-ProfileTemplateQuestion-MaxSelectedChoices"></a>
The maximum number of choices selected.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MinSelectedChoices **   <a name="wellarchitected-Type-ProfileTemplateQuestion-MinSelectedChoices"></a>
The minimum number of choices selected.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** QuestionChoices **   <a name="wellarchitected-Type-ProfileTemplateQuestion-QuestionChoices"></a>
The question choices.
Type: Array of [ProfileTemplateChoice](API_ProfileTemplateChoice.md) objects
Required: No

 ** QuestionDescription **   <a name="wellarchitected-Type-ProfileTemplateQuestion-QuestionDescription"></a>
The description of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-ProfileTemplateQuestion-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionTitle **   <a name="wellarchitected-Type-ProfileTemplateQuestion-QuestionTitle"></a>
The title of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_ProfileTemplateQuestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ProfileTemplateQuestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ProfileTemplateQuestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ProfileTemplateQuestion)
