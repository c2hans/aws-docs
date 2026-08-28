---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/deleting-tls-configuration.html
---

# Deleting a TLS inspection configuration in Network Firewall
<a name="deleting-tls-configuration"></a>

To delete a TLS inspection configuration, perform the following procedure.

**Deleting a TLS inspection configuration**
When you delete a TLS inspection configuration, AWS Network Firewall checks to see if it's currently being referenced in a firewall policy. If it is, Network Firewall sends you a warning, and doesn't delete the TLS inspection configuration. Network Firewall is almost always able to determine whether a resource is being referenced, however, in rare cases it might not be able to do so. To be sure that the resource that you want to delete isn't in use, check all of your firewall policies before deleting it. TLS inspection configurations referenced in firewall policies can't be deleted.

**To delete a TLS inspection configuration**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **TLS inspection configurations**.

1. In the **TLS inspection configuration** page, select the TLS inspection configuration that you want to delete.

1. Choose **Delete**, and confirm your request.

Your TLS inspection configuration is removed from the list in the **TLS inspection configuration** page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
