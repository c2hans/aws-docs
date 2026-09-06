---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicReviewedAnswer.html
---

# TopicReviewedAnswer
<a name="API_TopicReviewedAnswer"></a>

The deinition for a `TopicReviewedAnswer`.

## Contents
<a name="API_TopicReviewedAnswer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnswerId **   <a name="QS-Type-TopicReviewedAnswer-AnswerId"></a>
The answer ID of the reviewed answer.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: Yes

 ** DatasetArn **   <a name="QS-Type-TopicReviewedAnswer-DatasetArn"></a>
The Dataset ARN for the `TopicReviewedAnswer`.
Type: String
Required: Yes

 ** Question **   <a name="QS-Type-TopicReviewedAnswer-Question"></a>
The question for the `TopicReviewedAnswer`.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Arn **   <a name="QS-Type-TopicReviewedAnswer-Arn"></a>
The Amazon Resource Name (ARN) of the reviewed answer.
Type: String
Required: No

 ** Mir **   <a name="QS-Type-TopicReviewedAnswer-Mir"></a>
The mir for the `TopicReviewedAnswer`.
Type: [TopicIR](API_TopicIR.md) object
Required: No

 ** PrimaryVisual **   <a name="QS-Type-TopicReviewedAnswer-PrimaryVisual"></a>
The primary visual for the `TopicReviewedAnswer`.
Type: [TopicVisual](API_TopicVisual.md) object
Required: No

 ** Template **   <a name="QS-Type-TopicReviewedAnswer-Template"></a>
The template for the `TopicReviewedAnswer`.
Type: [TopicTemplate](API_TopicTemplate.md) object
Required: No

## See Also
<a name="API_TopicReviewedAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicReviewedAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicReviewedAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicReviewedAnswer)
