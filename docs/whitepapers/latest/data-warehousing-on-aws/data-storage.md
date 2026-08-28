---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data storage
<a name="data-storage"></a>

 You can store your data in a lake house, data warehouse, or data mart.
+  **Lake house** — A lake house is an architectural pattern that combines the best elements of data warehouses and data lakes. Lake houses enable you to query data across your data warehouse, data lake, and operational databases to gain faster and deeper insights that are not possible otherwise. With a lake house architecture, you can store data in open file formats in your data lake and query it in place while joining with data warehouse data. This enables you to make this data easily available to other analytics and machine learning tools, rather than locking it in a new silo.
+  **Data warehouse** — Using data warehouses, you can run fast analytics on large volumes of data and unearth patterns hidden in your data by leveraging BI tools. Data scientists query a data warehouse to perform offline analytics and spot trends. Users across the enterprise consume the data using SQL queries, periodic reports, and dashboards as needed to make critical business decisions.
+  **Data mart** — A data mart is a simple form of data warehouse focused on a specific functional area or subject matter. For example, you can have specific data marts for each division in your enterprise, or segment data marts based on regions. You can build data marts from a large data warehouse, operational stores, or a hybrid of the two. Data marts are simple to design, build, and administer. However, because data marts are focused on specific functional areas, querying across functional areas can become complex because of distribution.

 You can use Amazon Redshift to build lake houses, data marts, and data warehouses. Redshift enables you to easily query data in your data lake, and write data back to your data lake in open formats. You can use familiar SQL statements to combine and process data across all your data stores, and execute queries on live data in your operational databases without requiring any data loading and ETL pipelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
