---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryResultEntity.html
---

# InventoryResultEntity
<a name="API_InventoryResultEntity"></a>

Inventory query results.

## Contents
<a name="API_InventoryResultEntity_Contents"></a>

 ** Data **   <a name="systemsmanager-Type-InventoryResultEntity-Data"></a>
The data section in the inventory result entity JSON.
Type: String to [InventoryResultItem](API_InventoryResultItem.md) object map
Required: No

 ** Id **   <a name="systemsmanager-Type-InventoryResultEntity-Id"></a>
ID of the inventory result entity. For example, for managed node inventory the result will be the managed node ID. For EC2 instance inventory, the result will be the instance ID.
Type: String
Required: No

## See Also
<a name="API_InventoryResultEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryResultEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryResultEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryResultEntity)
