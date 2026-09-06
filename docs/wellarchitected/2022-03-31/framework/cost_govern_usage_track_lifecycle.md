---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_govern_usage_track_lifecycle.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST02-BP06 Track project lifecycle
<a name="cost_govern_usage_track_lifecycle"></a>

 Track, measure, and audit the lifecycle of projects, teams, and environments to avoid using and paying for unnecessary resources.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Ensure that you track the entire lifecycle of the workload. This ensures that when workloads or workload components are no longer required, they can be decommissioned or modified. This is especially useful when you release new services or features. The existing workloads and components may appear to be in use, but should be decommissioned to redirect customers to the new service. Notice previous stages of workloads — after a workload is in production, previous environments can be decommissioned or greatly reduced in capacity until they are required again.

AWS provides a number of management and governance services you can use for entity lifecycle tracking. You can use [AWS Config](https://aws.amazon.com/config/) or [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to provide a detailed inventory of your AWS resources and configuration. It is recommended that you integrate with your existing project or asset management systems to keep track of active projects and products within your organization. Combining your current system with the rich set of events and metrics provided by AWS allows you to build a view of significant lifecycle events and proactively manage resources to reduce unnecessary costs.

Refer to the [Well-Architected Operational Excellence Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) for more details on implementing entity lifecycle tracking.

**Implementation steps**
+ ** Perform workload reviews: **As defined by your organizational policies, audit your existing projects. The amount of effort spent in the audit should be proportional to the approximate risk, value, or cost to the organization. Key areas to include in the audit would be risk to the organization of an incident or outage, value, or contribution to the organization (measured in revenue or brand reputation), cost of the workload (measured as total cost of resources and operational costs), and usage of the workload (measured in number of organization outcomes per unit of time). If these areas change over the lifecycle, adjustments to the workload are required, such as full or partial decommissioning.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Config](https://aws.amazon.com/config/)
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+  [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
+  [AWS multiple account billing strategy](https://aws.amazon.com/answers/account-management/aws-multi-account-billing-strategy/)
+  [Control access to AWS Regions using IAM policies](https://aws.amazon.com/blogs/security/easier-way-to-control-access-to-aws-regions-using-iam-policies/)
