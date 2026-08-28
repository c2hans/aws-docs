---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-auth-rule-create.html
---

# Create an AWS Client VPN endpoint security group rule
<a name="client-auth-rule-create"></a>

The default security group for the VPC applied when you associate a subnet with a Client VPN might restrict traffic from the default security group traffic that you want to allow, while simultaneously allowing traffic that you don't want. Use the following steps to create a Client VPN endpoint security group rule that either allows or restricts traffic for an endpoint security group associated with a resource or application. For more information about security group rules, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

**To add a rule that allows traffic from the Client VPN endpoint security group**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security Groups**.

1. Choose the security group that's associated with your resource or application, and choose **Actions**, **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Type**, choose **All traffic**. Alternatively, you can restrict access to a specific type of traffic, for example, **SSH**.

   For **Source**, specify the ID of the security group that's associated with the target network (subnet) for the Client VPN endpoint.

1. Choose **Save rules**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
