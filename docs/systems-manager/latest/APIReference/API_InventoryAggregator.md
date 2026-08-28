---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryAggregator.html
---

# InventoryAggregator
<a name="API_InventoryAggregator"></a>

Specifies the inventory type and attribute for the aggregation execution.

## Contents
<a name="API_InventoryAggregator_Contents"></a>

 ** Aggregators **   <a name="systemsmanager-Type-InventoryAggregator-Aggregators"></a>
Nested aggregators to further refine aggregation for an inventory type.
Type: Array of [InventoryAggregator](#API_InventoryAggregator) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Expression **   <a name="systemsmanager-Type-InventoryAggregator-Expression"></a>
The inventory type and attribute name for aggregation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Groups **   <a name="systemsmanager-Type-InventoryAggregator-Groups"></a>
A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don't match the specified criteria.
Type: Array of [InventoryGroup](API_InventoryGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

## See Also
<a name="API_InventoryAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryAggregator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
