---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/reference-architecture-4.html
---

# Reference architecture
<a name="reference-architecture-4"></a>

![Diagram showing QuickSight dashboard end-to-end design](http://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/images/quicksight-dashboard-design.png)

 **Data sources:** Supports connection with traditional Data Warehouse or databases and also have the capacity to connect to non-traditional sources such as SaaS applications. Supported datasources in QuickSight include Amazon S3, Amazon Redshift, Amazon Aurora, Oracle, MySQL, Microsoft SQL Server, Snowﬂake, Teradata, Jira, and ServiceNow. Check [here](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html) for the complete list of data sources supported in QuickSight. These data sources could be secured behind a private subnet and QuickSight can connect in a secure mechanism using strategies such as VPC endpoints, and secure firewalls.

 **Visualization Tool:** Quick.

 **Consumers:** Visual dashboard consumers accessing a QuickSight console or embedded QuickSight analytics dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
