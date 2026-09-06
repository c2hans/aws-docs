---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/server-ip-mismatch.html
---

# Troubleshooting AWS Client VPN: A connection is terminated due to an IP mismatch
<a name="server-ip-mismatch"></a>

**Problem**
VPN connection terminated and the client software returns the following error: `"The VPN connection is being terminated due to a discrepancy between the IP address of the connected server and the expected VPN server IP. Please contact your network administrator for assistance in resolving this issue."`

**Cause**
The AWS provided client requires that the IP address that it is connected to matches the IP of the VPN server backing the Client VPN endpoint. For more information, see [Rules and best practices for using AWS Client VPN](what-is-best-practices.md).

**Solution**
Verify that there is no DNS proxy between the AWS provided client and the Client VPN endpoint.
