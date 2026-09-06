---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotRecommendationSummary.html
---

# BotRecommendationSummary
<a name="API_BotRecommendationSummary"></a>

A summary of the bot recommendation.

## Contents
<a name="API_BotRecommendationSummary_Contents"></a>

 ** botRecommendationId **   <a name="lexv2-Type-BotRecommendationSummary-botRecommendationId"></a>
The unique identifier of the bot recommendation to be updated.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** botRecommendationStatus **   <a name="lexv2-Type-BotRecommendationSummary-botRecommendationStatus"></a>
The status of the bot recommendation.
If the status is Failed, then the reasons for the failure are listed in the failureReasons field.
Type: String
Valid Values: `Processing | Deleting | Deleted | Downloading | Updating | Available | Failed | Stopping | Stopped`
Required: Yes

 ** creationDateTime **   <a name="lexv2-Type-BotRecommendationSummary-creationDateTime"></a>
A timestamp of the date and time that the bot recommendation was created.
Type: Timestamp
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-BotRecommendationSummary-lastUpdatedDateTime"></a>
A timestamp of the date and time that the bot recommendation was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_BotRecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotRecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotRecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotRecommendationSummary)
