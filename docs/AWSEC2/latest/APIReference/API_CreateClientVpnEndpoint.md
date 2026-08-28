---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnEndpoint.html
---

# CreateClientVpnEndpoint
<a name="API_CreateClientVpnEndpoint"></a>

Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.

## Request Parameters
<a name="API_CreateClientVpnEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Authentication.N**
Information about the authentication method to be used to authenticate clients.
Type: Array of [ClientVpnAuthenticationRequest](API_ClientVpnAuthenticationRequest.md) objects
Required: Yes

 **ClientCidrBlock**
The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. Client CIDR range must have a size of at least /22 and must not be greater than /12.
Type: String
Required: No

 **ClientConnectOptions**
The options for managing connection authorization for new client connections.
Type: [ClientConnectOptions](API_ClientConnectOptions.md) object
Required: No

 **ClientLoginBannerOptions**
Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Type: [ClientLoginBannerOptions](API_ClientLoginBannerOptions.md) object
Required: No

 **ClientRouteEnforcementOptions**
Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.
Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.
Type: [ClientRouteEnforcementOptions](API_ClientRouteEnforcementOptions.md) object
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ConnectionLogOptions**
Information about the client connection logging options.
If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:
+ Client connection requests
+ Client connection results (successful and unsuccessful)
+ Reasons for unsuccessful client connection requests
+ Client connection termination time
Type: [ConnectionLogOptions](API_ConnectionLogOptions.md) object
Required: Yes

 **Description**
A brief description of the Client VPN endpoint.
Type: String
Required: No

 **DisconnectOnSessionTimeout**
Indicates whether the client VPN session is disconnected after the maximum timeout specified in `SessionTimeoutHours` is reached. If `true`, users are prompted to reconnect client VPN. If `false`, client VPN attempts to reconnect automatically. The default value is `true`.
Type: Boolean
Required: No

 **DnsServers.N**
Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address configured on the device is used for the DNS server.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndpointIpAddressType**
The IP address type for the Client VPN endpoint. Valid values are `ipv4` (default) for IPv4 addressing only, `ipv6` for IPv6 addressing only, or `dual-stack` for both IPv4 and IPv6 addressing. When set to `dual-stack,` clients can connect to the endpoint using either IPv4 or IPv6 addresses..
Type: String
Valid Values: `ipv4 | ipv6 | dual-stack`
Required: No

 **SecurityGroupId.N**
The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that contains the security groups.
Type: Array of strings
Required: No

 **SelfServicePortal**
Specify whether to enable the self-service portal for the Client VPN endpoint.
Default Value: `enabled`
Type: String
Valid Values: `enabled | disabled`
Required: No

 **ServerCertificateArn**
The ARN of the server certificate. For more information, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/).
Type: String
Required: Yes

 **SessionTimeoutHours**
The maximum VPN session duration time in hours.
Valid values: `8 | 10 | 12 | 24`
Default value: `24`
Type: Integer
Required: No

 **SplitTunnel**
Indicates whether split-tunnel is enabled on the AWS Client VPN endpoint.
By default, split-tunnel on a VPN endpoint is disabled.
For information about split-tunnel VPN endpoints, see [Split-tunnel AWS Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the * AWS Client VPN Administrator Guide*.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to apply to the Client VPN endpoint during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TrafficIpAddressType**
The IP address type for traffic within the Client VPN tunnel. Valid values are `ipv4` (default) for IPv4 traffic only, `ipv6` for IPv6 addressing only, or `dual-stack` for both IPv4 and IPv6 traffic. When set to `dual-stack`, clients can access both IPv4 and IPv6 resources through the VPN .
Type: String
Valid Values: `ipv4 | ipv6 | dual-stack`
Required: No

 **TransitGatewayConfiguration**
The Transit Gateway configuration for the Client VPN endpoint. Use this parameter to associate the endpoint with a Transit Gateway instead of a VPC. You cannot specify both `TransitGatewayConfiguration` and `VpcId`/`SecurityGroupIds`.
Type: [TransitGatewayConfigurationInputStructure](API_TransitGatewayConfigurationInputStructure.md) object
Required: No

 **TransportProtocol**
The transport protocol to be used by the VPN session.
Default value: `udp`
Type: String
Valid Values: `tcp | udp`
Required: No

 **VpcId**
The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the default security group for the VPC is applied.
Type: String
Required: No

 **VpnPort**
The port number to assign to the Client VPN endpoint for TCP and UDP traffic.
Valid Values: `443` \| `1194`
Default Value: `443`
Type: Integer
Required: No

## Response Elements
<a name="API_CreateClientVpnEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **clientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String

 **dnsName**
The DNS name to be used by clients when establishing their VPN session.
Type: String

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the Client VPN endpoint.
Type: [ClientVpnEndpointStatus](API_ClientVpnEndpointStatus.md) object

## Errors
<a name="API_CreateClientVpnEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateClientVpnEndpoint_Examples"></a>

### Example
<a name="API_CreateClientVpnEndpoint_Example_1"></a>

This example creates a Client VPN endpoint.

#### Sample Request
<a name="API_CreateClientVpnEndpoint_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateClientVpnEndpoint
&ClientCidrBlock=11.0.0.0/16
&ServerCertificateArn=arn:aws:acm:us-east-1:123456789098:certificate/82916b3c-7449-43cf-ab9e-EXAMPLE
&Authentication.1.Type=certificate-authentication
&Authentication.1.MutualAuthentication.1.ClientRootCertificateChainArn=arn:aws:acm:us-east-1:123456789098:certificate/82916b3c-7449-43cf-ab9e-EXAMPLE
&ConnectionLogOptions.Enabled=false
&DnsServers=11.11.0.1
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateClientVpnEndpoint_Example_1_Response"></a>

```
<CreateClientVpnEndpointResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c11b2aa2-c48d-4711-a394-43cbe8961c46</requestId>
    <dnsName>cvpn-endpoint-00c5d11fc4729f2a5.prod.clientvpn.us-east-1.amazonaws.com</dnsName>
    <status>
        <code>pending-associate</code>
    </status>
    <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4729f2a5</clientVpnEndpointId>
</CreateClientVpnEndpointResponse>
```

## See Also
<a name="API_CreateClientVpnEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateClientVpnEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateClientVpnEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
