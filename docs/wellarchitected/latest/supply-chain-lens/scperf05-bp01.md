---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp01.html
---

# SCPERF05-BP01 Implement comprehensive monitoring and dashboards for supply chain performance
<a name="scperf05-bp01"></a>

 Building an effective dashboard involves focusing on the key performance indicators (KPIs) that matter most to your organization and displaying them in an understandable and visually appealing way.

 **Desired outcome:** Measuring of the application behavior can help manage it better, just not only the performance of the application also during vulnerable situations and to take actions spontaneously.

 **Benefits of establishing this best practice:** Good observability and dashboard to monitor performance efficiency and continuous improvements.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-scperf05-bp01"></a>

 Use tools and best practices to gain insights including End-to-end visibility, alerts and alarms, Anomaly detection, regular review of metrics and logs, security monitoring, and cost optimization. Remember, while AWS provides observability tools (Amazon CloudWatch, AWS CloudTrail) to monitor and gain insights, it's the combination of these tools with best practices that will give you the most valuable insights about the end-to-end supply chain systems.

### Implementation steps
<a name="implementation-steps-44"></a>

1.  Identify key performance indicators (KPIs) that are most critical to supply chain operations and business objectives.

1.  Design and implement comprehensive dashboards using Quick or CloudWatch dashboards to visualize supply chain performance.

1.  Configure automated alerts and alarms based on performance thresholds and anomaly detection to enable proactive response.

1.  Implement end-to-end tracing and monitoring across all supply chain components, from edge devices to cloud applications.

1.  Establish regular review processes for performance metrics and logs to identify trends and optimization opportunities.

1.  Create role-based dashboard views that provide relevant insights to different stakeholders across the supply chain organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
