---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-clientvpnendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint
<a name="aws-resource-ec2-clientvpnendpoint"></a>

Specifies a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.

## Syntax
<a name="aws-resource-ec2-clientvpnendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-clientvpnendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::ClientVpnEndpoint",
  "Properties" : {
      "[AuthenticationOptions](#cfn-ec2-clientvpnendpoint-authenticationoptions)" : {{[ ClientAuthenticationRequest, ... ]}},
      "[ClientCidrBlock](#cfn-ec2-clientvpnendpoint-clientcidrblock)" : {{String}},
      "[ClientConnectOptions](#cfn-ec2-clientvpnendpoint-clientconnectoptions)" : {{ClientConnectOptions}},
      "[ClientLoginBannerOptions](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions)" : {{ClientLoginBannerOptions}},
      "[ClientRouteEnforcementOptions](#cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions)" : {{ClientRouteEnforcementOptions}},
      "[ConnectionLogOptions](#cfn-ec2-clientvpnendpoint-connectionlogoptions)" : {{ConnectionLogOptions}},
      "[Description](#cfn-ec2-clientvpnendpoint-description)" : {{String}},
      "[DisconnectOnSessionTimeout](#cfn-ec2-clientvpnendpoint-disconnectonsessiontimeout)" : {{Boolean}},
      "[DnsServers](#cfn-ec2-clientvpnendpoint-dnsservers)" : {{[ String, ... ]}},
      "[EndpointIpAddressType](#cfn-ec2-clientvpnendpoint-endpointipaddresstype)" : {{String}},
      "[SecurityGroupIds](#cfn-ec2-clientvpnendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[SelfServicePortal](#cfn-ec2-clientvpnendpoint-selfserviceportal)" : {{String}},
      "[ServerCertificateArn](#cfn-ec2-clientvpnendpoint-servercertificatearn)" : {{String}},
      "[SessionTimeoutHours](#cfn-ec2-clientvpnendpoint-sessiontimeouthours)" : {{Integer}},
      "[SplitTunnel](#cfn-ec2-clientvpnendpoint-splittunnel)" : {{Boolean}},
      "[TagSpecifications](#cfn-ec2-clientvpnendpoint-tagspecifications)" : {{[ TagSpecification, ... ]}},
      "[TrafficIpAddressType](#cfn-ec2-clientvpnendpoint-trafficipaddresstype)" : {{String}},
      "[TransitGatewayConfiguration](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration)" : {{TransitGatewayConfiguration}},
      "[TransportProtocol](#cfn-ec2-clientvpnendpoint-transportprotocol)" : {{String}},
      "[VpcId](#cfn-ec2-clientvpnendpoint-vpcid)" : {{String}},
      "[VpnPort](#cfn-ec2-clientvpnendpoint-vpnport)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-ec2-clientvpnendpoint-syntax.yaml"></a>

```
Type: AWS::EC2::ClientVpnEndpoint
Properties:
  [AuthenticationOptions](#cfn-ec2-clientvpnendpoint-authenticationoptions): {{
    - ClientAuthenticationRequest}}
  [ClientCidrBlock](#cfn-ec2-clientvpnendpoint-clientcidrblock): {{String}}
  [ClientConnectOptions](#cfn-ec2-clientvpnendpoint-clientconnectoptions): {{
    ClientConnectOptions}}
  [ClientLoginBannerOptions](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions): {{
    ClientLoginBannerOptions}}
  [ClientRouteEnforcementOptions](#cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions): {{
    ClientRouteEnforcementOptions}}
  [ConnectionLogOptions](#cfn-ec2-clientvpnendpoint-connectionlogoptions): {{
    ConnectionLogOptions}}
  [Description](#cfn-ec2-clientvpnendpoint-description): {{String}}
  [DisconnectOnSessionTimeout](#cfn-ec2-clientvpnendpoint-disconnectonsessiontimeout): {{Boolean}}
  [DnsServers](#cfn-ec2-clientvpnendpoint-dnsservers): {{
    - String}}
  [EndpointIpAddressType](#cfn-ec2-clientvpnendpoint-endpointipaddresstype): {{String}}
  [SecurityGroupIds](#cfn-ec2-clientvpnendpoint-securitygroupids): {{
    - String}}
  [SelfServicePortal](#cfn-ec2-clientvpnendpoint-selfserviceportal): {{String}}
  [ServerCertificateArn](#cfn-ec2-clientvpnendpoint-servercertificatearn): {{String}}
  [SessionTimeoutHours](#cfn-ec2-clientvpnendpoint-sessiontimeouthours): {{Integer}}
  [SplitTunnel](#cfn-ec2-clientvpnendpoint-splittunnel): {{Boolean}}
  [TagSpecifications](#cfn-ec2-clientvpnendpoint-tagspecifications): {{
    - TagSpecification}}
  [TrafficIpAddressType](#cfn-ec2-clientvpnendpoint-trafficipaddresstype): {{String}}
  [TransitGatewayConfiguration](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration): {{
    TransitGatewayConfiguration}}
  [TransportProtocol](#cfn-ec2-clientvpnendpoint-transportprotocol): {{String}}
  [VpcId](#cfn-ec2-clientvpnendpoint-vpcid): {{String}}
  [VpnPort](#cfn-ec2-clientvpnendpoint-vpnport): {{Integer}}
```

## Properties
<a name="aws-resource-ec2-clientvpnendpoint-properties"></a>

`AuthenticationOptions`  <a name="cfn-ec2-clientvpnendpoint-authenticationoptions"></a>
Information about the authentication method to be used to authenticate clients.
*Required*: Yes
*Type*: Array of [ClientAuthenticationRequest](aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientCidrBlock`  <a name="cfn-ec2-clientvpnendpoint-clientcidrblock"></a>
The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. Client CIDR range must have a size of at least /22 and must not be greater than /12.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientConnectOptions`  <a name="cfn-ec2-clientvpnendpoint-clientconnectoptions"></a>
The options for managing connection authorization for new client connections.
*Required*: No
*Type*: [ClientConnectOptions](aws-properties-ec2-clientvpnendpoint-clientconnectoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientLoginBannerOptions`  <a name="cfn-ec2-clientvpnendpoint-clientloginbanneroptions"></a>
Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
*Required*: No
*Type*: [ClientLoginBannerOptions](aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientRouteEnforcementOptions`  <a name="cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions"></a>
Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.
Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.
*Required*: No
*Type*: [ClientRouteEnforcementOptions](aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionLogOptions`  <a name="cfn-ec2-clientvpnendpoint-connectionlogoptions"></a>
Information about the client connection logging options.
If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:
+ Client connection requests
+ Client connection results (successful and unsuccessful)
+ Reasons for unsuccessful client connection requests
+ Client connection termination time
*Required*: Yes
*Type*: [ConnectionLogOptions](aws-properties-ec2-clientvpnendpoint-connectionlogoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-clientvpnendpoint-description"></a>
A brief description of the Client VPN endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisconnectOnSessionTimeout`  <a name="cfn-ec2-clientvpnendpoint-disconnectonsessiontimeout"></a>
Indicates whether the client VPN session is disconnected after the maximum `sessionTimeoutHours` is reached. If `true`, users are prompted to reconnect client VPN. If `false`, client VPN attempts to reconnect automatically. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsServers`  <a name="cfn-ec2-clientvpnendpoint-dnsservers"></a>
Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address configured on the device is used for the DNS server.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointIpAddressType`  <a name="cfn-ec2-clientvpnendpoint-endpointipaddresstype"></a>
The IP address type of the Client VPN endpoint. Possible values are `ipv4` for IPv4 addressing only, `ipv6` for IPv6 addressing only, or `dual-stack `for both IPv4 and IPv6 addressing.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dual-stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-ec2-clientvpnendpoint-securitygroupids"></a>
The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that contains the security groups.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfServicePortal`  <a name="cfn-ec2-clientvpnendpoint-selfserviceportal"></a>
Specify whether to enable the self-service portal for the Client VPN endpoint.
Default Value: `enabled`
*Required*: No
*Type*: String
*Allowed values*: `enabled | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerCertificateArn`  <a name="cfn-ec2-clientvpnendpoint-servercertificatearn"></a>
The ARN of the server certificate. For more information, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionTimeoutHours`  <a name="cfn-ec2-clientvpnendpoint-sessiontimeouthours"></a>
The maximum VPN session duration time in hours.
Valid values: `8 | 10 | 12 | 24`
Default value: `24`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SplitTunnel`  <a name="cfn-ec2-clientvpnendpoint-splittunnel"></a>
Indicates whether split-tunnel is enabled on the AWS Client VPN endpoint.
By default, split-tunnel on a VPN endpoint is disabled.
For information about split-tunnel VPN endpoints, see [Split-tunnel AWS Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the *AWS Client VPN Administrator Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagSpecifications`  <a name="cfn-ec2-clientvpnendpoint-tagspecifications"></a>
The tags to apply to the Client VPN endpoint during creation.
*Required*: No
*Type*: Array of [TagSpecification](aws-properties-ec2-clientvpnendpoint-tagspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficIpAddressType`  <a name="cfn-ec2-clientvpnendpoint-trafficipaddresstype"></a>
The IP address type of the Client VPN endpoint. Possible values are either `ipv4` for IPv4 addressing only, `ipv6` for IPv6 addressing only, or `dual-stack` for both IPv4 and IPv6 addressing.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dual-stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayConfiguration`  <a name="cfn-ec2-clientvpnendpoint-transitgatewayconfiguration"></a>
The Transit Gateway configuration for the Client VPN endpoint.
*Required*: No
*Type*: [TransitGatewayConfiguration](aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransportProtocol`  <a name="cfn-ec2-clientvpnendpoint-transportprotocol"></a>
The transport protocol to be used by the VPN session.
Default value: `udp`
*Required*: No
*Type*: String
*Allowed values*: `tcp | udp`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-ec2-clientvpnendpoint-vpcid"></a>
The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the default security group for the VPC is applied.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpnPort`  <a name="cfn-ec2-clientvpnendpoint-vpnport"></a>
The port number to assign to the Client VPN endpoint for TCP and UDP traffic.
Valid Values: `443` \| `1194`
Default Value: `443`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-clientvpnendpoint-return-values"></a>

### Ref
<a name="aws-resource-ec2-clientvpnendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Client VPN endpoint ID. For example: `cvpn-endpoint-1234567890abcdef0`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-ec2-clientvpnendpoint--examples"></a>

### Client VPN endpoint
<a name="aws-resource-ec2-clientvpnendpoint--examples--Client_VPN_endpoint"></a>

The following example creates a Client VPN endpoint that uses Active Directory authentication and assigns client IP addresses from the `10.0.0.0/22` CIDR range.

#### YAML
<a name="aws-resource-ec2-clientvpnendpoint--examples--Client_VPN_endpoint--yaml"></a>

```
myClientVpnEndpoint:
  Type: AWS::EC2::ClientVpnEndpoint
  Properties:
    AuthenticationOptions:
    - Type: "directory-service-authentication"
      ActiveDirectory:
        DirectoryId: d-926example
    ClientCidrBlock: "10.0.0.0/22"
    ConnectionLogOptions:
      Enabled: false
    Description: "My Client VPN Endpoint"
    DnsServers:
      - "11.11.0.1"
    SecurityGroupIds:
      - !Ref mySecurityGroup
    ServerCertificateArn: "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"
    TagSpecifications:
      - ResourceType: "client-vpn-endpoint"
        Tags:
        - Key: "Purpose"
          Value: "Production"
    TransportProtocol: "udp"
```

#### JSON
<a name="aws-resource-ec2-clientvpnendpoint--examples--Client_VPN_endpoint--json"></a>

```
"myClientVpnEndpoint": {
    "Type": "AWS::EC2::ClientVpnEndpoint",
    "Properties": {
        "AuthenticationOptions": [
            {
                "Type": "directory-service-authentication",
                "ActiveDirectory": {
                    "DirectoryId": "d-926example"
                }
            }
        ],
        "ClientCidrBlock": "10.0.0.0/22",
        "ConnectionLogOptions": {
            "Enabled": false
        },
        "Description": "My Client VPN Endpoint",
        "DnsServers": [
            "11.11.0.1"
        ],
        "SecurityGroupIds": [
            {
                "Ref": "mySecurityGroup"
            }
        ],
        "ServerCertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012",
        "TagSpecifications": [
            {
                "ResourceType": "client-vpn-endpoint",
                "Tags": [
                    {
                        "Key": "Purpose",
                        "Value": "Production"
                    }
                ]
            }
        ],
        "TransportProtocol": "udp"
    }
}
```

## See also
<a name="aws-resource-ec2-clientvpnendpoint--seealso"></a>
+ [ Getting Started with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html) in the *AWS Client VPN Administrator Guide*
+ [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html) in the *AWS Client VPN Administrator Guide*
