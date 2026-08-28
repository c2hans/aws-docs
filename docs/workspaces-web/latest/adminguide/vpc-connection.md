---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-connection.html
---

# Internet connectivity ports for Amazon WorkSpaces Secure Browser
<a name="vpc-connection"></a>

Each WorkSpaces Secure Browser streaming instance has a customer network interface that provides connectivity to the resources within your VPC, as well as to the internet if private subnets with NAT gateway are set up.

For internet connectivity, the following ports must be open to all destinations. If you are using a modified or custom security group, you'll need to add the required rules manually. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules.html).

**Note**
This applies to egress traffic.
+ TCP 80 (HTTP)
+ TCP 443 (HTTPS)
+ UDP 8433

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
