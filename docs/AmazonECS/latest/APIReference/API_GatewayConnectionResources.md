---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnectionResources.html
---

# GatewayConnectionResources
<a name="API_GatewayConnectionResources"></a>

The gateway-managed infrastructure resources for a connection, as a union keyed by gateway type.

## Contents
<a name="API_GatewayConnectionResources_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hostSharedAlb **   <a name="ECS-Type-GatewayConnectionResources-hostSharedAlb"></a>
The Application Load Balancer resources for a host-based, shared ALB gateway.
Type: Array of [GatewayConnectionAlbResources](API_GatewayConnectionAlbResources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_GatewayConnectionResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnectionResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnectionResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnectionResources)
