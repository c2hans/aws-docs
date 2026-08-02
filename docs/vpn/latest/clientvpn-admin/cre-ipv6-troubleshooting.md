---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cre-ipv6-troubleshooting.html
---

# Troubleshoot IPv6 Client Route Enforcement
<a name="cre-ipv6-troubleshooting"></a>

If you encounter issues with IPv6 Client Route Enforcement, consider the following troubleshooting steps:

Verify client version
Ensure that you are using AWS VPN Client version 5.3.0 or higher, which is required for IPv6 Client Route Enforcement support.

Check endpoint configuration
Verify that the endpoint has Client Route Enforcement enabled and is configured for IPv6 or dual-stack traffic.

Examine client logs
Review the AWS VPN Client logs for any error messages related to IPv6 Client Route Enforcement. Look for entries containing "IPv6" and "Client Route Enforcement" or "CRM".

Inspect routing table
Use the appropriate command for your operating system to view the IPv6 routing table:
+ Windows: `netsh interface ipv6 show route`
+ macOS: `netstat -rn -f inet6`
+ Linux: `ip -6 route`

Check for conflicting routes
Look for any IPv6 routes that might conflict with the VPN routes. Pay special attention to routes with the same destination but different gateways.

Verify ISP IPv6 support
Ensure that your internet service provider (ISP) properly supports IPv6.

If you continue to experience issues with IPv6 Client Route Enforcement after trying these troubleshooting steps, contact AWS Support for further assistance.
