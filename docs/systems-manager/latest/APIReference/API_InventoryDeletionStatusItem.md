---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryDeletionStatusItem.html
---

# InventoryDeletionStatusItem
<a name="API_InventoryDeletionStatusItem"></a>

Status information returned by the `DeleteInventory` operation.

## Contents
<a name="API_InventoryDeletionStatusItem_Contents"></a>

 ** DeletionId **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-DeletionId"></a>
The deletion ID returned by the `DeleteInventory` operation.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** DeletionStartTime **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-DeletionStartTime"></a>
The UTC timestamp when the delete operation started.
Type: Timestamp
Required: No

 ** DeletionSummary **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-DeletionSummary"></a>
Information about the delete operation. For more information about this summary, see [Understanding the delete inventory summary](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom.html#delete-custom-inventory) in the * AWS Systems Manager User Guide*.
Type: [InventoryDeletionSummary](API_InventoryDeletionSummary.md) object
Required: No

 ** LastStatus **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-LastStatus"></a>
The status of the operation. Possible values are InProgress and Complete.
Type: String
Valid Values: `InProgress | Complete`
Required: No

 ** LastStatusMessage **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-LastStatusMessage"></a>
Information about the status.
Type: String
Required: No

 ** LastStatusUpdateTime **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-LastStatusUpdateTime"></a>
The UTC timestamp of when the last status report.
Type: Timestamp
Required: No

 ** TypeName **   <a name="systemsmanager-Type-InventoryDeletionStatusItem-TypeName"></a>
The name of the inventory data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: No

## See Also
<a name="API_InventoryDeletionStatusItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryDeletionStatusItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryDeletionStatusItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryDeletionStatusItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
