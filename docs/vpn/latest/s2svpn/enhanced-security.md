---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/enhanced-security.html
---

# Enhanced AWS Site-to-Site VPN security features using Secrets Manager
<a name="enhanced-security"></a>

AWS Site-to-Site VPN's Security Rebase feature provides enhanced security capabilities that gives you greater control and visibility over your VPN connections. A key improvement is the ability to store pre-shared keys (PSKs) in AWS Secrets Manager rather than directly in the Site-to-Site VPN service, allowing for better secret management and compliance with security best practices. The feature also includes a `GetActiveVpnTunnelStatus` API that provides real-time visibility into the security parameters being used in active VPN tunnels, including encryption algorithms, integrity algorithms, and Diffie-Hellman groups for both IKE phases. Additionally, you can now generate recommended security configurations that enforce the use of modern protocols by excluding legacy options such as IKEv1. These enhancements are particularly valuable if your organization needs to maintain strict security standards, require detailed audit trails of your VPN configurations, or want to ensure your VPN connections are using the most secure protocols available.

**Topics**
+ [Change the Secrets Manager pre-shared key](enhanced-security-tunnel.md)
+ [Change the pre-shared key storage mode](enhanced-security-storage.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
