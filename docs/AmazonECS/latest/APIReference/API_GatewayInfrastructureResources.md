---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayInfrastructureResources.html
---

# GatewayInfrastructureResources
<a name="API_GatewayInfrastructureResources"></a>

The gateway-managed infrastructure in a `DescribeGatewayResources` response, as a union keyed by gateway type.

## Contents
<a name="API_GatewayInfrastructureResources_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hostSharedAlb **   <a name="ECS-Type-GatewayInfrastructureResources-hostSharedAlb"></a>
The Application Load Balancer resource groups for a host-based, shared ALB gateway.
Type: Array of [ElbGatewayResources](API_ElbGatewayResources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_GatewayInfrastructureResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayInfrastructureResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayInfrastructureResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayInfrastructureResources)
