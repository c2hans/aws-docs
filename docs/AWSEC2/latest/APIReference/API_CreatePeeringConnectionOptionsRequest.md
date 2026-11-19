---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePeeringConnectionOptionsRequest.html
---

# CreatePeeringConnectionOptionsRequest

The VPC peering connection options to apply to the requester VPC when you create a VPC peering connection.

## Contents
<a name="API_CreatePeeringConnectionOptionsRequest_Contents"></a>

 ** AllowMultipathResilience **
Specifies whether you allow multipath resilience for the requester VPC. Multipath resilience is supported only for inter-Region VPC peering connections between supported Regions. It takes effect only when both the requester and the accepter allow it. Accepting the VPC peering connection request also allows multipath resilience for the accepter VPC. If you don't specify this parameter, the default is `false`.
Type: Boolean
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
<a name="API_CreatePeeringConnectionOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreatePeeringConnectionOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreatePeeringConnectionOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreatePeeringConnectionOptionsRequest)
