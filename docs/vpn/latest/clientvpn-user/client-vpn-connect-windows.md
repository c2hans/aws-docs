---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-windows.html
---

# AWS Client VPN for Windows
<a name="client-vpn-connect-windows"></a>

These sections describe how to establish a VPN connection using the AWS provided client for Windows x64 and Windows Arm64 systems. You can download and install the client at [AWS Client VPN download](https://aws.amazon.com/vpn/client-vpn-download/). The AWS provided client does not support automatic updates.

## Requirements
<a name="client-vpn-connect-windows-req"></a>

The AWS provided client supports both Windows x64 and Arm64 systems. The following is required for each operating system:

**Windows Arm64 operating systems**
+ Windows 11 (64-bit operating system, Arm64 processor)
+ .NET Framework 4.8.1 or higher

**Note**
This application includes background processes that utilize Arm64 emulation. This is fully supported and enabled by default on Windows 11 Arm64 devices, ensuring seamless operation without any additional setup required. For more information, see [How emulation works on Arm](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation).

**Windows x64 operating systems**
+ Windows 11 (64-bit operating system, x64 processor)
+ .NET Framework 4.7.2 or higher

**Note**
For both Windows x64 and Arm64 operating systems, Client VPN endpoints that use SAML-based federated authentication (single sign-on), the client reserves TCP ports 8096-8115 on your computer.

Before you begin, ensure that your Client VPN administrator has [created a Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html#cvpn-working-endpoint-create) and provided you with the [Client VPN endpoint configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html). If you want to connect to multiple profiles simultaneously, you'll need a configuration file for each profile.

**Topics**
+ [Requirements](#client-vpn-connect-windows-req)
+ [Connect using the client](client-vpn-connect-windows-connecting-how.md)
+ [Release notes](client-vpn-connect-windows-release-notes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
