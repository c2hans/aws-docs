---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network-manual-enable-internet-access.html
---

# Enable Internet Access for WorkSpaces Pools
<a name="managing-network-manual-enable-internet-access"></a>

After your NAT gateway is available on a VPC, you can enable internet access for your WorkSpaces Pools. You can enable internet access when you [create the WorkSpaces Pool directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-directory-pools.html). Choose the VPC with a NAT gateway when you create the directory. Then select a private subnet for **Subnet 1** and, optionally, another private subnet for **Subnet 2**. If you don't already have a private subnet in your VPC, you may need to create a second private subnet.

You can test your internet connectivity by starting your WorkSpaces Pool, and then connecting to a WorkSpace in the pool and browsing to the internet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
