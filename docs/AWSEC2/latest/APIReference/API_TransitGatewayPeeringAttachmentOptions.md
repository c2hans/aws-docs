---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPeeringAttachmentOptions.html
---

# TransitGatewayPeeringAttachmentOptions
<a name="API_TransitGatewayPeeringAttachmentOptions"></a>

Describes dynamic routing for the transit gateway peering attachment.

## Contents
<a name="API_TransitGatewayPeeringAttachmentOptions_Contents"></a>

 ** accepterAllowMultipathResilience **
Indicates whether the accepter allows multipath resilience for the transit gateway peering attachment.
Type: Boolean
Required: No

 ** accepterMultipathResilienceMode **
The multipath resilience mode for the accepter. This value is present only when the accepter allows multipath resilience.
Type: String
Valid Values: `always-on`
Required: No

 ** dynamicRouting **
Describes whether dynamic routing is enabled or disabled for the transit gateway peering attachment.
Type: String
Valid Values: `enable | disable`
Required: No

 ** multipathResilienceStatus **
The multipath resilience status of the transit gateway peering attachment. The possible values are:
+  `enabled` – Both the requester and the accepter allow multipath resilience.
+  `pending` – Either the requester or the accepter allows multipath resilience, but not both.
+  `disabled` – Neither the requester nor the accepter allows multipath resilience.
Type: String
Valid Values: `pending | enabled | disabled`
Required: No

 ** requesterAllowMultipathResilience **
Indicates whether the requester allows multipath resilience for the transit gateway peering attachment.
Type: Boolean
Required: No

 ** requesterMultipathResilienceMode **
The multipath resilience mode for the requester. This value is present only when the requester allows multipath resilience.
Type: String
Valid Values: `always-on`
Required: No

## See Also
<a name="API_TransitGatewayPeeringAttachmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPeeringAttachmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPeeringAttachmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPeeringAttachmentOptions)
