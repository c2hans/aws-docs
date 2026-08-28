---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_StatisticsConfiguration.html
---

# StatisticsConfiguration
<a name="API_StatisticsConfiguration"></a>

Configuration of evaluations for a profile job. This configuration can be used to select evaluations and override the parameters of selected evaluations.

## Contents
<a name="API_StatisticsConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IncludedStatistics **   <a name="databrew-Type-StatisticsConfiguration-IncludedStatistics"></a>
List of included evaluations. When the list is undefined, all supported evaluations will be included.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: No

 ** Overrides **   <a name="databrew-Type-StatisticsConfiguration-Overrides"></a>
List of overrides for evaluations.
Type: Array of [StatisticOverride](API_StatisticOverride.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_StatisticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/StatisticsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/StatisticsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/StatisticsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
