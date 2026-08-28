---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html
---

# RecommendationFeedbackSummary
<a name="API_RecommendationFeedbackSummary"></a>

Information about recommendation feedback summaries.

## Contents
<a name="API_RecommendationFeedbackSummary_Contents"></a>

 ** Reactions **   <a name="reviewer-Type-RecommendationFeedbackSummary-Reactions"></a>
List for storing reactions. Reactions are utf-8 text code for emojis.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ThumbsUp | ThumbsDown`
Required: No

 ** RecommendationId **   <a name="reviewer-Type-RecommendationFeedbackSummary-RecommendationId"></a>
The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** UserId **   <a name="reviewer-Type-RecommendationFeedbackSummary-UserId"></a>
The ID of the user that gave the feedback.
 The `UserId` is an IAM principal that can be specified as an AWS account ID or an Amazon Resource Name (ARN). For more information, see [ Specifying a Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) in the * AWS Identity and Access Management User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RecommendationFeedbackSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RecommendationFeedbackSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RecommendationFeedbackSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RecommendationFeedbackSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
