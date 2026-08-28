---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec10-bp01.html
---

# EUCSEC10-BP01 Implement network separation for AWS EUC instances
<a name="eucsec10-bp01"></a>

 Separating end user systems from infrastructure, application servers, and data at the network level verifies that you can enforce minimal access between systems to help prevent unauthorized access to data and applications.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-30"></a>

 Enforce network separation between user instances and other services. EUC instances provided by Amazon WorkSpaces or WorkSpaces Applications usually have network connectivity to other workloads in the same network subnet. The use of security groups within VPCs can restrict lateral movement and are recommended for implementation. For defense-in-depth, non-end user instances such as application servers, authentication providers, and other infrastructure services should reside on subnets different to those where user instances reside.

 You can apply security controls to the non-end user instances at various points using AWS capabilities, such as separate AWS accounts and VPCs, VPC endpoints, proxy servers, and network firewalls. Review network security best practices for [WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf) and [AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html) to improve security posture in your EUC environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
