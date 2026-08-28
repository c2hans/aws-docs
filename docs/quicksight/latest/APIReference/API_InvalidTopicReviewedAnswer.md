---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InvalidTopicReviewedAnswer.html
---

# InvalidTopicReviewedAnswer
<a name="API_InvalidTopicReviewedAnswer"></a>

The definition for a `InvalidTopicReviewedAnswer`.

## Contents
<a name="API_InvalidTopicReviewedAnswer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnswerId **   <a name="QS-Type-InvalidTopicReviewedAnswer-AnswerId"></a>
The answer ID for the `InvalidTopicReviewedAnswer`.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: No

 ** Error **   <a name="QS-Type-InvalidTopicReviewedAnswer-Error"></a>
The error that is returned for the `InvalidTopicReviewedAnswer`.
Type: String
Valid Values: `INTERNAL_ERROR | MISSING_ANSWER | DATASET_DOES_NOT_EXIST | INVALID_DATASET_ARN | DUPLICATED_ANSWER | INVALID_DATA | MISSING_REQUIRED_FIELDS`
Required: No

## See Also
<a name="API_InvalidTopicReviewedAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InvalidTopicReviewedAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InvalidTopicReviewedAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InvalidTopicReviewedAnswer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
