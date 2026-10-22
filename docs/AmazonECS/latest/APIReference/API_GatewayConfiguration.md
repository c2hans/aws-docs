---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConfiguration.html
---

# GatewayConfiguration
<a name="API_GatewayConfiguration"></a>

The type-specific configuration for a gateway that you provide when you create it. Exactly one variant is set, and it determines the gateway type.

## Contents
<a name="API_GatewayConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hostSharedAlb **   <a name="ECS-Type-GatewayConfiguration-hostSharedAlb"></a>
The configuration for a host-based, shared Application Load Balancer gateway. Each service that uses the gateway is assigned a unique DNS host name.
Type: [HostSharedAlbConfiguration](API_HostSharedAlbConfiguration.md) object
Required: No

## See Also
<a name="API_GatewayConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConfiguration)
