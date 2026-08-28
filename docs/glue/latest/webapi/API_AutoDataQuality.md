---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AutoDataQuality.html
---

# AutoDataQuality
<a name="API_AutoDataQuality"></a>

Specifies configuration options for automatic data quality evaluation in AWS Glue jobs. This structure enables automated data quality checks and monitoring during ETL operations, helping to ensure data integrity and reliability without manual intervention.

## Contents
<a name="API_AutoDataQuality_Contents"></a>

 ** EvaluationContext **   <a name="Glue-Type-AutoDataQuality-EvaluationContext"></a>
The evaluation context for the automatic data quality checks. This defines the scope and parameters for the data quality evaluation.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** IsEnabled **   <a name="Glue-Type-AutoDataQuality-IsEnabled"></a>
Specifies whether automatic data quality evaluation is enabled. When set to `true`, data quality checks are performed automatically.
Type: Boolean
Required: No

## See Also
<a name="API_AutoDataQuality_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AutoDataQuality)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AutoDataQuality)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AutoDataQuality)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
