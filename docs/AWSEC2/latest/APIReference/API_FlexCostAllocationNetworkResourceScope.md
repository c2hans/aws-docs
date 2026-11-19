---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationNetworkResourceScope.html
---

# FlexCostAllocationNetworkResourceScope

Specifies a scope of network resources for a scope-based policy association.

## Contents
<a name="API_FlexCostAllocationNetworkResourceScope_Contents"></a>

 ** ResourceIds.N **
The IDs of the resources owned by you that define the scope. You can specify from 1 to 20 IDs. This parameter is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** ResourceType **
The type of scope. This parameter is required. Valid values are `account`, `vpc`, and `subnet`.
Type: String
Valid Values: `account | vpc | subnet`
Required: Yes

## See Also
<a name="API_FlexCostAllocationNetworkResourceScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationNetworkResourceScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationNetworkResourceScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationNetworkResourceScope)
