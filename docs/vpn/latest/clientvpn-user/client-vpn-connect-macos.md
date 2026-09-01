---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-macos.html
---

# AWS Client VPN for macOS
<a name="client-vpn-connect-macos"></a>

These sections describe how to establish a VPN connection using the AWS provided client for macOS. You can download and install the client at [AWS Client VPN download](https://aws.amazon.com/vpn/client-vpn-download/). The AWS provided client does not support automatic updates.

## Requirements
<a name="client-vpn-connect-macos-req"></a>

To use the AWS provided client for macOS, the following is required:
+ macOS Sonoma (14.0), Sequoia (15.0), or Tahoe (26.0)
+ x86\_64 or ARM64 processor compatible.
+ For Client VPN, endpoints that use SAML-based federated authentication (single sign-on), The client reserves TCP ports 8096-8115 on your computer.
+ Endpoint security software might require exclusions to allow the AWS provided client to function. For more information, see [Endpoint security software compatibility](client-vpn-connect-endpoint-security.md).

For instructions on using the client, see [Connect using the AWS provided client](client-vpn-connect-how.md).

**Topics**
+ [Requirements](#client-vpn-connect-macos-req)
+ [Release notes](client-vpn-connect-macos-release-notes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
