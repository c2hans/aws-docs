---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DQResultsPublishingOptions.html
---

# DQResultsPublishingOptions
<a name="API_DQResultsPublishingOptions"></a>

Options to configure how your data quality evaluation results are published.

## Contents
<a name="API_DQResultsPublishingOptions_Contents"></a>

 ** CloudWatchMetricsEnabled **   <a name="Glue-Type-DQResultsPublishingOptions-CloudWatchMetricsEnabled"></a>
Enable metrics for your data quality results.
Type: Boolean
Required: No

 ** EvaluationContext **   <a name="Glue-Type-DQResultsPublishingOptions-EvaluationContext"></a>
The context of the evaluation.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** ResultsPublishingEnabled **   <a name="Glue-Type-DQResultsPublishingOptions-ResultsPublishingEnabled"></a>
Enable publishing for your data quality results.
Type: Boolean
Required: No

 ** ResultsS3Prefix **   <a name="Glue-Type-DQResultsPublishingOptions-ResultsS3Prefix"></a>
The Amazon S3 prefix prepended to the results.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_DQResultsPublishingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DQResultsPublishingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DQResultsPublishingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DQResultsPublishingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
