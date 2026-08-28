---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/data-federation-using-sql-engine.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data federation using SQL engine
<a name="data-federation-using-sql-engine"></a>

## Amazon Athena: Introduction
<a name="amazon-athena"></a>

 [Amazon Athena](https://aws.amazon.com/athena) is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

 [Amazon Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html) is a new Athena feature that enables data analysts, engineers, and data scientists to run SQL queries across data stored in relational, non-relational, object, and custom data sources. With Amazon Athena Federated Query, customers can submit a single SQL query and analyze data from multiple sources running on-premises or hosted on the cloud. Athena runs federated queries using Data Source Connectors that run on [AWS Lambda](https://aws.amazon.com/lambda).

 Customers can use these connectors to run federated SQL queries in Athena across multiple data sources, including SaaS applications. Additionally, using Query Federation SDK, customers can build connectors to any proprietary data source, and enable Athena to run SQL queries against the data source. Because connectors run on Lambda, customers continue to benefit from Athena’s serverless architecture and do not have to manage infrastructure or scale for peak demands.

### Architecture overview
<a name="architecture-overview-2"></a>

 Athena Federated query connector allows Athena to connect to SaaS applications like Salesforce, Snowflake, and Google BigQuery. Once a connection is established, you can write SQL queries to retrieve data stored in these SaaS applications. To store data in Amazon S3 data lake, you can use Athena statements [Create Table as Select (CTAS) and INSERT INTO for ETL](https://docs.aws.amazon.com/athena/latest/ug/ctas-insert-into-etl.html), which then store the data in Amazon S3 and create a table in the AWS AWS Glue Data Catalog.

![This diagram shows a data ingestion pattern involving Amazon Athena, Amazon S3, AWS Lambda, Salesforce, Snowflake, and Google BigQuery.](http://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/images/athena-based-data-ingestion-pattern.png)

### Usage patterns
<a name="usage-patterns-2"></a>

 This pattern is ideal for anyone who can write ANSI SQL queries. Also, the Create Table as Select (CTAS) statement of Athena provides the flexibility to create a table in AWS AWS Glue Data Catalog with the selected fields from the query, along with the file type for the data to be stored in Amazon S3. You can do an ETL transformation with ease, and the final datasets can be made ready for end user consumption. You can also use [AWS Step Functions](https://aws.amazon.com/step-functions) to orchestrate the whole ingestion process. For details, refer to [Build and orchestrate ETL pipelines using Amazon Athena and AWS Step Functions](https://aws.amazon.com/blogs/big-data/build-and-orchestrate-etl-pipelines-using-amazon-athena-and-aws-step-functions/).

 Some use cases are as follows:
+  Analysts need to create a real-time, data-driven narrative, and identify specific data points.
+  Administrators need to deprecate old ingestion pipelines, and move to a serverless ingestion pipeline using just a few SQL queries.
+  Data engineers do not need to learn different data access paradigms; they can use SQL to source data from any particular data source.
+  Data scientists needs to use data from any SaaS data source to train their machine learning (ML) models, and that helps them to improve the accuracy of their ML models as well.

### Considerations
<a name="considerations-2"></a>

 Some third-party Athena connectors found in the AWS Serverless Application Repository are paid connectors, so due diligence should be done on the pricing aspect of such SaaS connectors. Also, SaaS applications may have their own bulk export limits and/or data export charges that need to be accounted for.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
