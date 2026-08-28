---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpnConnectionDetails.html
---

# AwsEc2VpnConnectionDetails
<a name="API_AwsEc2VpnConnectionDetails"></a>

Details about an Amazon EC2 VPN connection.

## Contents
<a name="API_AwsEc2VpnConnectionDetails_Contents"></a>

 ** Category **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-Category"></a>
The category of the VPN connection. `VPN` indicates an AWS VPN connection. `VPN-Classic` indicates an AWS Classic VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CustomerGatewayConfiguration **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-CustomerGatewayConfiguration"></a>
The configuration information for the VPN connection's customer gateway, in the native XML format.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CustomerGatewayId **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-CustomerGatewayId"></a>
The identifier of the customer gateway that is at your end of the VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Options **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-Options"></a>
The VPN connection options.
Type: [AwsEc2VpnConnectionOptionsDetails](API_AwsEc2VpnConnectionOptionsDetails.md) object
Required: No

 ** Routes **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-Routes"></a>
The static routes that are associated with the VPN connection.
Type: Array of [AwsEc2VpnConnectionRoutesDetails](API_AwsEc2VpnConnectionRoutesDetails.md) objects
Required: No

 ** State **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-State"></a>
The current state of the VPN connection. Valid values are as follows:
+  `available`
+  `deleted`
+  `deleting`
+  `pending`
Type: String
Pattern: `.*\S.*`
Required: No

 ** TransitGatewayId **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-TransitGatewayId"></a>
The identifier of the transit gateway that is associated with the VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-Type"></a>
The type of VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VgwTelemetry **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-VgwTelemetry"></a>
Information about the VPN tunnel.
Type: Array of [AwsEc2VpnConnectionVgwTelemetryDetails](API_AwsEc2VpnConnectionVgwTelemetryDetails.md) objects
Required: No

 ** VpnConnectionId **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-VpnConnectionId"></a>
The identifier of the VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpnGatewayId **   <a name="securityhub-Type-AwsEc2VpnConnectionDetails-VpnGatewayId"></a>
The identifier of the virtual private gateway that is at the AWS side of the VPN connection.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpnConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpnConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpnConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpnConnectionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
