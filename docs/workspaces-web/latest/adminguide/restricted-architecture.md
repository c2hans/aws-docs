---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-architecture.html
---

# Restricted internet browsing architecture for Amazon WorkSpaces Secure Browser
<a name="restricted-architecture"></a>

The following is an example of a typical proxy setup in your VPC. The proxy Amazon EC2 instance is in public subnets and associated with Elastic IP, so they have access to internet. A network load balancer hosts an auto scaling group of proxy instances. This ensures that proxy instances can scale up automatically, and the network load balancer is the single proxy endpoint, which can be consumed by WorkSpaces Secure Browser sessions.

![WorkSpaces Secure Browser architecture](http://docs.aws.amazon.com/workspaces-web/latest/adminguide/images/restricted-internet-architecture.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
