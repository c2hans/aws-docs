---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayRouteResources.html
---

# GatewayRouteResources
<a name="API_GatewayRouteResources"></a>

The service-specific infrastructure that a gateway manages for a route, keyed by gateway type.

## Contents
<a name="API_GatewayRouteResources_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hostSharedAlb **   <a name="ECS-Type-GatewayRouteResources-hostSharedAlb"></a>
The Application Load Balancer resources for a host-based, shared ALB gateway.
Type: Array of [GatewayRouteAlbResources](API_GatewayRouteAlbResources.md) objects
Required: No

## See Also
<a name="API_GatewayRouteResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayRouteResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayRouteResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayRouteResources)
