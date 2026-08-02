---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRuleRecommendationRunDescription.html
---

# DataQualityRuleRecommendationRunDescription
<a name="API_DataQualityRuleRecommendationRunDescription"></a>

Describes the result of a data quality rule recommendation run.

## Contents
<a name="API_DataQualityRuleRecommendationRunDescription_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityRuleRecommendationRunDescription-DataSource"></a>
The data source (AWS Glue table) associated with the recommendation run.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** RunId **   <a name="Glue-Type-DataQualityRuleRecommendationRunDescription-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-DataQualityRuleRecommendationRunDescription-StartedOn"></a>
The date and time when this run started.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-DataQualityRuleRecommendationRunDescription-Status"></a>
The status for this run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

## See Also
<a name="API_DataQualityRuleRecommendationRunDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRuleRecommendationRunDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRuleRecommendationRunDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRuleRecommendationRunDescription)
