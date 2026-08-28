---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-port.html
---

# Troubleshooting AWS Client VPN: Client returns no available ports error — federated authentication
<a name="client-no-port"></a>

**Problem**
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software returns the following error:

```
The authentication flow could not be initiated. There are no available ports.
```

**Cause**
The AWS provided client requires the use of TCP port 35001 to complete authentication. For more information, see [Requirements and considerations for SAML-based federated authentication](federated-authentication.md#saml-requirements).

**Solution**
Verify that the client's device is not blocking TCP port 35001 or is using it for a different process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
