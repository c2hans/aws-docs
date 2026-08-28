---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp02.html
---

# EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting your AWS EUC services
<a name="eucperf01-bp02"></a>

 Within each Region, only select Availability Zones support each AWS EUC service. This is important if you are architecting solutions with extreme performance or security requirements that demand that applications and desktops reside on the same subnet as the user data they need to access.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-1"></a>

 For the WorkSpaces service line, explore the Availability Zone information.
+  [Amazon WorkSpaces Availability Zone Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html)
+  [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html)

 For WorkSpaces Applications, selecting a subnet when creating a new fleet automatically checks if the associated Availability Zone can support the requested requirements, which are based on several criteria such as instance type and availability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
