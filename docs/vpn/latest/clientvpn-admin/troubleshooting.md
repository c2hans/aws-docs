---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/troubleshooting.html
---

# Troubleshooting AWS Client VPN
<a name="troubleshooting"></a>

The following sections can help you troubleshoot problems that you might have with a Client VPN endpoint.

For more information about troubleshooting OpenVPN-based software that clients use to connect to a Client VPN, see [Troubleshooting Your Client VPN Connection](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/troubleshooting.html) in the *AWS Client VPN User Guide*.

**Topics**
+ [Unable to resolve the Client VPN endpoint DNS name](resolve-host-name.md)
+ [Traffic is not being split between subnets](split-traffic.md)
+ [Authorization rules for Active Directory groups not working as expected](ad-group-auth-rules.md)
+ [Clients can't access a peered VPC, Amazon S3, or the internet](no-internet-access.md)
+ [Access to a peered VPC, Amazon S3, or the internet is intermittent](intermittent-access.md)
+ [Client software returns TLS error](client-cannot-connect.md)
+ [Client software returns user name and password errors — Active Directory authentication](client-user-name-password-mfa.md)
+ [Client software returns user name and password errors — federated authentication](missing-attribute.md)
+ [Clients cannot connect — mutual authentication](client-cannot-connect-mutual.md)
+ [Client returns a credentials exceed max size error — federated authentication](client-credentials-exceeded.md)
+ [Client does not open browser — federated authentication](client-no-browser.md)
+ [Client returns no available ports error — federated authentication](client-no-port.md)
+ [VPN connection terminated due to IP mismatch](server-ip-mismatch.md)
+ [Routing traffic to LAN not working as expected](routing-to-lan.md)
+ [Verify the bandwidth limit for an endpoint](test-throughput.md)
+ [Client VPN tunnel connectivity](VPNTunnelConnectivityTroubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
