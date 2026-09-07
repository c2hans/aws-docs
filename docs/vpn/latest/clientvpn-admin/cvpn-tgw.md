---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-tgw.html
---

# Transit Gateway integration with Client VPN
<a name="cvpn-tgw"></a>

You can attach a Client VPN endpoint natively to a Transit Gateway for secure remote access to multiple VPCs, on-premises networks, and other resources connected to the Transit Gateway. This eliminates the need to create separate VPN endpoints for each VPC or manage complex routing through intermediate VPCs.

**Topics**
+ [Overview](#cvpn-tgw-overview)
+ [Benefits](#cvpn-tgw-benefits)
+ [How Transit Gateway integration works](#cvpn-tgw-how-it-works)
+ [Prerequisites](#cvpn-tgw-prerequisites)
+ [Create a Transit Gateway Client VPN endpoint](#cvpn-tgw-create)
+ [Manage routes](#cvpn-tgw-routes)
+ [Configure authorization](#cvpn-tgw-authorization)
+ [Manage Availability Zones](#cvpn-tgw-manage-azs)
+ [Cross-account Transit Gateway access](#cvpn-tgw-cross-account)
+ [Considerations and limitations](#cvpn-tgw-limitations)

## Overview
<a name="cvpn-tgw-overview"></a>

When you associate a Transit Gateway with a Client VPN endpoint, the connected VPN clients can access all the resources connected to the Transit Gateway if appropriate routes and authorization rules are configured in the Client VPN endpoint.

Transit Gateway-associated endpoints preserve the client source IP address. Source network address translation (SNAT) is not applied, which provides enhanced visibility into client traffic.

**Important**
You cannot mix VPC subnet associations and Transit Gateway associations in a single Client VPN endpoint. Choose one association type when you create the endpoint.

## Benefits
<a name="cvpn-tgw-benefits"></a>

Transit Gateway integration with Client VPN provides the following benefits:
+ **Simplified management** — Eliminate the need for separate VPN endpoints per VPC. No need to create intermediate VPCs solely for VPN termination.
+ **Centralized routing** — Leverage Transit Gateway as a central routing hub. Simplify route management across your network.
+ **Enhanced visibility** — Preserve client source IP addresses (no SNAT). Provides flow logs support for Client VPN.
+ **Scalability** — Easily add new VPCs to your Transit Gateway which can be accessed through Client VPN. Scale to support large remote workforces and business units.
+ **Centralized security** — Implement consistent security policies across all connected networks. Maintain comprehensive audit trails.

## How Transit Gateway integration works
<a name="cvpn-tgw-how-it-works"></a>

The following describes how Client VPN works with Transit Gateway:

1. **Endpoint creation** — You create a Client VPN endpoint and specify the Transit Gateway ID.

1. **Attachment creation** — AWS automatically creates a Transit Gateway attachment of type `client-vpn` for the endpoint.

1. **Availability Zone selection** — You specify which Availability Zones to use, or AWS selects 2 Availability Zones automatically.

1. **Route configuration** — You add routes to the Client VPN endpoint route table to direct client traffic to destination networks through the Transit Gateway.

1. **Client connection flow** — When a client connects, traffic flows from the client through the Client VPN endpoint to the Transit Gateway, and then to the destination network based on Transit Gateway route tables.

![Transit Gateway traffic flow with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-tgw-traffic-flow.png)

## Prerequisites
<a name="cvpn-tgw-prerequisites"></a>

Before you create a Transit Gateway-associated Client VPN endpoint, verify the following requirements.

Transit Gateway requirements
+ An existing Transit Gateway in the same Region as the Client VPN endpoint.
+ For cross-account access, the Transit Gateway must be shared with your account through AWS Resource Access Manager.
+ The Transit Gateway must have an IPv4 CIDR block assigned. If you plan to use IPv6 or dual-stack configuration, also assign an IPv6 CIDR block.

Network requirements
+ The client CIDR range must not overlap with the CIDR ranges of VPCs attached to the Transit Gateway.
+ The Availability Zones you select must be supported by the Transit Gateway.
+ Return routes must be configured in VPC route tables to direct traffic destined for the client CIDR range to the Transit Gateway.

Certificate requirements
+ A server certificate provisioned in AWS Certificate Manager (ACM) in the same Region as the Client VPN endpoint.
+ If you use mutual authentication, a client certificate provisioned in ACM.

## Create a Transit Gateway Client VPN endpoint
<a name="cvpn-tgw-create"></a>

You can create a Client VPN endpoint associated with a Transit Gateway by using the console or the AWS CLI.

**To create a Transit Gateway Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints** and then choose **Create Client VPN Endpoint**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the endpoint.

1. For **Traffic IP address type**, choose one of the following:
   + **IPv4** — Specify a client IPv4 CIDR range (for example, `10.0.0.0/22`).
   + **IPv6** — AWS automatically assigns the client IPv6 CIDR range.
   + **Dual stack** — Specify a client IPv4 CIDR range. AWS automatically assigns the client IPv6 CIDR range.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate provisioned in ACM.

1. Choose your authentication method. For more information, see [Client authentication in AWS Client VPN](client-authentication.md).

1. (Optional) For **Connection logging**, turn on **Enable log details on client connections** and specify the CloudWatch Logs log group and log stream.

1. For **Network Infrastructure**, choose **Transit Gateway**.

1. For **Transit Gateway ID**, select the Transit Gateway from the dropdown list.

1. (Optional) For **Availability Zones**, select up to 5 Availability Zones. If you do not select Availability Zones, AWS automatically selects 2.

1. (Optional) Configure additional settings such as DNS servers, transport protocol, split-tunnel, VPN port, session timeout, and login banner.

1. Choose **Create Client VPN endpoint**.

**Note**
After creation, the endpoint state is `pending-associate`. The Transit Gateway attachment is created automatically. Clients can connect after the attachment becomes available.

**To create a Transit Gateway Client VPN endpoint (AWS CLI)**
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command with the `--transit-gateway-id` parameter.

The following example creates a Client VPN endpoint with specific Availability Zones:

```
aws ec2 create-client-vpn-endpoint \
    --client-cidr-block 10.0.0.0/22 \
    --server-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
    --connection-log-options Enabled=false \
    --transit-gateway-id tgw-0a1b2c3d4e5f6EXAMPLE \
    --availability-zone-list us-east-1a us-east-1b us-east-1c
```

Example output:

```
{
    "ClientVpnEndpointId": "cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE",
    "Status": {
        "Code": "pending-associate"
    },
    "DnsName": "cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE.prod.clientvpn.us-east-1.amazonaws.com"
}
```

To let AWS automatically select 2 Availability Zones, omit the `--availability-zone-list` parameter:

```
aws ec2 create-client-vpn-endpoint \
    --client-cidr-block 10.0.0.0/22 \
    --server-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
    --connection-log-options Enabled=false \
    --transit-gateway-id tgw-0a1b2c3d4e5f6EXAMPLE
```

### Verify the Transit Gateway attachment
<a name="cvpn-tgw-verify"></a>

After you create the endpoint, verify that the Transit Gateway attachment was created.

**To verify the Transit Gateway attachment (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Attachments**.

1. Locate the attachment with **Resource type** = `client-vpn` and **Resource ID** matching your Client VPN endpoint ID.

1. Verify that the **State** is `available`.

**To verify the Transit Gateway attachment (AWS CLI)**
Use the [describe-transit-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-attachments.html) command.

```
aws ec2 describe-transit-gateway-attachments \
    --filters Name=transit-gateway-id,Values=tgw-0a1b2c3d4e5f6EXAMPLE Name=resource-type,Values=client-vpn
```

To view the Transit Gateway configuration for the endpoint, use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command:

```
aws ec2 describe-client-vpn-endpoints \
    --client-vpn-endpoint-ids cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE
```

The output includes a `TransitGatewayConfiguration` object with the Transit Gateway ID and associated Availability Zones.

## Manage routes
<a name="cvpn-tgw-routes"></a>

**Important**
For Transit Gateway-associated endpoints, you do not specify a target subnet ID when you create routes. Traffic is automatically directed through the Transit Gateway attachment.

**To add a route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Route table**, and then choose **Create route**.

1. For **Route destination**, enter the destination CIDR range (for example, `10.1.0.0/16` for a VPC or `0.0.0.0/0` for all traffic).

1. (Optional) For **Description**, enter a description for the route.

1. Choose **Create route**.

**To add a route (AWS CLI)**
Use the [create-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-route.html) command without the `--target-vpc-subnet-id` parameter.

```
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16
```

To add multiple routes, run the command for each destination CIDR range:

```
# Route to VPC 1
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16

# Route to VPC 2
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.2.0.0/16

# Route to on-premises network
aws ec2 create-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 192.168.0.0/16
```

**To delete a route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Route table**, select the route, and then choose **Delete route**.

1. Choose **Delete route** to confirm.

**To delete a route (AWS CLI)**
Use the [delete-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-route.html) command.

```
aws ec2 delete-client-vpn-route \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --destination-cidr-block 10.1.0.0/16
```

## Configure authorization
<a name="cvpn-tgw-authorization"></a>

**Important**
Security group-based authorization is not supported for Transit Gateway-associated Client VPN endpoints. You must use network-based authorization rules to control client access.

**To add an authorization rule (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Authorization rules**, and then choose **Add authorization rule**.

1. For **Destination network to enable access**, enter the destination CIDR range (for example, `10.1.0.0/16`).

1. For **Grant access to**, choose one of the following:
   + **Allow access to all users** — All authenticated clients can access the destination network.
   + **Allow access to users in a specific access group** — Enter the Active Directory group SID or IdP group name in **Access group ID**.

1. Choose **Add authorization rule**.

**To add an authorization rule (AWS CLI)**
Use the [authorize-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-client-vpn-ingress.html) command.

The following example authorizes all users to access the `10.1.0.0/16` network:

```
aws ec2 authorize-client-vpn-ingress \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --target-network-cidr 10.1.0.0/16 \
    --authorize-all-groups
```

The following example authorizes a specific Active Directory group:

```
aws ec2 authorize-client-vpn-ingress \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --target-network-cidr 10.1.0.0/16 \
    --access-group-id S-1-2-34-1234567890-1234567890-1234567890-1234
```

## Manage Availability Zones
<a name="cvpn-tgw-manage-azs"></a>

You can modify the Availability Zones for a Transit Gateway-associated Client VPN endpoint after creation.

**To add a single Availability Zone (AWS CLI)**
Use the [associate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-client-vpn-target-network.html) command with the `--availability-zone` parameter.

```
aws ec2 associate-client-vpn-target-network \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --availability-zone us-east-1c
```

**To remove a single Availability Zone (AWS CLI)**
First, use the [describe-client-vpn-target-networks](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-target-networks.html) command to find the association ID for the Availability Zone.

```
aws ec2 describe-client-vpn-target-networks \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE
```

Then use the [disassociate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-client-vpn-target-network.html) command with the association ID.

```
aws ec2 disassociate-client-vpn-target-network \
    --client-vpn-endpoint-id cvpn-endpoint-0a1b2c3d4e5f6EXAMPLE \
    --association-id cvpn-assoc-0a1b2c3d4e5f6EXAMPLE
```

## Cross-account Transit Gateway access
<a name="cvpn-tgw-cross-account"></a>

You can create a Client VPN endpoint associated with a Transit Gateway that is owned by a different AWS account. To do this, the Transit Gateway owner must share the Transit Gateway with your account through AWS Resource Access Manager.

Prerequisites
+ **Transit Gateway owner account** — An existing Transit Gateway and permissions to create resource shares in AWS Resource Access Manager.
+ **Client VPN endpoint account** — Permissions to create Client VPN endpoints and accept AWS Resource Access Manager resource shares.

In the Client VPN endpoint account, accept the resource share in the AWS Resource Access Manager console or by using the [accept-resource-share-invitation](https://docs.aws.amazon.com/cli/latest/reference/ram/accept-resource-share-invitation.html) command. After you accept the share, the Transit Gateway appears in the Transit Gateway ID dropdown when you create a Client VPN endpoint.

## Considerations and limitations
<a name="cvpn-tgw-limitations"></a>

Consider the following when you use Transit Gateway integration with Client VPN:
+ **Association restrictions**
  + You cannot mix VPC subnet associations and Transit Gateway associations in a single endpoint.
  + Each endpoint must use exclusively one association type.
+ **Security groups**
  + Security group-based authorization is not supported for Transit Gateway endpoints.
  + Use network-based authorization rules only.
+ **Route management**
  + Automatic route propagation from Transit Gateway is not supported.
  + You must manually define routes for destination networks.
+ **CIDR overlap**
  + Client VPN CIDR block should not overlap with other Transit Gateway attachments or Transit Gateway CIDR blocks.
  + Transit Gateway does not support overlapping CIDR ranges across attached VPCs.
+ **Regional limitation**
  + Client VPN endpoint and Transit Gateway must be in the same AWS Region.
  + Cross-region Transit Gateway peering is not supported for Client VPN.
+ **Availability Zones**
  + You can specify up to 5 Availability Zones per endpoint.
  + If not specified, AWS automatically assigns 2 Availability Zones.
  + All specified Availability Zones must be supported by both Client VPN and Transit Gateway.
+ **Return routing**
  + VPCs connected to the Transit Gateway must have return routes configured to route traffic destined for the Client VPN CIDR back to the Transit Gateway.
  + Without proper return routing, VPN clients cannot access resources in the VPCs.
    + **For IPv4**: The Client VPN CIDR is known at endpoint creation time.
    + **For IPv6**: You must describe the Transit Gateway route table to determine the IPv6 CIDR range assigned to the Client VPN endpoint (the largest CIDR range in the Transit Gateway Route Table associated with the Client VPN endpoint), as IPv6 client CIDR ranges are automatically assigned by AWS Client VPN.
+ **Connection and flow logs**
  + [Transit Gateway flow logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html) can be enabled to capture information about the IP traffic going to and from your Transit Gateways. [Client VPN connection logs](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html) can be enabled to capture information about Client VPN connection events.
  + You can correlate a Transit Gateway flow log event to a Client VPN connection by comparing a client IP and time stamp in a Transit Gateway flow log event to the same client IP and time period in the Client VPN connection logs.
+ **Internet connectivity**
  + To access the internet through Client VPN with Transit Gateway, without split tunnel, an attached VPC must have NAT configured.
    + **For IPv4**: Configure a NAT Gateway to replace Client VPN client IPs with a public IP address.
    + **For IPv6**: See [Centralized internet outbound traffic with IPv6](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/advanced-dual-stack-and-ipv6-only-network-designs.html#centralized-internet-outbound-traffic-with-ipv6).
