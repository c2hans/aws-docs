---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-credentials-exceeded.html
---

# Troubleshooting AWS Client VPN: Client returns a credentials exceed max size error in Client VPN — federated authentication
<a name="client-credentials-exceeded"></a>

**Problem**
I use federated authentication for my Client VPN endpoint. When clients enter their user name and password in the SAML-based identity provider (IdP) browser window, they get an error that the credentials exceed the maximum supported size.

**Cause**
The SAML response returned by the IdP exceeds the maximum supported size. For more information, see [Requirements and considerations for SAML-based federated authentication](federated-authentication.md#saml-requirements).

**Solution**
Try to reduce the number of groups that the user belongs to in the IdP, and try connecting again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
