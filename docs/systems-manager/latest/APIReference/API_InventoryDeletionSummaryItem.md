---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryDeletionSummaryItem.html
---

# InventoryDeletionSummaryItem
<a name="API_InventoryDeletionSummaryItem"></a>

Either a count, remaining count, or a version number in a delete inventory summary.

## Contents
<a name="API_InventoryDeletionSummaryItem_Contents"></a>

 ** Count **   <a name="systemsmanager-Type-InventoryDeletionSummaryItem-Count"></a>
A count of the number of deleted items.
Type: Integer
Required: No

 ** RemainingCount **   <a name="systemsmanager-Type-InventoryDeletionSummaryItem-RemainingCount"></a>
The remaining number of items to delete.
Type: Integer
Required: No

 ** Version **   <a name="systemsmanager-Type-InventoryDeletionSummaryItem-Version"></a>
The inventory type version.
Type: String
Pattern: `^([0-9]{1,6})(\.[0-9]{1,6})$`
Required: No

## See Also
<a name="API_InventoryDeletionSummaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryDeletionSummaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryDeletionSummaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryDeletionSummaryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
