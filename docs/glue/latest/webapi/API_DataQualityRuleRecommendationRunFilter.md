---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRuleRecommendationRunFilter.html
---

# DataQualityRuleRecommendationRunFilter
<a name="API_DataQualityRuleRecommendationRunFilter"></a>

A filter for listing data quality recommendation runs.

## Contents
<a name="API_DataQualityRuleRecommendationRunFilter_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityRuleRecommendationRunFilter-DataSource"></a>
Filter based on a specified data source (AWS Glue table).
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** StartedAfter **   <a name="Glue-Type-DataQualityRuleRecommendationRunFilter-StartedAfter"></a>
Filter based on time for results started after provided time.
Type: Timestamp
Required: No

 ** StartedBefore **   <a name="Glue-Type-DataQualityRuleRecommendationRunFilter-StartedBefore"></a>
Filter based on time for results started before provided time.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityRuleRecommendationRunFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRuleRecommendationRunFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRuleRecommendationRunFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRuleRecommendationRunFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
