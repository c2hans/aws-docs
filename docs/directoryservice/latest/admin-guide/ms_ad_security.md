---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_security.html
---

# Secure your AWS Managed Microsoft AD
<a name="ms_ad_security"></a>

You can use password policies, features like multi-factor authentication (MFA), and settings to secure your AWS Managed Microsoft AD. Ways you can secure your directory include:
+ [Understand how the password policies in Active Directory works](ms_ad_password_policies.md) so they can be applied to AWS Managed Microsoft AD users. You can also delegate which user can manage your AWS Managed Microsoft AD password policies.
+ [Enable MFA](ms_ad_mfa.md) which increases your AWS Managed Microsoft AD security.
+ [>Enable Lightweight Directory Access Protocol over Secure Socket Layer (SSL)/Transport Layer Security (TLS) (LDAPS)](ms_ad_ldap.md) so that communications over LDAP are encrypted and improves security.
+ [Manage your AWS Managed Microsoft AD compliance](ms_ad_compliance.md) with standards like Federal Risk and Authorization Management Program (FedRAMP) and Payment Card Industry (PCI) Data Security Standard (DSS).
+ [Enhance your AWS Managed Microsoft AD network security configuration>](ms_ad_network_security.md) by modifying AWS Security Group to meet your environment needs.
+ [Edit your AWS Managed Microsoft AD directory security settings](ms_ad_directory_settings.md) like Certificate Base Authentication, Secure Channel Cipher and Protocol to meet your needs.
+ [Set up AWS Private Certificate Authority Connector for AD](ms_ad_pca_connector.md) so you can issue and manage certificates for your AWS Managed Microsoft AD with AWS Private CA.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
