---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-browser.html
---

# Troubleshooting AWS Client VPN: Client does not open browser for an endpoint — federated authentication
<a name="client-no-browser"></a>

**Problem**
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software does not open a browser window, and instead displays a user name and password popup window.

**Cause**
The configuration file that was provided to the clients does not contain the `auth-federate` flag.

**Solution**
[Export the latest configuration file](cvpn-working-endpoint-export.md), import it to the AWS provided client, and try connecting again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
