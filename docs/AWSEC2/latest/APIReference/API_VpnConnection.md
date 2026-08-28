---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnConnection.html
---

# VpnConnection
<a name="API_VpnConnection"></a>

Describes a VPN connection.

## Contents
<a name="API_VpnConnection_Contents"></a>

 ** category **
The category of the VPN connection. A value of `VPN` indicates an AWS VPN connection. A value of `VPN-Classic` indicates an AWS Classic VPN connection.
Type: String
Required: No

 ** coreNetworkArn **
The ARN of the core network.
Type: String
Required: No

 ** coreNetworkAttachmentArn **
The ARN of the core network attachment.
Type: String
Required: No

 ** customerGatewayConfiguration **
The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the [CreateVpnConnection](API_CreateVpnConnection.md) response; however, it's present in the [DescribeVpnConnections](API_DescribeVpnConnections.md) response only if the VPN connection is in the `pending` or `available` state.
Type: String
Required: No

 ** customerGatewayId **
The ID of the customer gateway at your end of the VPN connection.
Type: String
Required: No

 ** gatewayAssociationState **
The current state of the gateway association.
Type: String
Valid Values: `associated | not-associated | associating | disassociating`
Required: No

 ** options **
The VPN connection options.
Type: [VpnConnectionOptions](API_VpnConnectionOptions.md) object
Required: No

 ** preSharedKeyArn **
The Amazon Resource Name (ARN) of the Secrets Manager secret storing the pre-shared key(s) for the VPN connection.
Type: String
Required: No

 ** Routes.N **
The static routes associated with the VPN connection.
Type: Array of [VpnStaticRoute](API_VpnStaticRoute.md) objects
Required: No

 ** state **
The current state of the VPN connection.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** TagSet.N **
Any tags assigned to the VPN connection.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayId **
The ID of the transit gateway associated with the VPN connection.
Type: String
Required: No

 ** type **
The type of VPN connection.
Type: String
Valid Values: `ipsec.1`
Required: No

 ** VgwTelemetry.N **
Information about the VPN tunnel.
Type: Array of [VgwTelemetry](API_VgwTelemetry.md) objects
Required: No

 ** vpnConcentratorId **
The ID of the VPN concentrator associated with the VPN connection.
Type: String
Required: No

 ** vpnConnectionId **
The ID of the VPN connection.
Type: String
Required: No

 ** vpnGatewayId **
The ID of the virtual private gateway at the AWS side of the VPN connection.
Type: String
Required: No

## See Also
<a name="API_VpnConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
