---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/cost_monitor_usage_config_tools.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP05 Configure billing and cost management tools
<a name="cost_monitor_usage_config_tools"></a>

 Configure cost management tools in line with your organization policies to manage and optimize cloud spend. This includes services, tools, and resources to organize and track cost and usage data, enhance control through consolidated billing and access permission, improve planning through budgeting and forecasts, receive notifications or alerts, and further lower cost with resources and pricing optimizations.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 To establish strong accountability, your account strategy should be considered first as part of your cost allocation strategy. Get this right, and you may not need to go any further. Otherwise, there can be unawareness and further pain points.

 To encourage accountability of cloud spend, users should have access to tools that provide visibility into their costs and usage. It is recommended that all workloads and teams have tools configured for the following details and purposes:
+  **Organize:** Establish your cost allocation and governance baseline with your own tagging strategy and taxonomy. Tag supported AWS resources and categorize them meaningfully based on your organization structure (business units, departments, or projects). Tag account names for specific cost centers and map them with AWS Cost Categories to group accounts for particular business units to their cost centers so that business unit owner can see multiple accounts’ consumption in one place.
+  **Access:** Track organization-wide billing information in [consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) and verify the right stakeholders and business owners have access.
+  **Control:** Build effective governance mechanisms with the right guardrails to prevent unexpected scenarios when using Service Control Policies (SCP), tag policies, and budget alerts. For example, you can allow teams to create resources in preferred Regions only by using effective control mechanisms.
+  **Current State:** Configure a dashboard showing current levels of cost and usage. The dashboard should be available in a highly visible place within the work environment similar to an operations dashboard. You can use [Cloud Intelligence Dashboard (CID)](https://github.com/aws-samples/aws-cudos-framework-deployment) or any other supported products to create this visibility.
+  **Notifications:** Provide notifications when cost or usage is outside of defined limits and when anomalies occur with AWS Budgets or AWS Cost Anomaly Detection.
+  **Reports:** Summarize all cost and usage information and raise awareness and accountability of your cloud spend with detailed, attributable cost data. Reports should be relevant to the team consuming them and ideally should contain recommendations.
+  **Tracking:** Show the current cost and usage against configured goals or targets.
+  **Analysis:** Allow team members to perform custom and deep analysis down to the hourly granularity, with all possible dimensions.
+  **Inspect:** Stay up to date with your resource deployment and cost optimization opportunities. Get notifications (using Amazon CloudWatch, Amazon SNS, or Amazon SES) for resource deployments at the organization level and review cost optimization recommendations (for example, AWS Compute Optimizer or AWS Trusted Advisor).
+  **Trending:** Display the variability in cost and usage over the required period of time, with the required granularity.
+  **Forecasts:** Show estimated future costs, estimate your resource usage, and spend with forecast dashboards that you create.

 You can use AWS tools like [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Billing and Cost Management](https://aws.amazon.com/aws-cost-management/aws-billing/), or [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) for essentials, or you can integrate CUR data with [Amazon Athena](https://docs.aws.amazon.com/athena/?id=docs_gateway) and [Quick](https://docs.aws.amazon.com/quicksight/?id=docs_gateway) to provide this capability for more detailed views. If you don't have essential skills or bandwidth in your organization, you can work with [AWS ProServ](https://aws.amazon.com/professional-services/), [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/), or [AWS Partners](https://aws.amazon.com/partners/) and use their tools. You can also use third-party tools, but verify first that the cost provides value to your organization.

### Implementation steps
<a name="implementation-steps"></a>
+  **Allow team-based access to tools:** Configure your accounts and create groups that have access to the required cost and usage reports for their consumptions and use [AWS Identity and Access Management](https://aws.amazon.com/iam/) to [control access](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html) to the tools such as AWS Cost Explorer. These groups must include representatives from all teams that own or manage an application. This certifies that every team has access to their cost and usage information to track their consumption.
+  **Configure AWS Budgets:** [Configure AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) on all accounts for your workloads. Set budgets for the overall account spend, and budgets for the workloads by using tags. Configure notifications in AWS Budgets to receive alerts for when you exceed your budgeted amounts, or when your estimated costs exceed your budgets.
+  **Configure AWS Cost Explorer:** Configure [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for your workload and accounts to visualize your cost data for further analysis. Create a dashboard for the workload that tracks overall spend, key usage metrics for the workload, and forecast of future costs based on your historical cost data.
+  **Configure AWS Cost Anomaly Detection:** Use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) for your accounts, core services or cost categories you created to monitor your cost and usage and detect unusual spends. You can receive alerts individually in aggregated reports, and receive alerts in an email or an Amazon SNS topic which allows you to analyze and determine the root cause of the anomaly, and identify the factor that is driving the cost increase.
+  **Configure advanced tools:** Optionally, you can create custom tools for your organization that provides additional detail and granularity. You can implement advanced analysis capability using [Amazon Athena](https://docs.aws.amazon.com/athena/?id=docs_gateway), and dashboards using [Quick](https://docs.aws.amazon.com/quicksight/?id=docs_gateway). Consider using the [CID solution](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/) which has pre-configured, advanced dashboards. There are also [AWS Partners](https://aws.amazon.com/marketplace/solutions/business-applications/cloud-cost-management) you can work with and adopt their cloud management solutions to enable cloud bill monitoring and optimization in one convenient location.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html)
+  [Tagging](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) AWS resources
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)
+  [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/)
+  [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)
+  [Example service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html)
+  [AWS APN Partners – Cost Management](https://aws.amazon.com/marketplace/solutions/business-applications/cloud-cost-management)

 **Related videos:**
+  [Deploying Cloud Intelligence Dashboards](https://www.youtube.com/watch?v=FhGZwfNJTnc)
+  [Get Alerts on any FinOps or Cost Optimization Metric or KPI](https://www.youtube.com/watch?v=dzRKDSXCtAs)

 **Related examples:**
+  [Well-Architected Labs - AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html/)
+  [Well-Architected Labs: Billing Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/README.html)
+  [Well-Architected Labs: Cost and Governance Usage](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_2_Cost_and_Usage_Governance/README.html)
+  [Well-Architected Labs: Cost and Usage Analysis](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_4_Cost_and_Usage_Analysis/README.html)
+  [Well-Architected Labs: Cost and Usage Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_5_Cost_Visualization/README.html)
+  [Well-Architected Labs: Cloud Intelligence Dashboards](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/)
+  [How to use SCPs to set permission guardrails across accounts](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/)
