---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPeeringAttachmentRequestOptions.html
---

# CreateTransitGatewayPeeringAttachmentRequestOptions
<a name="API_CreateTransitGatewayPeeringAttachmentRequestOptions"></a>

Describes whether dynamic routing is enabled or disabled for the transit gateway peering request.

## Contents
<a name="API_CreateTransitGatewayPeeringAttachmentRequestOptions_Contents"></a>

 ** AllowMultipathResilience **
Specifies whether you allow multipath resilience for the requester side of the transit gateway peering attachment. Multipath resilience is supported only for inter-Region transit gateway peering attachments between supported Regions. It takes effect only when both the requester and the accepter allow it. If you don't specify this parameter, the default is `false`.
Type: Boolean
Required: No

 ** DynamicRouting **
Indicates whether dynamic routing is enabled or disabled.
Type: String
Valid Values: `enable | disable`
Required: No

 ** MultipathResilienceMode **
The multipath resilience mode. You can specify this parameter only if `AllowMultipathResilience` is `true`.
The following value is valid:
+  `always-on` – Replicates traffic across multiple network paths while multipath resilience is in effect.
If `AllowMultipathResilience` is `true` and you don't specify a mode, the default is `always-on`.
Type: String
Valid Values: `always-on`
Required: No

## See Also
<a name="API_CreateTransitGatewayPeeringAttachmentRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayPeeringAttachmentRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayPeeringAttachmentRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayPeeringAttachmentRequestOptions)
