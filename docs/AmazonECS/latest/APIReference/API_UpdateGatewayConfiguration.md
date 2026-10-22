---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateGatewayConfiguration.html
---

# UpdateGatewayConfiguration
<a name="API_UpdateGatewayConfiguration"></a>

The type-specific configuration to change on a gateway. The variant must match the gateway's existing type.

## Contents
<a name="API_UpdateGatewayConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** hostSharedAlb **   <a name="ECS-Type-UpdateGatewayConfiguration-hostSharedAlb"></a>
The mutable configuration for a host-based, shared Application Load Balancer gateway.
Type: [UpdateGatewayAlbConfiguration](API_UpdateGatewayAlbConfiguration.md) object
Required: No

## See Also
<a name="API_UpdateGatewayConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateGatewayConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateGatewayConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateGatewayConfiguration)
