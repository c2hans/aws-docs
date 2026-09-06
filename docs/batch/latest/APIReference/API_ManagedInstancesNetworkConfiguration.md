---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ManagedInstancesNetworkConfiguration.html
---

# ManagedInstancesNetworkConfiguration
<a name="API_ManagedInstancesNetworkConfiguration"></a>

The network configuration for Amazon ECS Managed Instances. Specifies the VPC subnets and security groups where instances are launched.

## Contents
<a name="API_ManagedInstancesNetworkConfiguration_Contents"></a>

 ** securityGroups **   <a name="Batch-Type-ManagedInstancesNetworkConfiguration-securityGroups"></a>
The VPC security groups to associate with the managed instances.
Type: Array of strings
Required: Yes

 ** subnets **   <a name="Batch-Type-ManagedInstancesNetworkConfiguration-subnets"></a>
The VPC subnets where managed instances are launched. If your subnets don't provide public IP addresses, they must have a NAT gateway for outbound internet access.
Type: Array of strings
Required: Yes

## See Also
<a name="API_ManagedInstancesNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ManagedInstancesNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ManagedInstancesNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ManagedInstancesNetworkConfiguration)
