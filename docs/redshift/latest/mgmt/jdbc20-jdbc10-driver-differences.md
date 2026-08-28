---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-jdbc10-driver-differences.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Differences between the 2.x and 1.x versions of the JDBC driver
<a name="jdbc20-jdbc10-driver-differences"></a>

This section describes the differences in the information returned by the 2.x and 1.x versions of the JDBC driver. The JDBC driver version 1.x is discontinued.

The following table lists the DatabaseMetadata information returned by the getDatabaseProductName() and getDatabaseProductVersion() functions for each version of the JDBC driver. JDBC driver version 2.x obtains the values while establishing the connection. JDBC driver version 1.x obtains the values as a result of a query.

| JDBC driver version | getDatabaseProductName() result | getDatabaseProductVersion() result |
| --- | --- | --- |
| 2.x | Redshift | 8.0.2 |
| 1.x | PostgreSQL | 08.00.0002 |

The following table lists the DatabaseMetadata information returned by the getTypeInfo function for each version of the JDBC driver.

| JDBC driver version | getTypeInfo result |
| --- | --- |
| 2.x | Consistent with Redshift datatypes |
| 1.x | Consistent with PostgreSQL datatypes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
