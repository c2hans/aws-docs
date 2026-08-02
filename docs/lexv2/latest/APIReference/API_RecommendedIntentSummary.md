---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_RecommendedIntentSummary.html
---

# RecommendedIntentSummary
<a name="API_RecommendedIntentSummary"></a>

An object that contains a summary of a recommended intent.

## Contents
<a name="API_RecommendedIntentSummary_Contents"></a>

 ** intentId **   <a name="lexv2-Type-RecommendedIntentSummary-intentId"></a>
The unique identifier of a recommended intent associated with the bot recommendation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** intentName **   <a name="lexv2-Type-RecommendedIntentSummary-intentName"></a>
The name of a recommended intent associated with the bot recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** sampleUtterancesCount **   <a name="lexv2-Type-RecommendedIntentSummary-sampleUtterancesCount"></a>
The count of sample utterances of a recommended intent that is associated with a bot recommendation.
Type: Integer
Required: No

## See Also
<a name="API_RecommendedIntentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/RecommendedIntentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/RecommendedIntentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/RecommendedIntentSummary)
