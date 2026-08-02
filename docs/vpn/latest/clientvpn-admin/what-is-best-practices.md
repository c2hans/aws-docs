---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is-best-practices.html
---

# Rules and best practices for using AWS Client VPN
<a name="what-is-best-practices"></a>

The following sections describe the rules and best practices for using AWS Client VPN:

**Topics**
+ [Networking and bandwidth requirements](#bp-nw)
+ [Subnet and VPC configuration](#bp-subnet)
+ [Authentication and security](#bp-auth)
+ [Connection and DNS requirements](#bp-dns)
+ [Limitations and restrictions](#bp-limits)

## Networking and bandwidth requirements
<a name="bp-nw"></a>
+ AWS Client VPN is a fully-managed service that automatically scales to accommodate additional user connections and bandwidth requirements. Each user connection has a maximum baseline bandwidth of 50 Mbps.

  The actual bandwidth you experience connecting through a Client VPN endpoint can vary based on several factors. These factors include packet size, traffic composition (TCP/UDP mix), network policies (shaping or throttling) on intermediate networks, internet conditions, application-specific requirements, and the total number of concurrent user connections. If you are hitting the maximum bandwidth limit, you can request an increase through AWS Support.
+ Client CIDR ranges cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or any routes manually added to the Client VPN endpoint's route table.
+ Client CIDR ranges must have a block size of at least /22 and must not be greater than /12.
+ A portion of the addresses in the client CIDR range are used to support the availability model of the Client VPN endpoint, and cannot be assigned to clients. Therefore, we recommend that you assign a CIDR block that contains twice the number of IP addresses that are required to enable the maximum number of concurrent connections that you plan to support on the Client VPN endpoint.
+ The client CIDR range cannot be changed after you create the Client VPN endpoint.
+ Client VPN supports IPv4, IPv6, and dual-stack (both IPv4 and IPv6) traffic. For more details on IPv6 support, see [IPv6 considerations for AWS Client VPNIPv6 considerations](ipv6-considerations.md).
+
  + The source IP address is translated to the Client VPN endpoint's IP address.
  + The original source port number from the client remains unchanged.
+ Client VPN performs Port Address Translation (PAT) only when concurrent users are connecting to the same target. Port translation is automatic and necessary to support multiple simultaneous connections through the same VPN endpoint.
  + For the source IP translation the source IP address is translated to the Client VPN's IP address.
  + For the source port translation for single client connections, the original source port number might remain unchanged.
  + For the source port translation for multiple clients connecting to the same destination (the same target IP address and port), Client VPN performs port translation to ensure unique connections.

  For example, when two clients, client 1 and client 2, connect to the same destination server and port through a Client VPN endpoint:
  + The original port for client 1 — for example, `9999` — might be translated to a different port — for example, port `4306`.
  + The original port for client 2 — for example, `9999` — might be translated to a unique port different form client 1 — for example, port `63922`.
+ For IPv6 traffic, Client VPN does not perform Network Address Translation (NAT). This provides enhanced visibility into the connected user's IPv6 address.

## Subnet and VPC configuration
<a name="bp-subnet"></a>
+ The subnets associated with a Client VPN endpoint must be in the same VPC.
+ You cannot associate multiple subnets from the same Availability Zone with a Client VPN endpoint.
+ A Client VPN endpoint does not support subnet associations in a dedicated tenancy VPC.
+ For IPv6 or dual-stack traffic, the associated subnets must have IPv6 or dual-stack CIDR ranges.
+ For dual-stack endpoints, you cannot associate more than one subnet per Availability Zone.

## Authentication and security
<a name="bp-auth"></a>
+ The self-service portal is not available for clients that authenticate using mutual authentication.
+ If multi-factor authentication (MFA) is disabled for your Active Directory, user passwords cannot use the following format.

  ```
  SCRV1:{{base64_encoded_string}}:{{base64_encoded_string}}
  ```
+ Certificates used in AWS Client VPN must adhere to [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://datatracker.ietf.org/doc/html/rfc5280), including the Certificate Extensions specified in section 4.2 of the memo.
+ User names with special characters might cause connection errors.
+ The maximum username length is 1024 bytes. Connections with longer usernames will be rejected.

## Connection and DNS requirements
<a name="bp-dns"></a>
+ We do not recommend connecting to a Client VPN endpoint using IP addresses. Because Client VPN is a managed service, you will occasionally see changes in the IP addresses to which the DNS name resolves. In addition, you will see Client VPN network interfaces deleted and recreated in your CloudTrail logs. We recommend connecting to the Client VPN endpoint using the DNS name provided.
+ The Client VPN service requires that the IP address the client is connected to matches the IP that the Client VPN endpoint's DNS name resolves to. In other words, if you set a custom DNS record for the Client VPN endpoint, then forward the traffic to the actual IP address the endpoint's DNS name resolves to, this setup will not work using recent AWS provided clients. This rule was added to mitigate a server IP attack as described here: [TunnelCrack](https://tunnelcrack.mathyvanhoef.com/).
+ You can use an AWS provided client to connect to multiple concurrent DNS sessions. However, for name resolution to work correctly, the DNS servers of all connections should have synchronized records.
+ The Client VPN service requires that the local area network (LAN) IP address ranges of client devices be within the following standard private IP address ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, or `169.254.0.0/16`. If the client LAN address range is detected to fall outside of the above ranges, the Client VPN endpoint will automatically push the OpenVPN directive "redirect-gateway block-local" to the client, forcing all LAN traffic into the VPN. Therefore, if you require LAN access during VPN connections, it is advised that you use the conventional address ranges listed above for your LAN. This rule is enforced to mitigate chances of a local net attack as described here: [TunnelCrack](https://tunnelcrack.mathyvanhoef.com/).
+ In Windows, when a full-tunnel endpoint is used, all DNS traffic is forced through the tunnel, regardless of the endpoint's IP address type (IPv4 IPv6, or dual stack). For DNS to function, a DNS server must be set up and reachable within the tunnel.

## Limitations and restrictions
<a name="bp-limits"></a>
+ IP forwarding is not currently supported when using the AWS Client VPN desktop application. IP forwarding is supported from other clients.
+ Client VPN does not support multi-Region replication in AWS Managed Microsoft AD. The Client VPN endpoint must be in the same Region as the AWS Managed Microsoft AD resource.
+ You can't establish a VPN connection from a computer if there are multiple users logged into the operating system.
+ Client-to-client communication is not supported for IPv6 clients. If an IPv6 client tries to communicate with another IPv6 client, the traffic will be dropped.
+ IPv6 and dual-stack endpoints require that user devices and internet service providers (ISPs) support the corresponding IP configuration.
