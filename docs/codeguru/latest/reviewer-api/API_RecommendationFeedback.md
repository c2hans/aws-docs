---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedback.html
---

# RecommendationFeedback
<a name="API_RecommendationFeedback"></a>

Information about the recommendation feedback.

## Contents
<a name="API_RecommendationFeedback_Contents"></a>

 ** CodeReviewArn **   <a name="reviewer-Type-RecommendationFeedback-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: No

 ** CreatedTimeStamp **   <a name="reviewer-Type-RecommendationFeedback-CreatedTimeStamp"></a>
The time at which the feedback was created.
Type: Timestamp
Required: No

 ** LastUpdatedTimeStamp **   <a name="reviewer-Type-RecommendationFeedback-LastUpdatedTimeStamp"></a>
The time at which the feedback was last updated.
Type: Timestamp
Required: No

 ** Reactions **   <a name="reviewer-Type-RecommendationFeedback-Reactions"></a>
List for storing reactions. Reactions are utf-8 text code for emojis. You can send an empty list to clear off all your feedback.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ThumbsUp | ThumbsDown`
Required: No

 ** RecommendationId **   <a name="reviewer-Type-RecommendationFeedback-RecommendationId"></a>
The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** UserId **   <a name="reviewer-Type-RecommendationFeedback-UserId"></a>
The ID of the user that made the API call.
 The `UserId` is an IAM principal that can be specified as an AWS account ID or an Amazon Resource Name (ARN). For more information, see [ Specifying a Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) in the * AWS Identity and Access Management User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RecommendationFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RecommendationFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RecommendationFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RecommendationFeedback)
