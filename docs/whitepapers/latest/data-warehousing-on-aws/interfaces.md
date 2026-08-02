---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/interfaces.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Interfaces
<a name="interfaces"></a>

 Amazon Redshift has custom Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC) drivers you can download from the **Connect Client** tab of the console, which means you can use a wide range of familiar SQL clients. You can also use standard PostgreSQL JDBC and ODBC drivers. For more information about Amazon Redshift drivers, see [Amazon Redshift and PostgreSQL](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html) in the [Amazon Redshift Database Developer Guide](https://docs.aws.amazon.com/redshift/latest/dg/redshift-dg.pdf).

 Amazon Redshift provides a built-in [Query Editor](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html) in the web console. The Query Editor is an in-browser interface for running SQL queries on Amazon Redshift clusters directly from AWS Management Console. It’s a convenient way for a database administrator (DBA) or a user to run queries as needed, or diagnose queries.

 You can also find numerous examples of validated integrations with many [popular BI and ETL vendors.](https://aws.amazon.com/redshift/partners/) In these integrations, loads and unloads execute in parallel on each compute node to maximize the rate at which you can ingest or export data to and from multiple resources, including S3, Amazon EMR, and DynamoDB. You can easily load streaming data into Amazon Redshift using [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/), enabling near real-time analytics with existing BI tools and dashboards. You can locate metrics for compute utilization, memory utilization, storage utilization, and read/write traffic to your Amazon Redshift data warehouse cluster by using the console, or [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) API operations.
