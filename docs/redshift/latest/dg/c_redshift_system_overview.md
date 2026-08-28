---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Amazon Redshift architecture
<a name="c_redshift_system_overview"></a>

This topic helps you understand the components that make up Amazon Redshift.

An Amazon Redshift data warehouse is an enterprise-class relational database query and management system.

Amazon Redshift supports client connections with many types of applications, including business intelligence (BI), reporting, data, and analytics tools.

When you run analytic queries, you are retrieving, comparing, and evaluating large amounts of data in multiple-stage operations to produce a final result.

Amazon Redshift achieves efficient storage and optimum query performance through a combination of massively parallel processing, columnar data storage, and very efficient, targeted data compression encoding schemes. This section presents an introduction to the Amazon Redshift system architecture.

**Topics**
+ [Data warehouse system architecture](c_high_level_system_architecture.md)
+ [Amazon Redshift Performance](c_challenges_achieving_high_performance_queries.md)
+ [Columnar storage](c_columnar_storage_disk_mem_mgmnt.md)
+ [Workload management](c_workload_mngmt_classification.md)
+ [Using Amazon Redshift with other services](using-redshift-with-other-services.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
