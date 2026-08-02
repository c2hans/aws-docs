---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EvaluateDataQualityMultiFrame.html
---

# EvaluateDataQualityMultiFrame
<a name="API_EvaluateDataQualityMultiFrame"></a>

Specifies your data quality evaluation criteria.

## Contents
<a name="API_EvaluateDataQualityMultiFrame_Contents"></a>

 ** Inputs **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-Inputs"></a>
The inputs of your data quality evaluation. The first input in this list is the primary data source.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-Name"></a>
The name of the data quality evaluation.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Ruleset **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-Ruleset"></a>
The ruleset for your data quality evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `([\u0020-\u007E\r\s\n])*`
Required: Yes

 ** AdditionalDataSources **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-AdditionalDataSources"></a>
The aliases of all data sources except primary.
Type: String to string map
Key Pattern: `([^\r\n])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AdditionalOptions **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-AdditionalOptions"></a>
Options to configure runtime behavior of the transform.
Type: String to string map
Valid Keys: `performanceTuning.caching | observations.scope | compositeRuleEvaluation.method`
Required: No

 ** PublishingOptions **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-PublishingOptions"></a>
Options to configure how your results are published.
Type: [DQResultsPublishingOptions](API_DQResultsPublishingOptions.md) object
Required: No

 ** StopJobOnFailureOptions **   <a name="Glue-Type-EvaluateDataQualityMultiFrame-StopJobOnFailureOptions"></a>
Options to configure how your job will stop if your data quality evaluation fails.
Type: [DQStopJobOnFailureOptions](API_DQStopJobOnFailureOptions.md) object
Required: No

## See Also
<a name="API_EvaluateDataQualityMultiFrame_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EvaluateDataQualityMultiFrame)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EvaluateDataQualityMultiFrame)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EvaluateDataQualityMultiFrame)
