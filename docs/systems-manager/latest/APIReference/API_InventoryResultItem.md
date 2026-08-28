---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryResultItem.html
---

# InventoryResultItem
<a name="API_InventoryResultItem"></a>

The inventory result item.

## Contents
<a name="API_InventoryResultItem_Contents"></a>

 ** Content **   <a name="systemsmanager-Type-InventoryResultItem-Content"></a>
Contains all the inventory data of the item type. Results include attribute names and values.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** SchemaVersion **   <a name="systemsmanager-Type-InventoryResultItem-SchemaVersion"></a>
The schema version for the inventory result item/
Type: String
Pattern: `^([0-9]{1,6})(\.[0-9]{1,6})$`
Required: Yes

 ** TypeName **   <a name="systemsmanager-Type-InventoryResultItem-TypeName"></a>
The name of the inventory result item type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

 ** CaptureTime **   <a name="systemsmanager-Type-InventoryResultItem-CaptureTime"></a>
The time inventory item data was captured.
Type: String
Pattern: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`
Required: No

 ** ContentHash **   <a name="systemsmanager-Type-InventoryResultItem-ContentHash"></a>
MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API doesn't update the inventory item type contents if the MD5 hash hasn't changed since last update.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_InventoryResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
