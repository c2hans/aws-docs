---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EvaluateDataQuality.html
---

# EvaluateDataQuality
<a name="API_EvaluateDataQuality"></a>

Specifies your data quality evaluation criteria.

## Contents
<a name="API_EvaluateDataQuality_Contents"></a>

 ** Inputs **   <a name="Glue-Type-EvaluateDataQuality-Inputs"></a>
The inputs of your data quality evaluation.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-EvaluateDataQuality-Name"></a>
The name of the data quality evaluation.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Ruleset **   <a name="Glue-Type-EvaluateDataQuality-Ruleset"></a>
The ruleset for your data quality evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `([\u0020-\u007E\r\s\n])*`
Required: Yes

 ** Output **   <a name="Glue-Type-EvaluateDataQuality-Output"></a>
The output of your data quality evaluation.
Type: String
Valid Values: `PrimaryInput | EvaluationResults`
Required: No

 ** PublishingOptions **   <a name="Glue-Type-EvaluateDataQuality-PublishingOptions"></a>
Options to configure how your results are published.
Type: [DQResultsPublishingOptions](API_DQResultsPublishingOptions.md) object
Required: No

 ** StopJobOnFailureOptions **   <a name="Glue-Type-EvaluateDataQuality-StopJobOnFailureOptions"></a>
Options to configure how your job will stop if your data quality evaluation fails.
Type: [DQStopJobOnFailureOptions](API_DQStopJobOnFailureOptions.md) object
Required: No

## See Also
<a name="API_EvaluateDataQuality_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EvaluateDataQuality)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EvaluateDataQuality)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EvaluateDataQuality)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
