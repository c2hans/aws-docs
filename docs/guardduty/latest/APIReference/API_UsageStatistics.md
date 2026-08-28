---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageStatistics.html
---

# UsageStatistics
<a name="API_UsageStatistics"></a>

Contains the result of GuardDuty usage. If a UsageStatisticType is provided the result for other types will be null.

## Contents
<a name="API_UsageStatistics_Contents"></a>

 ** sumByAccount **   <a name="guardduty-Type-UsageStatistics-sumByAccount"></a>
The usage statistic sum organized by account ID.
Type: Array of [UsageAccountResult](API_UsageAccountResult.md) objects
Required: No

 ** sumByDataSource **   <a name="guardduty-Type-UsageStatistics-sumByDataSource"></a>
The usage statistic sum organized by on data source.
Type: Array of [UsageDataSourceResult](API_UsageDataSourceResult.md) objects
Required: No

 ** sumByFeature **   <a name="guardduty-Type-UsageStatistics-sumByFeature"></a>
The usage statistic sum organized by feature.
Type: Array of [UsageFeatureResult](API_UsageFeatureResult.md) objects
Required: No

 ** sumByResource **   <a name="guardduty-Type-UsageStatistics-sumByResource"></a>
The usage statistic sum organized by resource.
Type: Array of [UsageResourceResult](API_UsageResourceResult.md) objects
Required: No

 ** topAccountsByFeature **   <a name="guardduty-Type-UsageStatistics-topAccountsByFeature"></a>
Lists the top 50 accounts by feature that have generated the most GuardDuty usage, in the order from most to least expensive.
Currently, this doesn't support `RDS_LOGIN_EVENTS`.
Type: Array of [UsageTopAccountsResult](API_UsageTopAccountsResult.md) objects
Required: No

 ** topResources **   <a name="guardduty-Type-UsageStatistics-topResources"></a>
Lists the top 50 resources that have generated the most GuardDuty usage, in order from most to least expensive.
Type: Array of [UsageResourceResult](API_UsageResourceResult.md) objects
Required: No

## See Also
<a name="API_UsageStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
