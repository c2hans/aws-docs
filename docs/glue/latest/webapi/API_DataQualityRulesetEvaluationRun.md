---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRulesetEvaluationRun.html
---

# DataQualityRulesetEvaluationRun
<a name="API_DataQualityRulesetEvaluationRun"></a>

The details of a data quality ruleset evaluation run.

## Contents
<a name="API_DataQualityRulesetEvaluationRun_Contents"></a>

 ** AdditionalDataSources **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-AdditionalDataSources"></a>
A map of reference strings to additional data sources you can specify for an evaluation run.
Type: String to [DataSource](API_DataSource.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** AdditionalRunOptions **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-AdditionalRunOptions"></a>
Additional run options you can specify for an evaluation run.
Type: [DataQualityEvaluationRunAdditionalRunOptions](API_DataQualityEvaluationRunAdditionalRunOptions.md) object
Required: No

 ** CompletedOn **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-CompletedOn"></a>
The date and time when this run was completed.
Type: Timestamp
Required: No

 ** DataSource **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-DataSource"></a>
A data source (an AWS Glue table) for which you want data quality results.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** ErrorString **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-ErrorString"></a>
The error strings that are associated with the run.
Type: String
Required: No

 ** ExecutionTime **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-ExecutionTime"></a>
The amount of time (in seconds) that the run consumed resources.
Type: Integer
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-LastModifiedOn"></a>
A timestamp. The last point in time when this run was modified.
Type: Timestamp
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-NumberOfWorkers"></a>
The number of `G.1X` workers to be used in the run. The default is 5.
Type: Integer
Required: No

 ** ResultIds **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-ResultIds"></a>
A list of result IDs for the data quality results for the run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Role **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-Role"></a>
An IAM role supplied to encrypt the results of the run.
Type: String
Required: No

 ** RulesetNames **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-RulesetNames"></a>
A list of ruleset names for the run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RunId **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-StartedOn"></a>
The date and time when this run started.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-Status"></a>
The status for this run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

 ** Timeout **   <a name="Glue-Type-DataQualityRulesetEvaluationRun-Timeout"></a>
The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_DataQualityRulesetEvaluationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRulesetEvaluationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRulesetEvaluationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRulesetEvaluationRun)
