---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityEvaluationRunAdditionalRunOptions.html
---

# DataQualityEvaluationRunAdditionalRunOptions
<a name="API_DataQualityEvaluationRunAdditionalRunOptions"></a>

Additional run options you can specify for an evaluation run.

## Contents
<a name="API_DataQualityEvaluationRunAdditionalRunOptions_Contents"></a>

 ** CloudWatchMetricsEnabled **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-CloudWatchMetricsEnabled"></a>
Whether or not to enable CloudWatch metrics.
Type: Boolean
Required: No

 ** CompositeRuleEvaluationMethod **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-CompositeRuleEvaluationMethod"></a>
Set the evaluation method for composite rules in the ruleset to ROW/COLUMN
Type: String
Valid Values: `COLUMN | ROW`
Required: No

 ** ResultsS3Prefix **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ResultsS3Prefix"></a>
Prefix for Amazon S3 to store results.
Type: String
Required: No

## See Also
<a name="API_DataQualityEvaluationRunAdditionalRunOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
