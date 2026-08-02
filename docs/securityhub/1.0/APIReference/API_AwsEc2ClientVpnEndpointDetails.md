---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2ClientVpnEndpointDetails.html
---

# AwsEc2ClientVpnEndpointDetails
<a name="API_AwsEc2ClientVpnEndpointDetails"></a>

 Describes an AWS Client VPN endpoint. A Client VPN endpoint is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for all client VPN sessions.

## Contents
<a name="API_AwsEc2ClientVpnEndpointDetails_Contents"></a>

 ** AuthenticationOptions **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-AuthenticationOptions"></a>
 Information about the authentication method used by the Client VPN endpoint.
Type: Array of [AwsEc2ClientVpnEndpointAuthenticationOptionsDetails](API_AwsEc2ClientVpnEndpointAuthenticationOptionsDetails.md) objects
Required: No

 ** ClientCidrBlock **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ClientCidrBlock"></a>
 The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClientConnectOptions **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ClientConnectOptions"></a>
 The options for managing connection authorization for new client connections.
Type: [AwsEc2ClientVpnEndpointClientConnectOptionsDetails](API_AwsEc2ClientVpnEndpointClientConnectOptionsDetails.md) object
Required: No

 ** ClientLoginBannerOptions **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ClientLoginBannerOptions"></a>
 Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Type: [AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails](API_AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails.md) object
Required: No

 ** ClientVpnEndpointId **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ClientVpnEndpointId"></a>
 The ID of the Client VPN endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ConnectionLogOptions **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ConnectionLogOptions"></a>
 Information about the client connection logging options for the Client VPN endpoint.
Type: [AwsEc2ClientVpnEndpointConnectionLogOptionsDetails](API_AwsEc2ClientVpnEndpointConnectionLogOptionsDetails.md) object
Required: No

 ** Description **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-Description"></a>
 A brief description of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DnsServer **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-DnsServer"></a>
 Information about the DNS servers to be used for DNS resolution.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityGroupIdSet **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-SecurityGroupIdSet"></a>
 The IDs of the security groups for the target network.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SelfServicePortalUrl **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-SelfServicePortalUrl"></a>
 The URL of the self-service portal.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServerCertificateArn **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-ServerCertificateArn"></a>
 The Amazon Resource Name (ARN) of the server certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SessionTimeoutHours **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-SessionTimeoutHours"></a>
 The maximum VPN session duration time in hours.
Type: Integer
Required: No

 ** SplitTunnel **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-SplitTunnel"></a>
 Indicates whether split-tunnel is enabled in the AWS Client VPN endpoint.
Type: Boolean
Required: No

 ** TransportProtocol **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-TransportProtocol"></a>
 The transport protocol used by the Client VPN endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-VpcId"></a>
 The ID of the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpnPort **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointDetails-VpnPort"></a>
 The port number for the Client VPN endpoint.
Type: Integer
Required: No

## See Also
<a name="API_AwsEc2ClientVpnEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2ClientVpnEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2ClientVpnEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2ClientVpnEndpointDetails)
