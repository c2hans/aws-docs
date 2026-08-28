---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/missing-attribute.html
---

# Troubleshooting AWS Client VPN: Client software returns user name and password errors — federated authentication
<a name="missing-attribute"></a>

**Problem**
Trying to log in with a user name and password with federated authentication and getting the error "The credentials received were incorrect. Contact your IT administrator."

**Cause**
This error can be caused by not having at least one attribute included in the SAML response from the IdP.

**Solution**
Make sure at least one attribute is included in the SAML response from the IdP. See [SAML-based IdP configuration resources](federated-authentication.md#saml-config-resources) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
