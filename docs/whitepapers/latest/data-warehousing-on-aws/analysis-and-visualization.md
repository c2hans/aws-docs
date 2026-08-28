---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/analysis-and-visualization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Analysis and visualization
<a name="analysis-and-visualization"></a>

 After processing the data and making it available for further analysis, you need the right tools to analyze and visualize the processed data.

 In many cases, you can perform data analysis using the same tools you use for processing data. You can use tools such as [MySQL Workbench](https://www.mysql.com/products/workbench/) to analyze your data in Amazon Redshift with ANSI SQL. Amazon Redshift also works well with popular third-party BI solutions available on the market, such as [Tableau](https://www.tableau.com/) and [MicroStrategy](https://www.microstrategy.com/en).

 [Amazon Quick](https://aws.amazon.com/quicksight/) is a fast, cloud-powered BI service that enables you to create visualizations, perform analysis as needed, and quickly get business insights from your data. Amazon Quick offers native integration with AWS data sources such as [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon S3](https://aws.amazon.com/s3/), and [Amazon RDS](https://aws.amazon.com/rds/). Amazon Redshift sources can be auto-detected by Amazon Quick, and can be queried either using a direct query or SPICE mode. SPICE is the in-memory optimized calculation engine for Amazon Quick, designed specifically for fast, as-needed data visualization. You can improve the performance of database datasets by importing the data into SPICE instead of using a direct query to the database.

 If you are using Amazon S3 as your primary storage, you can use [Amazon Athena/QuickSight integration](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html) to perform analysis and visualization. [Amazon Athena](https://aws.amazon.com/athena/) is an interactive query service that makes it easy to analyze data in S3 using standard SQL. You can run SQL queries using Athena on data stored in S3, and build business dashboards within QuickSight.

 For another visualization approach, [Apache Zeppelin](https://zeppelin.apache.org/) is an open-source BI solution that you can run on Amazon EMR to visualize data in Amazon S3 using [Spark SQL](https://spark.apache.org/). You can also use Apache Zeppelin to visualize data in Amazon Redshift.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
