---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_cloud_financial_management_proactive_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST01-BP06 Monitor cost proactively
<a name="cost_cloud_financial_management_proactive_process"></a>

Implement tooling and dashboards to monitor cost proactively for the workload. Regularly review the costs with configured tools or out of the box tools, do not just look at costs and categories when you receive notifications. Monitoring and analyzing costs proactively helps to identify positive trends and allows you to promote them throughout your organization.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

It is recommended to monitor cost and usage proactively within your organization, not just when there are exceptions or anomalies. Highly visible dashboards throughout your office or work environment ensure that key people have access to the information they need, and indicate the organization’s focus on cost optimization. Visible dashboards allow you to actively promote successful outcomes and implement them throughout your organization.

Create a daily or frequent routine to use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or any other dashboard such as [Amazon Quick](https://aws.amazon.com/quicksight/) to see the costs and analyze proactively. Analyze AWS service usage and costs at the AWS account-level, workload-level, or specific AWS service-level with grouping and filtering, and validate whether they are expected or not. Use the hourly- and resource-level granularity and tags to filter and identify incurring costs for the top resources. You can also build your own reports with the [Cost Intelligence Dashboard](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/), an [Amazon Quick](https://aws.amazon.com/quicksight/) solution built by AWS Solutions Architects, and compare your budgets with the actual cost and usage.

**Implementation steps**
+  **Report on cost optimization:** Set up a regular cycle to discuss and analyze the efficiency of the workload. Using the metrics established, report on the metrics achieved and the cost of achieving them. Identify and fix any negative trends, and identify positive trends to promote across your organization. Reporting should involve representatives from the application teams and owners, finance, and management.
+ **Create and enable daily granularity [AWS Budgets](https://aws.amazon.com/blogs/aws-cloud-financial-management/launch-daily-cost-and-usage-budgets/) for the cost and usage to take timely actions to prevent any potential cost overruns: ** AWS Budgets allow you to configure alert notifications, so you stay informed if any of your budget types fall out of your pre-configured thresholds. The best way to leverage AWS Budgets is to set your expected cost and usage as your limits, so that anything above your budgets can be considered overspend.
+ **Create AWS Cost Anomaly Detection for cost monitor: ** [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) uses advanced Machine Learning technology to identify anomalous spend and root causes, so you can quickly take action. It allows you to configure cost monitors that define spend segments you want to evaluate (for example, individual AWS services, member accounts, cost allocation tags, and cost categories), and lets you set when, where, and how you receive your alert notifications. For each monitor, attach multiple alert subscriptions for business owners and technology teams, including a name, a cost impact threshold, and alerting frequency (individual alerts, daily summary, weekly summary) for each subscription.
+ **Use AWS Cost Explorer or integrate your AWS Cost and Usage Report (CUR) data with Amazon Quick dashboards to visualize your organization’s costs:** AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. The [Cost Intelligence Dashboard](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/) is a customizable and accessible dashboard to help create the foundation of your own cost management and optimization tool.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
+ [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
+ [Daily Cost and Usage Budgets](https://aws.amazon.com/blogs/aws-cloud-financial-management/launch-daily-cost-and-usage-budgets/)
+ [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/)

 **Related examples:**
+  [Well-Architected Labs: Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/README.html)
+  [Well-Architected Labs: Advanced Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_5_Cost_Visualization/README.html)
+ [Well-Architected Labs: Cloud Intelligence Dashboards](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/)
+ [Well-Architected Labs: Cost Visualization](https://wellarchitectedlabs.com/cost/200_labs/200_5_cost_visualization/)
+ [AWS Cost Anomaly Detection Alert with Slack](https://aws.amazon.com/aws-cost-management/resources/slack-integrations-for-aws-cost-anomaly-detection-using-aws-chatbot/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
