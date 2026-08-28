---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/cost_monitor_usage_detailed_source.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST03-BP01 Configure detailed information sources
<a name="cost_monitor_usage_detailed_source"></a>

Configure the cost management and reporting tools for hourly granularity to provide detailed cost and usage information, enabling deeper analytics and transparency. Configure your workload to generate or have the log entries for every delivered business outcome.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Detailed billing information such as hourly granularity in cost management tools allow organizations to track their consumptions with further details and help them to identify some of the cost increase reasons. These data sources provide the most accurate view of cost and usage across your entire organization.

 AWS Cost and Usage Report provides daily or hourly usage granularity, rates, costs, and usage attributes for all chargeable AWS services. All possible dimensions are in the CUR, including tagging, location, resource attributes, and account IDs.

 Configure your CUR with the following customizations:
+  Include resource IDs
+  Automatically refresh the CUR
+  Hourly granularity
+  **Versioning:** Overwrite existing report
+  **Data integration:** Athena (Parquet format and compression)

 Use [AWS Glue](https://aws.amazon.com/glue/) to prepare the data for analysis, and use [Amazon Athena](https://aws.amazon.com/athena/) to perform data analysis, using SQL to query the data. You can also use [Quick](https://aws.amazon.com/quicksight/) to build custom and complex visualizations and distribute them throughout your organization.

### Implementation steps
<a name="implementation-steps"></a>
+  **Configure the cost and usage report:** Using the billing console, configure at least one cost and usage report. Configure a report with hourly granularity that includes all identifiers and resource IDs. You can also create other reports with different granularities to provide higher-level summary information.
+  **Configure hourly granularity in Cost Explorer:** Enable **Hourly** and **Resource Level Data** to access cost and usage data at hourly granularity for the past 14 days and resource level granularity.
+  **Configure application logging:** Verify that your application logs each business outcome that it delivers so it can be tracked and measured. Ensure that the granularity of this data is at least hourly so it matches with the cost and usage data. For more details on logging and monitoring, see [Well-Architected Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
+  [AWS Glue](https://aws.amazon.com/glue/)
+  [Quick](https://aws.amazon.com/quicksight/)
+  [AWS Cost Management Pricing](https://aws.amazon.com/aws-cost-management/pricing/)
+  [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)
+  [Analyzing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)
+  [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html)
+  [Managing AWS Cost and Usage Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.html)
+  [Well-Architected Operational Excellence Pillar](https://wa.aws.amazon.com/wat.pillar.operationalExcellence.en.html)

 **Related examples:**
+  [AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html)
+  [AWS Cost Explorer’s New Look and Common Use Cases](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cost-explorers-new-ui-and-common-use-cases/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
