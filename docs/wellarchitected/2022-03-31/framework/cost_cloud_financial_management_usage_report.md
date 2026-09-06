---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_cloud_financial_management_usage_report.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST01-BP05 Report and notify on cost optimization
<a name="cost_cloud_financial_management_usage_report"></a>

 Configure AWS Budgets and AWS Cost Anomaly Detection to provide notifications on cost and usage against targets. Have regular meetings to analyze your workload's cost efficiency and to promote cost-aware culture.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

You must regularly report on cost and usage optimization within your organization. You can implement dedicated sessions to cost optimization, or include cost optimization in your regular operational reporting cycles for your workloads. Use services and tools to identify and implement cost savings opportunities. [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) provides dashboards and reports. You can track your progress of cost and usage against configured budgets with [AWS Budgets Reports](https://aws.amazon.com/about-aws/whats-new/2019/07/introducing-aws-budgets-reports/).

Use [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to set custom budgets to track your costs and usage, and respond quickly to alerts received from email or Amazon Simple Notification Service (Amazon SNS) notifications if you exceed your threshold. [Set your preferred budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) period to daily, monthly, quarterly, or annually, and create specific budget limits to stay informed on how actual or forecasted costs and usage progress toward your budget threshold. You can also set up [alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/sns-alert-chime.html) and [actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) against those alerts to run automatically, or through an approval process when a budget target is exceeded.

Implement notifications on cost and usage to ensure that changes in cost and usage can be acted upon quickly if they are unexpected. [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) allows you to reduce cost surprises and enhance control without slowing innovation. AWS Cost Anomaly Detection identifies anomalous spend and root causes, which helps to reduce the risk of billing surprises. With three simple steps, you can create your own contextualized monitor and receive alerts when any anomalous spend is detected.

You can also use [Amazon Quick](https://aws.amazon.com/quicksight/) with AWS Cost and Usage Report (CUR) data, to provide highly customized reporting with more granular data. Amazon Quick allows you to schedule reports and receive periodic Cost Report emails for historical cost and usage, or cost-saving opportunities.

Use [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), which provides guidance to verify whether provisioned resources are aligned with AWS best practices for cost optimization.

Periodically create reports containing a highlight of Savings Plans, Reserved Instances and Amazon Elastic Compute Cloud (Amazon EC2) rightsizing recommendations from AWS Cost Explorer to start reducing the cost associated with steady-state workloads, idle, and underutilized resources. Identify and recoup spend associated with cloud waste for resources that are deployed. Cloud waste occurs when incorrectly-sized resources are created, or different usage patterns are observed instead what is expected. Follow AWS best practices to reduce your waste and [optimize and save](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/) your cloud costs.

Generate reports regularly for better purchasing options for your resources to drive down unit costs for your workloads. Purchasing options such as Savings Plans, Reserved Instances, or Amazon EC2 Spot Instances offer the deepest cost savings for fault-tolerant workloads and allow stakeholders (business owners, finance and tech teams) to be part of these commitment discussions.

Share the reports that contain opportunities or new release announcements that may help you to reduce total cost of ownership (TCO) of the cloud. Adopt new services, Regions, features, solutions, or new ways to achieve further cost reductions.

**Implementation steps**
+  **Configure AWS Budgets: **Configure AWS Budgets on all accounts for your workload. Set a budget for the overall account spend, and a budget for the workload by using tags.
  +  [Well-Architected Labs: Cost and Governance Usage](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_2_Cost_and_Usage_Governance/README.html)
+  **Report on cost optimization: **Set up a regular cycle to discuss and analyze the efficiency of the workload. Using the metrics established, report on the metrics achieved and the cost of achieving them. Identify and fix any negative trends, and identify positive trends that you can promote across your organization. Reporting should involve representatives from the application teams and owners, finance, and management.
  +  [Well-Architected Labs: Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/README.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
+ [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+ [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
+ [AWS Budgets Best Practices](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html#budgets-best-practices-setting-budgets%3Fsc_channel=ba%26sc_campaign=aws-budgets%26sc_medium=manage-and-control%26sc_content=web_pdp%26sc_detail=how-do-I%26sc_outcome=aw%26trk=how-do-I_web_pdp_aws-budgets)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
+ [Amazon S3 Analytics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html)
+ [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

 **Related examples:**
+  [Well-Architected Labs: Cost and Governance Usage](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_2_Cost_and_Usage_Governance/README.html)
+  [Well-Architected Labs: Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/README.html)
+ [Key ways to start optimizing your AWS cloud costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/key-ways-to-start-optimizing-your-aws-cloud-costs/)
