---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_operations_health_measure_ops_goals_kpis.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP01 Measure operations goals and KPIs with metrics
<a name="ops_operations_health_measure_ops_goals_kpis"></a>

 Obtain goals and KPIs that define operations success from your organization and determine that metrics reflect these. Set baselines as a point of reference and reevaluate regularly. Develop mechanisms to collect these metrics from teams for evaluation.

 **Desired outcome:**
+  The goals and KPIs for the organization's operations teams have been published and shared.
+  Metrics that reflect these KPIs are established. Examples may include:
  +  Ticket queue depth or average age of ticket
  +  Ticket count grouped by type of issue
  +  Time spent working issues with or without a standardized operating procedure (SOP)
  +  Amount of time spent recovering from a failed code push
  +  Call volume

 **Common anti-patterns:**
+  Deployment deadlines are missed because developers are pulled away to perform troubleshooting tasks. Development teams argue for more personnel, but cannot quantify how many they need because the time taken away cannot be measured.
+  A Tier 1 desk was set up to handle user calls. Over time, more workloads were added, but no headcount was allocated to the Tier 1 desk. Customer satisfaction suffers as call times increase and issues go longer without resolution, but management sees no indicators of such, preventing any action.
+  A problematic workload has been handed off to a separate operations team for upkeep. Unlike other workloads, this new one was not supplied with proper documentation and runbooks. As such, teams spend longer troubleshooting and addressing failures. However, there are no metrics documenting this, which makes accountability difficult.

 **Benefits of establishing this best practice:** Where workload monitoring shows the state of our applications and services, monitoring operations teams provide owners gain insight into changes among the consumers of those workloads, such as shifting business needs. Measure the effectiveness of these teams and evaluate them against business goals by creating metrics that can reflect the state of operations. Metrics can highlight support issues or identify when drifts occur away from a service level target.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Schedule time with business leaders and stakeholders to determine the overall goals of the service. Determine what the tasks of various operations teams should be and what challenges they could be approached with. Using these, brainstorm key performance indicators (KPIs) that might reflect these operations goals. These might be customer satisfaction, time from feature conception to deployment, average issue resolution time, and others.

 Working from KPIs, identify the metrics and sources of data that might reflect these goals best. Customer satisfaction may be an combination of various metrics such as call wait or response times, satisfaction scores, and types of issues raised. Deployment times may be the sum of time needed for testing and deployment, plus any post-deployment fixes that needed to be added. Statistics showing the time spent on different types of issues (or the counts of those issues) can provide a window into where targeted effort is needed.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ Quick - Using KPIs ](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)
+ [ Amazon CloudWatch - Using Metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [ Building Dashboards ](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/)
+ [ How to track your cost optimization KPIs with KPI Dashboard ](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/)
