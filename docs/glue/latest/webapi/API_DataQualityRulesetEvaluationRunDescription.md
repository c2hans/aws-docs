---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRulesetEvaluationRunDescription.html
---

# DataQualityRulesetEvaluationRunDescription
<a name="API_DataQualityRulesetEvaluationRunDescription"></a>

Describes the result of a data quality ruleset evaluation run.

## Contents
<a name="API_DataQualityRulesetEvaluationRunDescription_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityRulesetEvaluationRunDescription-DataSource"></a>
The data source (an AWS Glue table) associated with the run.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** RunId **   <a name="Glue-Type-DataQualityRulesetEvaluationRunDescription-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-DataQualityRulesetEvaluationRunDescription-StartedOn"></a>
The date and time when the run started.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-DataQualityRulesetEvaluationRunDescription-Status"></a>
The status for this run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

## See Also
<a name="API_DataQualityRulesetEvaluationRunDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRulesetEvaluationRunDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRulesetEvaluationRunDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRulesetEvaluationRunDescription)
