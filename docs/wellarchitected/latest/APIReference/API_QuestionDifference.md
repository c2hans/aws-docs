---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_QuestionDifference.html
---

# QuestionDifference
<a name="API_QuestionDifference"></a>

A question difference return object.

## Contents
<a name="API_QuestionDifference_Contents"></a>

 ** DifferenceStatus **   <a name="wellarchitected-Type-QuestionDifference-DifferenceStatus"></a>
Indicates the type of change to the question.
Type: String
Valid Values: `UPDATED | NEW | DELETED`
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-QuestionDifference-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionTitle **   <a name="wellarchitected-Type-QuestionDifference-QuestionTitle"></a>
The title of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_QuestionDifference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/QuestionDifference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/QuestionDifference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/QuestionDifference)
