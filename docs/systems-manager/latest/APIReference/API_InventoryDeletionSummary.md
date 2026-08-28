---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryDeletionSummary.html
---

# InventoryDeletionSummary
<a name="API_InventoryDeletionSummary"></a>

Information about the delete operation.

## Contents
<a name="API_InventoryDeletionSummary_Contents"></a>

 ** RemainingCount **   <a name="systemsmanager-Type-InventoryDeletionSummary-RemainingCount"></a>
Remaining number of items to delete.
Type: Integer
Required: No

 ** SummaryItems **   <a name="systemsmanager-Type-InventoryDeletionSummary-SummaryItems"></a>
A list of counts and versions for deleted items.
Type: Array of [InventoryDeletionSummaryItem](API_InventoryDeletionSummaryItem.md) objects
Required: No

 ** TotalCount **   <a name="systemsmanager-Type-InventoryDeletionSummary-TotalCount"></a>
The total number of items to delete. This count doesn't change during the delete operation.
Type: Integer
Required: No

## See Also
<a name="API_InventoryDeletionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryDeletionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryDeletionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryDeletionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
