---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TrainingMetrics.html
---

# TrainingMetrics
<a name="API_connect-customer-profiles_TrainingMetrics"></a>

Contains metrics and performance indicators from the training of a recommender model.

## Contents
<a name="API_connect-customer-profiles_TrainingMetrics_Contents"></a>

 ** Metrics **   <a name="connect-Type-connect-customer-profiles_TrainingMetrics-Metrics"></a>
A collection of performance metrics and statistics from the training process.
Type: String to double map
Valid Keys: `hit | coverage | recall | popularity | freshness | similarity | mean_reciprocal_rank_at_25 | normalized_discounted_cumulative_gain_at_5 | normalized_discounted_cumulative_gain_at_10 | normalized_discounted_cumulative_gain_at_25 | precision_at_5 | precision_at_10 | precision_at_25`
Required: No

 ** RecommenderVersionName **   <a name="connect-Type-connect-customer-profiles_TrainingMetrics-RecommenderVersionName"></a>
The name of the recommender version that produced these training metrics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+/\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z`
Required: No

 ** Time **   <a name="connect-Type-connect-customer-profiles_TrainingMetrics-Time"></a>
The timestamp when these training metrics were recorded.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-customer-profiles_TrainingMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/TrainingMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/TrainingMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/TrainingMetrics)
