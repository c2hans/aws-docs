---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTopicReviewedAnswer.html
---

# CreateTopicReviewedAnswer
<a name="API_CreateTopicReviewedAnswer"></a>

The definition for a `CreateTopicReviewedAnswer`.

## Contents
<a name="API_CreateTopicReviewedAnswer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnswerId **   <a name="QS-Type-CreateTopicReviewedAnswer-AnswerId"></a>
The answer ID for the `CreateTopicReviewedAnswer`.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: Yes

 ** DatasetArn **   <a name="QS-Type-CreateTopicReviewedAnswer-DatasetArn"></a>
The Dataset arn for the `CreateTopicReviewedAnswer`.
Type: String
Required: Yes

 ** Question **   <a name="QS-Type-CreateTopicReviewedAnswer-Question"></a>
The Question to be created.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Mir **   <a name="QS-Type-CreateTopicReviewedAnswer-Mir"></a>
The Mir for the `CreateTopicReviewedAnswer`.
Type: [TopicIR](API_TopicIR.md) object
Required: No

 ** PrimaryVisual **   <a name="QS-Type-CreateTopicReviewedAnswer-PrimaryVisual"></a>
The `PrimaryVisual` for the `CreateTopicReviewedAnswer`.
Type: [TopicVisual](API_TopicVisual.md) object
Required: No

 ** Template **   <a name="QS-Type-CreateTopicReviewedAnswer-Template"></a>
The template for the `CreateTopicReviewedAnswer`.
Type: [TopicTemplate](API_TopicTemplate.md) object
Required: No

## See Also
<a name="API_CreateTopicReviewedAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateTopicReviewedAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateTopicReviewedAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateTopicReviewedAnswer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
