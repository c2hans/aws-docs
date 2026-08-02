---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_NetworkConfig.html
---

# NetworkConfig
<a name="API_NetworkConfig"></a>

The network configuration for a notebook run in Amazon SageMaker Unified Studio.

## Contents
<a name="API_NetworkConfig_Contents"></a>

 ** networkAccessType **   <a name="datazone-Type-NetworkConfig-networkAccessType"></a>
The network access type for the notebook run. Valid values are `PUBLIC_INTERNET_ONLY` and `VPC_ONLY`.
Type: String
Valid Values: `PUBLIC_INTERNET_ONLY | VPC_ONLY`
Required: Yes

 ** securityGroupIds **   <a name="datazone-Type-NetworkConfig-securityGroupIds"></a>
The identifiers of the security groups for the notebook run. You can specify up to 5 security groups.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** subnetIds **   <a name="datazone-Type-NetworkConfig-subnetIds"></a>
The identifiers of the subnets for the notebook run. You can specify up to 10 subnets.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** vpcId **   <a name="datazone-Type-NetworkConfig-vpcId"></a>
The identifier of the VPC for the notebook run. This is required when the network access type is `VPC_ONLY`.
Type: String
Required: No

## See Also
<a name="API_NetworkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/NetworkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/NetworkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/NetworkConfig)
