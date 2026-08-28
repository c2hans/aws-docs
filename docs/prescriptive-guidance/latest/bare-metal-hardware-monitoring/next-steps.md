---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/next-steps.html
---

# Next steps
<a name="next-steps"></a>

By following the architecture and best practices described in this guide, you can collect data from your on-premises bare-metal servers and then send that data to AWS for storage and visualization. We recommend that you use Amazon Managed Service for Prometheus to reliably store the data and monitor the Prometheus instances. Then, you can use Amazon Managed Grafana to query, correlate, and visualize the data.

We recommend the following next steps:
+ Set up Telegraf in an Amazon Elastic Kubernetes Service (Amazon EKS) Anywhere container in your on-premises data center. You can use the sample YAML deployment file that is provided in the [Scalability and high performance](best-practices.md#best-practices-performance) section.
+ Determine the key performance indicators (KPIs) and metrics that you need to monitor for your bare-metal infrastructure. These might include CPU utilization, memory usage, disk I/O, network traffic, temperature, and other hardware-specific metrics.
+ In Amazon Managed Service for Prometheus, define and configure alerts for critical metrics and thresholds. To make sure that you receive timely notifications, you can integrate this monitoring solution with other incident management or communication tools, such as email, Slack, or PagerDuty.
+ Establish on-call rotations and escalation procedures so that your organization can effectively respond to any alerts.
+ In Amazon Managed Grafana, create custom dashboards that help you visualize key metrics and understand the overall health of your bare-metal hardware. Generate regular reports that help you analyze trends, identify potential issues, and plan for capacity or infrastructure changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
