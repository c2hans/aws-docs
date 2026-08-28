---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRulesetEvaluationRunFilter.html
---

# DataQualityRulesetEvaluationRunFilter
<a name="API_DataQualityRulesetEvaluationRunFilter"></a>

The filter criteria.

## Contents
<a name="API_DataQualityRulesetEvaluationRunFilter_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityRulesetEvaluationRunFilter-DataSource"></a>
Filter based on a data source (an AWS Glue table) associated with the run.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** StartedAfter **   <a name="Glue-Type-DataQualityRulesetEvaluationRunFilter-StartedAfter"></a>
Filter results by runs that started after this time.
Type: Timestamp
Required: No

 ** StartedBefore **   <a name="Glue-Type-DataQualityRulesetEvaluationRunFilter-StartedBefore"></a>
Filter results by runs that started before this time.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityRulesetEvaluationRunFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRulesetEvaluationRunFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRulesetEvaluationRunFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRulesetEvaluationRunFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
