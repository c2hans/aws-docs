---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html
---

# AWS Client VPN endpoints
<a name="cvpn-working-endpoints"></a>

All AWS Client VPN sessions establish communication with a Client VPN endpoint. You can manage the Client VPN endpoint to create, modify, view, and delete client VPN sessions with that endpoint. Endpoints can be created and modified using either the Amazon VPC Console or by using the AWS CLI.

## Requirements for creating Client VPN endpoints
<a name="cvpn-working-create-req"></a>

**Important**
A Client VPN endpoint must be created in the same AWS account in which the intended target network is provisioned. You'll also need to generate a server certificate, and if required, a client certificate. For more information, see [Client authentication in AWS Client VPN](client-authentication.md).

Before you begin, ensure that you do the following:
+ Review the rules and limitations in [Rules and best practices for using AWS Client VPN](what-is-best-practices.md).
+ Generate the server certificate, and if required, the client certificate. For more information, see [Client authentication in AWS Client VPN](client-authentication.md).

## IP address types
<a name="cvpn-ip-address-types"></a>

AWS Client VPN supports IPv4-only, IPv6-only, and dual-stack configurations for both endpoint connectivity and traffic routing. The following guidance helps you select the appropriate IP address type based on your client device capabilities, network infrastructure, and application requirements.

### Endpoint address type
<a name="cvpn-endpoint-types"></a>

The endpoint address type determines which IP protocols your Client VPN endpoint supports for client connections. This setting cannot be changed after endpoint creation.

**Choose IPv4-only when:**
+ Your client devices only support IPv4 VPN connections
+ Your security tools are optimized for IPv4 traffic inspection

**Choose IPv6-only when:**
+ All client devices fully support IPv6 connections
+ You're in networks where IPv4 addresses are depleted

**Choose dual-stack when:**
+ You have a mix of client devices with varying IP capabilities
+ You're gradually transitioning from IPv4 to IPv6

### Traffic IP address type
<a name="cvpn-traffic-ip-considerations"></a>

The traffic IP address type controls how Client VPN routes traffic between clients and your VPC resources, independent of the endpoint's supported protocols.

**Route traffic as IPv4 when:**
+ Target applications in your VPC only support IPv4
+ You have complex IPv4 security groups and network ACLs
+ You're connecting to legacy systems

**Route traffic as IPv6 when:**
+ Your VPC infrastructure is primarily IPv6
+ You want to future-proof your network architecture
+ You have modern applications built for IPv6

## Endpoint modification
<a name="cvpn-endpoints-modify-req"></a>

**Note**
Client VPN endpoints created using quickstart setup can be modified using the same procedures as endpoints created with standard setup. All configuration options are available regardless of the setup method used during creation.

After a Client VPN has been created, you can modify any of the following settings:
+ The description
+ The server certificate
+ The client connection logging options
+ The client connect handler option
+ The DNS servers
+ The split-tunnel option
+ Routes (when using the split-tunnel option)
+ Certificate Revocation List (CRL)
+ Authorization rules
+ The VPC and security group associations
+ The VPN port number
+ The self-service portal option
+ The maximum VPN session duration
+ Enable or disable automatic reconnection on session timeout
+ Enable or disable client login banner text
+ Client login banner text

**Note**
Modifications to Client VPN endpoints, including Certificate Revocation List (CRL) changes, will take effect up to 4 hours after a request is accepted by the Client VPN service.
You cannot modify the client IPv4 CIDR range, authentication options, client certificate or transport protocol after the Client VPN endpoint has been created.

When you modify any of the following parameters on a Client VPN endpoint, the connection resets:
+ The server certificate
+ The DNS servers
+ The split-tunnel option (turning support on or off)
+ Routes (when you use the split-tunnel option)
+  Certificate Revocation List (CRL)
+ Authorization rules
+ The VPN port number

**Topics**
+ [Requirements for creating Client VPN endpoints](#cvpn-working-create-req)
+ [IP address types](#cvpn-ip-address-types)
+ [Endpoint modification](#cvpn-endpoints-modify-req)
+ [Create an endpoint](cvpn-working-endpoint-create.md)
+ [View endpoints](cvpn-working-endpoint-view.md)
+ [Modify an endpoint](cvpn-working-endpoint-modify.md)
+ [Delete an endpoint](cvpn-working-endpoint-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
