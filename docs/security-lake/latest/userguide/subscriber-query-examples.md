---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-examples.html
---

# Security Lake queries
<a name="subscriber-query-examples"></a>

You can query the data that Security Lake stores in AWS Lake Formation databases and tables. You can also create third-party subscribers in the Security Lake console, API, or AWS CLI. Third-party subscribers can also query Lake Formation data from the sources that you specify.

The Lake Formation data lake administrator must grant `SELECT` permissions on the relevant databases and tables to the IAM identity that queries the data. A subscriber must also be created in Security Lake before it can query data. For more information about how to create a subscriber with query access, see [Managing query access for Security Lake subscribers](subscriber-query-access.md).

**Querying data with retention settings**
The [Amazon S3 Lifecycle settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) affect how long data is kept, which in turn affects how far back in time you can query. If you have retention settings configured in Security Lake, you must include a time-based filter in your queries to ensure your result sets are scoped to the data files that have not expired. For more information about data retention in Security Lake, see [Lifecycle management](lifecycle-management.md).

The query examples in the following sections include time-based filters, such as `eventDay` or `time_dt`, to demonstrate this best practice.

**Topics**
+ [Security Lake queries for AWS source version 1 (OCSF 1.0.0-rc.2)](subscriber-query-examples1.md)
+ [Security Lake queries for AWS source version 2 (OCSF 1.1.0)](subscriber-query-examples2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
