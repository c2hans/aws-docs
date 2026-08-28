---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ColumnStatisticsConfiguration.html
---

# ColumnStatisticsConfiguration
<a name="API_ColumnStatisticsConfiguration"></a>

Configuration for column evaluations for a profile job. ColumnStatisticsConfiguration can be used to select evaluations and override parameters of evaluations for particular columns.

## Contents
<a name="API_ColumnStatisticsConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Statistics **   <a name="databrew-Type-ColumnStatisticsConfiguration-Statistics"></a>
Configuration for evaluations. Statistics can be used to select evaluations and override parameters of evaluations.
Type: [StatisticsConfiguration](API_StatisticsConfiguration.md) object
Required: Yes

 ** Selectors **   <a name="databrew-Type-ColumnStatisticsConfiguration-Selectors"></a>
List of column selectors. Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns.
Type: Array of [ColumnSelector](API_ColumnSelector.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ColumnStatisticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ColumnStatisticsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ColumnStatisticsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ColumnStatisticsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
