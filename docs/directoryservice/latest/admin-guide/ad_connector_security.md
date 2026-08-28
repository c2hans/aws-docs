---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_security.html
---

# Secure your AD Connector directory
<a name="ad_connector_security"></a>

You can use features like multi-factor authentication (MFA), client-side Lightweight Directory Access Protocol over Secure Sockets Layer (SSL)/Transport Layer Security (TLS) (LDAPS), and AWS Private Certificate Authority to secure your AD Connector. Ways you can secure your AD Connector include:
+ Enable MFA which increases your AD Connector security.
+ Enable client-side Lightweight Directory Access Protocol over Secure Socket Layer (SSL)/Transport Layer Security (TLS) (LDAPS) so that communications over LDAP are encrypted and improves security.
+ Enable certificate-based mutual Transport Layer Security (mTLS) authentication with smart cards which allows users to authenticate in to Amazon Web Services through your Active Directory and AD Connector.
+ Update your AD Connector service account credentials.
+ Set up AWS Private CA Connector for AD so you can issue and manage certificates for your AD Connector.

**Topics**
+ [Enabling multi-factor authentication for AD Connector](ad_connector_mfa.md)
+ [Enabling client-side LDAPS using AD Connector](ad_connector_ldap_client_side.md)
+ [Enabling mTLS authentication in AD Connector for use with smart cards](ad_connector_clientauth.md)
+ [Updating your AD Connector service account credentials in AWS Management Console](ad_connector_update_creds.md)
+ [Set up AWS Private CA Connector for AD](ad_connector_pca_connector.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
