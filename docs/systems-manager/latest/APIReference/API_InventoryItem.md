---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryItem.html
---

# InventoryItem
<a name="API_InventoryItem"></a>

Information collected from managed nodes based on your inventory policy document

## Contents
<a name="API_InventoryItem_Contents"></a>

 ** CaptureTime **   <a name="systemsmanager-Type-InventoryItem-CaptureTime"></a>
The time the inventory information was collected.
Type: String
Pattern: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`
Required: Yes

 ** SchemaVersion **   <a name="systemsmanager-Type-InventoryItem-SchemaVersion"></a>
The schema version for the inventory item.
Type: String
Pattern: `^([0-9]{1,6})(\.[0-9]{1,6})$`
Required: Yes

 ** TypeName **   <a name="systemsmanager-Type-InventoryItem-TypeName"></a>
The name of the inventory type. Default inventory item type names start with `AWS`. Custom inventory type names will start with Custom. Default inventory item types include the following: `AWS:AWSComponent`, `AWS:Application`, `AWS:InstanceInformation`, `AWS:Network`, and `AWS:WindowsUpdate`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

 ** Content **   <a name="systemsmanager-Type-InventoryItem-Content"></a>
The inventory data of the inventory type.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** ContentHash **   <a name="systemsmanager-Type-InventoryItem-ContentHash"></a>
MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API doesn't update the inventory item type contents if the MD5 hash hasn't changed since last update.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Context **   <a name="systemsmanager-Type-InventoryItem-Context"></a>
A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the `ExecutionId`, `ExecutionType`, `ComplianceType` properties of the `AWS:ComplianceItem` type.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_InventoryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
