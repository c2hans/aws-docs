---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_intro_system_views.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# System monitoring (provisioned only)
<a name="c_intro_system_views"></a>

The following system tables and views can be queried on provisioned clusters. STL and STV tables and views contain a subset of data found in several of the system tables. These provide quicker and easier access to commonly queried data found in those tables.

SVCS views provide details about queries on both the main and concurrency scaling clusters. SVL views provide information only for queries run on the main cluster, with the exception of SVL\_STATEMENTTEXT. SVL\_STATEMENTTEXT can contain information for queries run on concurrency scaling clusters as well as the main cluster.

**Topics**
+ [STL views for logging](c_intro_STL_tables.md)
+ [STV tables for snapshot data](c_intro_STV_tables.md)
+ [SVCS views for main and concurrency scaling clusters](svcs_views.md)
+ [SVL views for main cluster](svl_views.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
