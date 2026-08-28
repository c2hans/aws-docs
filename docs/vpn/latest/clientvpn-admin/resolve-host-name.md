---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/resolve-host-name.html
---

# Troubleshooting AWS Client VPN: Unable to resolve the Client VPN endpoint DNS name
<a name="resolve-host-name"></a>

**Problem**
I am unable to resolve the Client VPN endpoint's DNS name.

**Cause**
The Client VPN endpoint configuration file includes a parameter called `remote-random-hostname`. This parameter forces the client to prepend a random string to the DNS name to prevent DNS caching. Some clients do not recognize this parameter and therefore, they do not prepend the required random string to the DNS name.

**Solution**
Open the Client VPN endpoint configuration file using your preferred text editor. Locate the line that specifies the Client VPN endpoint DNS name, and prepend a random string to it so that the format is {{random\_string.displayed\_DNS\_name}}. For example:
+ Original DNS name: `cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`
+ Modified DNS name: `asdfa.cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
