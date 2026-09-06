---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_RecommenderConfig.html
---

# RecommenderConfig
<a name="API_connect-customer-profiles_RecommenderConfig"></a>

Configuration settings that define the behavior and parameters of a recommender.

## Contents
<a name="API_connect-customer-profiles_RecommenderConfig_Contents"></a>

 ** DiversityConfig **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-DiversityConfig"></a>
Configuration for diversity-aware recommendations. When set, the recommender applies diversity constraints defined per item column to reduce over-concentration of similar items in the results.
Type: [DiversityConfig](API_connect-customer-profiles_DiversityConfig.md) object
Required: No

 ** EventsConfig **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-EventsConfig"></a>
Configuration settings for how the recommender processes and uses events.
Type: [EventsConfig](API_connect-customer-profiles_EventsConfig.md) object
Required: No

 ** ExcludedColumns **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-ExcludedColumns"></a>
A map of dataset type to a list of column names to exclude from training. The `_webAnalytics` and `_catalogItem` keys are supported. The column names must be valid columns defined in the recommender schema. All columns in the schema except the listed columns will be used for training. The following columns are mandatory and cannot be excluded: `Item.Id`, `EventTimestamp`, and `EventType` for `_webAnalytics`; `Id` for `_catalogItem`. Mutually exclusive with IncludedColumns — both cannot be specified in the same request.
Type: String to array of strings map
Map Entries: Maximum number of 2 items.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** IncludedColumns **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-IncludedColumns"></a>
A map of dataset type to a list of column names to train on. The `_webAnalytics` and `_catalogItem` keys are supported. The column names must be a subset of the columns defined in the recommender schema. If not specified, all columns in the schema are used for training. The following columns are always included in training and do not need to be specified: `Item.Id`, `EventTimestamp`, and `EventType` for `_webAnalytics`; `Id` for `_catalogItem`. Mutually exclusive with ExcludedColumns — both cannot be specified in the same request.
Type: String to array of strings map
Map Entries: Maximum number of 2 items.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** InferenceConfig **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-InferenceConfig"></a>
Configuration settings for how the recommender handles inference requests.
Type: [InferenceConfig](API_connect-customer-profiles_InferenceConfig.md) object
Required: No

 ** TrainingFrequency **   <a name="connect-Type-connect-customer-profiles_RecommenderConfig-TrainingFrequency"></a>
How often the recommender should retrain its model with new data. If set to 0, automatic retraining will not be enabled.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 30.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderConfig)
