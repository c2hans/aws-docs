---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsAggregator.html
---

# OpsAggregator
<a name="API_OpsAggregator"></a>

One or more aggregators for viewing counts of OpsData using different dimensions such as `Source`, `CreatedTime`, or `Source and CreatedTime`, to name a few.

## Contents
<a name="API_OpsAggregator_Contents"></a>

 ** Aggregators **   <a name="systemsmanager-Type-OpsAggregator-Aggregators"></a>
A nested aggregator for viewing counts of OpsData.
Type: Array of [OpsAggregator](#API_OpsAggregator) objects
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Required: No

 ** AggregatorType **   <a name="systemsmanager-Type-OpsAggregator-AggregatorType"></a>
Either a `Range` or `Count` aggregator for limiting an OpsData summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^(range|count|sum)`
Required: No

 ** AttributeName **   <a name="systemsmanager-Type-OpsAggregator-AttributeName"></a>
The name of an OpsData attribute on which to limit the count of OpsData.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Filters **   <a name="systemsmanager-Type-OpsAggregator-Filters"></a>
The aggregator filters.
Type: Array of [OpsFilter](API_OpsFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** TypeName **   <a name="systemsmanager-Type-OpsAggregator-TypeName"></a>
The data type name to use for viewing counts of OpsData.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: No

 ** Values **   <a name="systemsmanager-Type-OpsAggregator-Values"></a>
The aggregator value.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_OpsAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsAggregator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
