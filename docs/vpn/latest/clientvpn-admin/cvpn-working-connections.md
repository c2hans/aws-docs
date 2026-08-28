---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections.html
---

# AWS Client VPN client connections
<a name="cvpn-working-connections"></a>

AWS Client VPN connections are active VPN sessions that have been established by clients to a specific Client VPN endpoint as well as connections that had been terminated within the last 60 minutes for that endpoint. A connection is established when a client successfully connects to a Client VPN endpoint. Terminating a session ends that client connection to the Client VPN endpoint.

You can view and terminate Client VPN connections. Viewing connection information returns information such as the IP address assigned from the client CIDR block range, the endpoint ID, and timestamp. Terminating a session ends the specified VPN connection to the endpoint. Viewing and terminating sessions can be done using either the Amazon VPC Console or the AWS CLI. If you're unable to connect to the endpoint, and depending on the error, see [Troubleshooting AWS Client VPN](troubleshooting.md) for steps to take to resolve the issue.

**Topics**
+ [View client connections](cvpn-working-connections-view.md)
+ [Terminate a client connection](cvpn-working-connections-disassociate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
