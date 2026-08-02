---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_monitor_usage_detailed_source.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP01 Configure detailed information sources
<a name="cost_monitor_usage_detailed_source"></a>

 Configure the AWS Cost and Usage Report, and Cost Explorer hourly granularity, to provide detailed cost and usage information. Configure your workload to have log entries for every delivered business outcome.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Enable hourly granularity in AWS Cost Explorer and create a [AWS Cost and Usage Report (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/). These data sources provide the most accurate view of cost and usage across your entire organization. The CUR provides daily or hourly usage granularity, rates, costs, and usage attributes for all chargeable AWS services. All possible dimensions are in the CUR including: tagging, location, resource attributes, and account IDs.

Configure your CUR with the following customizations:
+ Include resource IDs
+ Automatically refresh the CUR
+ Hourly granularity
+ **Versioning:** Overwrite existing report
+ **Data integration:** Amazon Athena (Parquet format and compression)

Use [AWS Glue](https://aws.amazon.com/glue/) to prepare the data for analysis, and use [Amazon Athena](https://aws.amazon.com/athena/) to perform data analysis, using SQL to query the data. You can also use [Amazon Quick](https://aws.amazon.com/quicksight/) to build custom and complex visualizations and distribute them throughout your organization.

**Implementation steps**
+ ** Configure the cost and usage report: **Using the billing console, configure at least one cost and usage report. Configure a report with hourly granularity that includes all identifiers and resource IDs. You can also create other reports with different granularities to provide higher-level summary information.
+ ** Configure hourly granularity in Cost Explorer: **Using the billing console, enable Hourly and Resource Level Data.
**Note**
There will be associated costs with enabling this feature. For details, refer to the pricing.
+  **Configure application logging:** Verify that your application logs each business outcome that it delivers so it can be tracked and measured. Ensure that the granularity of this data is at least hourly so it matches with the cost and usage data. Refer to the [Well-Architected Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) for more detail on logging and monitoring.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html)
+  [AWS Cost and Usage Report (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
+  [AWS Glue](https://aws.amazon.com/glue/)
+  [Amazon Quick](https://aws.amazon.com/quicksight/)
+  [AWS Cost Management Pricing](https://aws.amazon.com/aws-cost-management/pricing/)
+  [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)
+  [Well-Architected Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)

 **Related examples:**
+  [AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html)
