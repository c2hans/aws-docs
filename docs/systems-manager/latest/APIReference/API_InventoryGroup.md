---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryGroup.html
---

# InventoryGroup
<a name="API_InventoryGroup"></a>

A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don't match the specified criteria.

## Contents
<a name="API_InventoryGroup_Contents"></a>

 ** Filters **   <a name="systemsmanager-Type-InventoryGroup-Filters"></a>
Filters define the criteria for the group. The `matchingCount` field displays the number of resources that match the criteria. The `notMatchingCount` field displays the number of resources that don't match the criteria.
Type: Array of [InventoryFilter](API_InventoryFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** Name **   <a name="systemsmanager-Type-InventoryGroup-Name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_InventoryGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryGroup)
