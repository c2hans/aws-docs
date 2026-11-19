---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_NatGatewayAttachment.html
---

# NatGatewayAttachment

The NAT gateway that's attached to a proxy mode firewall in an Availability Zone, and the status of the attachment. Traffic that the firewall allows in the Availability Zone leaves through this NAT gateway.

## Contents
<a name="API_NatGatewayAttachment_Contents"></a>

 ** NatGatewayId **   <a name="networkfirewall-Type-NatGatewayAttachment-NatGatewayId"></a>
The ID of the NAT gateway.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Status **   <a name="networkfirewall-Type-NatGatewayAttachment-Status"></a>
The status of the NAT gateway attachment. `READY` means that the NAT gateway is attached and the firewall can send traffic through it. Other values are `CREATING`, `UPDATING`, `DELETING`, and `FAILED`.
Type: String
Valid Values: `CREATING | READY | UPDATING | FAILED | DELETING`
Required: Yes

 ** DnsName **   <a name="networkfirewall-Type-NatGatewayAttachment-DnsName"></a>
The proxy DNS name of the firewall in this Availability Zone. This is the same as the `DnsName` of the firewall's `Attachment`.
Type: String
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-NatGatewayAttachment-StatusMessage"></a>
The reason that Network Firewall couldn't create or attach the NAT gateway, if it couldn't.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9- ]+$`
Required: No

## See Also
<a name="API_NatGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/NatGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/NatGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/NatGatewayAttachment)
