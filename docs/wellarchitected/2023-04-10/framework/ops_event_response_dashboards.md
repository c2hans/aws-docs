---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_event_response_dashboards.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP06 Communicate status through dashboards
<a name="ops_event_response_dashboards"></a>

 Provide dashboards tailored to their target audiences (for example, internal technical teams, leadership, and customers) to communicate the current operating status of the business and provide metrics of interest.

 You can create dashboards using [Amazon CloudWatch Dashboards](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views/) on customizable home pages in the CloudWatch console. Using business intelligence services such as [Quick](https://aws.amazon.com/quicksight/) you can create and publish interactive dashboards of your workload and operational health (for example, order rates, connected users, and transaction times). Create Dashboards that present system and business-level views of your metrics.

 **Common anti-patterns:**
+  Upon request, you run a report on the current utilization of your application for management.
+  During an incident, you are contacted every twenty minutes by a concerned system owner wanting to know if it is fixed yet.

 **Benefits of establishing this best practice:** By creating dashboards, you create self-service access to information helping your customers to informed themselves and determine if they need to take action.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Communicate status through dashboards: Provide dashboards tailored to their target audiences (for example, internal technical teams, leadership, and customers) to communicate the current operating status of the business and provide metrics of interest. Providing a self-service option for status information reduces the disruption of fielding requests for status by the operations team. Examples include Amazon CloudWatch dashboards, and AWS Health Dashboard.
  +  [CloudWatch dashboards create and use customized metrics views](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Quick](https://aws.amazon.com/quicksight/)
+  [CloudWatch dashboards create and use customized metrics views](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
