---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedInstancesNetworkConfiguration.html
---

# ManagedInstancesNetworkConfiguration
<a name="API_ManagedInstancesNetworkConfiguration"></a>

The network configuration for Amazon ECS Managed Instances. This specifies the VPC subnets and security groups that instances use for network connectivity. Amazon ECS Managed Instances support multiple network modes including `awsvpc` (instances receive ENIs for task isolation), `host` (instances share network namespace with tasks), and `none` (no external network connectivity), ensuring backward compatibility for migrating workloads from Fargate or Amazon EC2.

## Contents
<a name="API_ManagedInstancesNetworkConfiguration_Contents"></a>

 ** securityGroups **   <a name="ECS-Type-ManagedInstancesNetworkConfiguration-securityGroups"></a>
The list of security group IDs to apply to Amazon ECS Managed Instances. These security groups control the network traffic allowed to and from the instances.
Type: Array of strings
Required: No

 ** subnets **   <a name="ECS-Type-ManagedInstancesNetworkConfiguration-subnets"></a>
The list of subnet IDs where Amazon ECS can launch Amazon ECS Managed Instances. Instances are distributed across the specified subnets for high availability. All subnets must be in the same VPC.
Type: Array of strings
Required: No

## See Also
<a name="API_ManagedInstancesNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedInstancesNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedInstancesNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedInstancesNetworkConfiguration)
