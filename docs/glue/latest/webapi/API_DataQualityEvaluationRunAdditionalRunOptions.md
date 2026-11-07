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

 ** CustomLogGroupPrefix **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-CustomLogGroupPrefix"></a>
A custom prefix for the CloudWatch log group names. When specified, evaluation run logs are written to `<CustomLogGroupPrefix>/error` and `<CustomLogGroupPrefix>/output` instead of the default `/aws-glue/data-quality/error` and `/aws-glue/data-quality/output` log groups.
Type: String
Required: No

 ** DataQualityRuleResults **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-DataQualityRuleResults"></a>
The configuration for writing rule results to a AWS Glue Data Catalog table.
Type: [DataQualityRuleResultsOptions](API_DataQualityRuleResultsOptions.md) object
Required: No

 ** ObservationMode **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ObservationMode"></a>
The observation mode for the evaluation run. Specifies how anomaly detection bounds are calculated.
Type: String
Valid Values: `SCHEDULED | FIXED`
Required: No

 ** ObservationResults **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ObservationResults"></a>
The configuration for writing observation results to a AWS Glue Data Catalog table.
Type: [ObservationResultsOptions](API_ObservationResultsOptions.md) object
Required: No

 ** ObservationScope **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ObservationScope"></a>
The scope of the observation for the evaluation run. Specifies whether anomaly detection is enabled or disabled.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** ProfilingResults **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ProfilingResults"></a>
The configuration for writing profiling results to a AWS Glue Data Catalog table.
Type: [ProfilingResultsOptions](API_ProfilingResultsOptions.md) object
Required: No

 ** ResultsS3Prefix **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-ResultsS3Prefix"></a>
Prefix for Amazon S3 to store results.
Type: String
Required: No

 ** RowLevelResults **   <a name="Glue-Type-DataQualityEvaluationRunAdditionalRunOptions-RowLevelResults"></a>
The configuration for writing row-level evaluation results to a AWS Glue Data Catalog table.
Type: [RowLevelResultsOptions](API_RowLevelResultsOptions.md) object
Required: No

## See Also
<a name="API_DataQualityEvaluationRunAdditionalRunOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityEvaluationRunAdditionalRunOptions)
