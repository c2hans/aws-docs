---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops09-bp01.html
---

# EUCOPS09-BP01 Maintain an up to date matrix of all EUC service owners and quick access links to the support plans for each service
<a name="eucops09-bp01"></a>

 Amazon WorkSpaces and Amazon WorkSpaces Applications, although easier to implement and administer than traditional on-premises alternatives, still require specific knowledge to deploy, manage, and support. To simplify the process of routing issues to the right owners, you should be able to quickly identify the teams who are responsible for implementation and support along with clear support plans for each application being delivered, expediting time to resolution.

 Each application delivered by WorkSpaces or WorkSpaces Applications should have a formalized support plan with designated business and technical owners who are responsible for and involved in the deployment, maintenance, and support of each application and its dependent technology stacks.

 Each application set should have its own designated level of criticality, with associated SLAs that are clearly understood by the support teams involved. For disaster recovery purposes, the business should be able to identify relevant RTO and RPO parameters which each service should be engineered to accommodate so that critical business services can be delivered even under the most challenging circumstances.

 If you are delivering WorkSpaces or WorkSpaces Applications across multiple AWS Regions, verify that a support and escalation mechanism exists that documents the transfer of responsibility between regions when required. This documentation is important to sustain support efforts across time zones, maximizing service continuity.

 Note: Your business RPO and RTO requirements may be more aggressive than the service can provide, and discrete groups of users may have different RPO and RTO requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-9"></a>

 Create a process to quickly identify roles and responsibilities for each application stack so that support teams can quickly identify the resources that need to be employed and address any issues in service delivery.

## Resources
<a name="resources"></a>
+  [WorkSpaces Service Level Agreement](https://aws.amazon.com/workspaces/sla/)
+  [WorkSpaces Applications Service Level Agreement](https://aws.amazon.com/appstream2/sla/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
