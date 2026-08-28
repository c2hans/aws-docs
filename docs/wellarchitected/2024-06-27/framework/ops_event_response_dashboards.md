---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/ops_event_response_dashboards.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP06 Communicate status through dashboards
<a name="ops_event_response_dashboards"></a>

 Use dashboards as a strategic tool to convey real-time operational status and key metrics to different audiences, including internal technical teams, leadership, and customers. These dashboards offer a centralized, visual representation of system health and business performance, enhancing transparency and decision-making efficiency.

 **Desired outcome:**
+  Your dashboards provide a comprehensive view of the system and business metrics relevant to different stakeholders.
+  Stakeholders can proactively access operational information, reducing the need for frequent status requests.
+  Real-time decision-making is enhanced during normal operations and incidents.

 **Common anti-patterns:**
+ Engineers joining an incident management call require status updates to get up to speed.
+ Relying on manual reporting for management, which leads to delays and potential inaccuracies.
+  Operations teams are frequently interrupted for status updates during incidents.

 **Benefits of establishing this best practice:**
+  Empowers stakeholders with immediate access to critical information, promoting informed decision-making.
+  Reduces operational inefficiencies by minimizing manual reporting and frequent status inquiries.
+  Increases transparency and trust through real-time visibility into system performance and business metrics.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Dashboards effectively communicate the status of your systems and business metrics and can be tailored to the needs of different audience groups. Tools like Amazon CloudWatch dashboards and Amazon Quick help you create interactive, real-time dashboards for system monitoring and business intelligence.

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify stakeholder needs:** Determine the specific information needs of different audience groups, such as technical teams, leadership, and customers.

1.  ** Choose the right tools:** Select appropriate tools like [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) for system monitoring and [Amazon Quick](https://aws.amazon.com/quicksight/) for interactive business intelligence.

1.  **Design effective dashboards:**
   +  Design dashboards to clearly present relevant metrics and KPIs, ensuring they are understandable and actionable.
   +  Incorporate system-level and business-level views as needed.
   +  Include both high-level (for broad overviews) and low-level (for detailed analysis) dashboards.
   +  Integrate automated alarms within dashboards to highlight critical issues.
   +  Annotate dashboards with important metrics thresholds and goals for immediate visibility.

1.  **Integrate data sources:**
   +  Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to aggregate and display metrics from various AWS services and [query metrics from other data sources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.html), creating a unified view of your system's health and business metrics.
   +  Use features like [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to query and visualize log data from different applications and services.

1.  **Provide self-service access:**
   +  Share CloudWatch dashboards with relevant stakeholders for self-service information access using [dashboard sharing features](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.html).
   +  Ensure that dashboards are easily accessible and provide real-time, up-to-date information.

1.  **Regularly update and refine:**
   +  Continually update and refine dashboards to align with evolving business needs and stakeholder feedback.
   +  Regularly review the dashboards to keep them relevant and effective for conveying the necessary information.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS08-BP05 Create dashboards](ops_workload_observability_create_dashboards.md)

 **Related documents:**
+ [ Building dashboards for operational visibility ](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/)
+ [ Using Amazon CloudWatch dashboards ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
+ [ Create flexible dashboards with dashboard variables ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html)
+ [ Sharing CloudWatch dashboards ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.html)
+ [ Query metrics from other data sources ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.html)
+ [ Add a custom widget to a CloudWatch dashboard ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.html)

 **Related examples:**
+ [ One Observability Workshop - Dashboards ](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US/aws-native/dashboards)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
