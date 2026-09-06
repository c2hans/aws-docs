---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CapacityProviderVpcConfig.html
---

# CapacityProviderVpcConfig
<a name="API_CapacityProviderVpcConfig"></a>

VPC configuration that specifies the network settings for compute instances managed by the capacity provider.

## Contents
<a name="API_CapacityProviderVpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="lambda-Type-CapacityProviderVpcConfig-SecurityGroupIds"></a>
A list of security group IDs that control network access for compute instances managed by the capacity provider.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

 ** SubnetIds **   <a name="lambda-Type-CapacityProviderVpcConfig-SubnetIds"></a>
A list of subnet IDs where the capacity provider launches compute instances.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Required: Yes

## See Also
<a name="API_CapacityProviderVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CapacityProviderVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CapacityProviderVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CapacityProviderVpcConfig)
