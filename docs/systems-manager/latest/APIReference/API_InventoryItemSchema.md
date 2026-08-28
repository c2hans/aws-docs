---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryItemSchema.html
---

# InventoryItemSchema
<a name="API_InventoryItemSchema"></a>

The inventory item schema definition. Users can use this to compose inventory query filters.

## Contents
<a name="API_InventoryItemSchema_Contents"></a>

 ** Attributes **   <a name="systemsmanager-Type-InventoryItemSchema-Attributes"></a>
The schema attributes for inventory. This contains data type and attribute name.
Type: Array of [InventoryItemAttribute](API_InventoryItemAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** TypeName **   <a name="systemsmanager-Type-InventoryItemSchema-TypeName"></a>
The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: `AWS:AWSComponent`, `AWS:Application`, `AWS:InstanceInformation`, `AWS:Network`, and `AWS:WindowsUpdate`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

 ** DisplayName **   <a name="systemsmanager-Type-InventoryItemSchema-DisplayName"></a>
The alias name of the inventory type. The alias name is used for display purposes.
Type: String
Required: No

 ** Version **   <a name="systemsmanager-Type-InventoryItemSchema-Version"></a>
The schema version for the inventory item.
Type: String
Pattern: `^([0-9]{1,6})(\.[0-9]{1,6})$`
Required: No

## See Also
<a name="API_InventoryItemSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryItemSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryItemSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryItemSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
