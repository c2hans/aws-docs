---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp03.html
---

# EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections
<a name="eucperf06-bp03"></a>

 WorkSpaces Applications instances use a dedicated management network interface (eth0) for streaming and service management connections.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-17"></a>

 Do not configure applications or the operating system to interfere with the connections listed in [Amazon WorkSpaces Applications Connections to Your VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream2-port-requirements-appstream2.html#management_ports). If private network connectivity from WorkSpaces Applications instances to resources outside your VPC is required, use a VPC-level solution such as AWS Site-to-Site VPN or AWS Transit Gateway. Do not use a client VPN on the WorkSpaces Applications instance, as this is complex and error-prone to configure properly.

 WorkSpaces instances use a dedicated management network interface (eth0) for streaming and service management connections.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
