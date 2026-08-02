---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/VPNTunnelConnectivityTroubleshooting.html
---

# Troubleshooting AWS Client VPN: Tunnel connectivity issues to a VPC
<a name="VPNTunnelConnectivityTroubleshooting"></a>

When experiencing connectivity issues with your AWS Client VPN connection, follow this systematic troubleshooting approach to identify and resolve the problem. This section provides step-by-step procedures to diagnose common Client VPN connectivity issues between remote clients and Amazon VPC resources.

**Topics**
+ [Network connectivity prerequisites](#NetworkConnectivityPrerequisites)
+ [Check Client VPN endpoint status](#CheckClientVPNEndpointStatus)
+ [Verify client connections](#VerifyClientConnections)
+ [Verify client authentication](#ClientAuthentication)
+ [Check authorization rules](#AuthorizationRules)
+ [Validate Client VPN routes](#ValidateClientVPNRoutes)
+ [Verify security groups and network ACLs](#SecurityGroupNACLVerification)
+ [Test client connectivity](#TestClientConnectivity)
+ [Diagnose the client device](#ClientSideDiagnostics)
+ [Troubleshoot DNS resolution](#DNSTroubleshooting)
+ [Troubleshoot performance](#PerformanceTroubleshooting)
+ [Monitor Client VPN metrics](#MonitorClientVPNMetrics)
+ [Check Client VPN logs](#CheckClientVPNLogs)
+ [Common issues and solutions](#CommonIssues)

## Network connectivity prerequisites
<a name="NetworkConnectivityPrerequisites"></a>

Before troubleshooting Client VPN connectivity, verify these network prerequisites:
+ Ensure the Client VPN endpoint subnet has internet connectivity (via Internet Gateway or NAT Gateway).
+ Verify that the Client VPN endpoint is associated with subnets in different Availability Zones for high availability.
+ Check that the VPC has sufficient IP address space and doesn't conflict with client CIDR blocks.
+ Confirm that target subnets have proper route table associations.

## Check Client VPN endpoint status
<a name="CheckClientVPNEndpointStatus"></a>

First, verify that your Client VPN endpoint is in the correct state:

1. Use the AWS CLI to check the Client VPN endpoint status:

   ```
   aws ec2 describe-client-vpn-endpoints --region {{your-region}}
   ```

1. Look for the endpoint state in the output. The state should be `available`.

1. Verify that the endpoint has associated target networks (subnets).

1. If the state is not `available`, check for any error messages or pending states that might indicate configuration issues.

## Verify client connections
<a name="VerifyClientConnections"></a>

Check the status of client connections to your Client VPN endpoint:

1. Check active client connections:

   ```
   aws ec2 describe-client-vpn-connections --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Review connection status and any error messages in the output.

1. Check client authentication logs for failed authentication attempts.

1. Verify that clients are receiving IP addresses from the configured client CIDR block.

**Note**
If clients cannot connect, the issue is likely with authentication configuration, authorization rules, or network connectivity.

## Verify client authentication
<a name="ClientAuthentication"></a>

Authentication issues are common causes of Client VPN connectivity problems:
+ For mutual authentication, ensure client certificates are valid and not expired.
+ For Active Directory authentication, verify user credentials and domain connectivity.
+ For SAML-based federated authentication, check IdP configuration and user permissions.
+ Review authentication logs in CloudWatch for detailed error information.
+ Verify that the authentication method configured on the endpoint matches the client configuration.

## Check authorization rules
<a name="AuthorizationRules"></a>

Authorization rules control which network resources clients can access:

1. List current authorization rules:

   ```
   aws ec2 describe-client-vpn-authorization-rules --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Verify that rules exist for the target networks clients need to access.

1. Check that the rules specify the correct Active Directory groups (if using AD authentication).

1. Ensure that authorization rules are in `active` state.

## Validate Client VPN routes
<a name="ValidateClientVPNRoutes"></a>

Proper routing configuration is essential for Client VPN connectivity:

1. Check Client VPN endpoint routes:

   ```
   aws ec2 describe-client-vpn-routes --client-vpn-endpoint-id {{cvpn-endpoint-id}} --region {{your-region}}
   ```

1. Verify routes exist for target networks that clients need to access.

1. Check Amazon VPC route tables to ensure return traffic can reach the Client VPN endpoint:

   ```
   aws ec2 describe-route-tables --filters "Name=vpc-id,Values={{vpc-id}}" --region {{your-region}}
   ```

1. Verify that target network associations are configured correctly.

## Verify security groups and network ACLs
<a name="SecurityGroupNACLVerification"></a>

Security groups and network ACLs can block Client VPN traffic:

1. Check security groups for target EC2 instances:

   ```
   aws ec2 describe-security-groups --group-ids {{sg-xxxxxxxxx}} --region {{your-region}}
   ```

1. Verify inbound rules allow traffic from Client VPN CIDR block:
   + SSH (port 22) from Client VPN CIDR: `10.0.0.0/16`
   + HTTP (port 80) from Client VPN CIDR: `10.0.0.0/16`
   + HTTPS (port 443) from Client VPN CIDR: `10.0.0.0/16`
   + Custom application ports as needed

1. For Client VPN endpoint security group (if applicable), ensure it allows:
   + UDP port 443 (OpenVPN) from 0.0.0.0/0
   + All traffic outbound to VPC CIDR blocks

1. Check that network ACLs are not blocking the traffic. Network ACLs are stateless, so both inbound and outbound rules must be configured.

1. Verify both inbound and outbound rules for the specific traffic you're trying to send.

## Test client connectivity
<a name="TestClientConnectivity"></a>

Test connectivity from Client VPN clients to Amazon VPC resources:

1. From a connected Client VPN client, test connectivity to Amazon VPC resources:

   ```
   ping {{vpc-resource-ip}}
   traceroute {{vpc-resource-ip}}
   ```

1. Test specific application connectivity:

   ```
   telnet {{vpc-resource-ip}} {{port}}
   ```

1. Verify DNS resolution if using private DNS names:

   ```
   nslookup {{private-dns-name}}
   ```

1. Test connectivity to internet resources if split tunneling is enabled.

## Diagnose the client device
<a name="ClientSideDiagnostics"></a>

Perform these checks on the client device:

1. Verify client configuration file (.ovpn) contains correct settings:
   + Correct server endpoint URL
   + Valid client certificate and private key
   + Proper authentication method configuration

1. Check client logs for connection errors:
   + Windows: Event Viewer → Applications and Services Logs → OpenVPN
   + macOS: Console app, search for "Tunnelblick" or "OpenVPN"
   + Linux: `/var/log/openvpn/` or systemd journal

1. Test basic network connectivity from client:

   ```
   ping 8.8.8.8
   nslookup {{cvpn-endpoint-id}}.cvpn.{{region}}.amazonaws.com
   ```

## Troubleshoot DNS resolution
<a name="DNSTroubleshooting"></a>

DNS issues can prevent access to resources using private DNS names:

1. Check if DNS servers are configured in the Client VPN endpoint:

   ```
   aws ec2 describe-client-vpn-endpoints --client-vpn-endpoint-ids {{cvpn-endpoint-id}} --query 'ClientVpnEndpoints[0].DnsServers'
   ```

1. Test DNS resolution from client:

   ```
   nslookup {{private-resource.internal}}
   dig {{private-resource.internal}}
   ```

1. Verify Route 53 Resolver rules if using custom DNS resolution.

1. Check that security groups allow DNS traffic (UDP/TCP port 53) from Client VPN CIDR to DNS servers.

## Troubleshoot performance
<a name="PerformanceTroubleshooting"></a>

Address performance issues with Client VPN connections:
+ Monitor bandwidth utilization using CloudWatch metrics for ingress/egress bytes.
+ Check for packet loss using continuous ping tests from clients.
+ Verify that Client VPN endpoint is not hitting connection limits.
+ Consider using multiple Client VPN endpoints for load distribution.
+ Test with different client locations to identify regional performance issues.

## Monitor Client VPN metrics
<a name="MonitorClientVPNMetrics"></a>

Monitor Client VPN endpoint metrics using CloudWatch:

1. Check active connection metrics:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace AWS/ClientVPN \
     --metric-name ActiveConnectionsCount \
     --dimensions Name=Endpoint,Value={{cvpn-endpoint-id}} \
     --start-time {{start-time}} \
     --end-time {{end-time}} \
     --period 300 \
     --statistics Average
   ```

1. Review authentication failure metrics:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace AWS/ClientVPN \
     --metric-name AuthenticationFailures \
     --dimensions Name=Endpoint,Value={{cvpn-endpoint-id}} \
     --start-time {{start-time}} \
     --end-time {{end-time}} \
     --period 300 \
     --statistics Sum
   ```

1. Review other available metrics such as ingress and egress bytes and packets.

## Check Client VPN logs
<a name="CheckClientVPNLogs"></a>

Client VPN connection logs provide detailed information about connection attempts and errors:
+ Enable Client VPN connection logging if not already configured.
+ Review CloudWatch logs for connection attempts, authentication failures, and authorization errors.
+ Look for specific error codes and messages that indicate the root cause of connectivity issues.
+ Check for patterns in failed connections that might indicate configuration problems.

## Common issues and solutions
<a name="CommonIssues"></a>

Common issues that can affect Client VPN connectivity:

Authentication failures
Client certificates expired or invalid, or Active Directory credentials incorrect. Verify authentication configuration and credential validity.

Missing authorization rules
Clients cannot access target networks due to missing or incorrect authorization rules. Add appropriate authorization rules for the required networks.

Split tunneling issues
Traffic routing incorrectly due to split tunneling configuration. Review and adjust split tunneling settings as needed.

Client IP pool exhaustion
No available IP addresses in the client CIDR block. Expand the client CIDR range or disconnect unused clients.

MTU issues
Large packets are being dropped due to MTU size limitations. Try setting the MTU to 1436 bytes or enable Path MTU Discovery on client devices.

DNS resolution problems
Clients cannot resolve private DNS names. Verify DNS server configuration and ensure DNS traffic is allowed through security groups.

Overlapping IP ranges
Client CIDR blocks conflict with local network ranges. Check for and resolve any overlapping IP address ranges between client CIDR and local networks.

TLS handshake failures
Connection fails during TLS negotiation. Check certificate validity, ensure correct cipher suites, and verify that client and server certificates are properly configured.

Route propagation delays
New routes not immediately available to clients. Allow 1-2 minutes for route propagation after making changes to Client VPN routes.

Connection drops/instability
Frequent disconnections or unstable connections. Check for network congestion, firewall interference, or power management settings on client devices.
