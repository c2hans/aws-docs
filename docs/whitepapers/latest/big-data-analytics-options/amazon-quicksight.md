---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-quicksight.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Quick
<a name="amazon-quicksight"></a>

Amazon Quick is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud. It makes it easy for all employees within an organization to build visualizations, perform ad hoc analysis, and quickly get business insights from their data, anytime, on any device. It can connect to a wide variety of data sources including flat files such as CSV and Excel, access on-premises databases including Oracle, SQL Server, MySQL, and PostgreSQL, AWS resources such as Amazon RDS databases, Amazon Redshift, Amazon Athena, and Amazon S3, and SaaS solutions such as Salesforce, ServiceNow, and Adobe Analytics. Amazon Quick enables organizations to scale their business analytics capabilities to hundreds of thousands of users, and delivers fast and responsive query performance by using a robust in-memory engine (SPICE).

Amazon Quick is built with "[SPICE](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-quicksight-spice-data-engine-supports-data-sets-250m-rows/)" – a Super-fast, Parallel, In-memory Calculation Engine. Built from the ground up for the cloud, SPICE uses a combination of columnar storage, in-memory technologies enabled through the latest hardware innovations, and machine code generation to run interactive queries on large datasets and get rapid responses. SPICE supports rich calculations to help you derive valuable insights from your analysis without worrying about provisioning or managing infrastructure. Data in SPICE is persisted until it is explicitly deleted by the user. SPICE also automatically replicates data for high availability and enables Amazon Quick to scale to hundreds of thousands of users who can all simultaneously perform fast interactive analysis across a wide variety of AWS data sources.

QuickSight leverages the AWS proven ML capabilities, making it easy for BI teams to perform advanced analytics (for example, what-if analyses, anomaly detection, ML-based forecasting, churn prediction, and so on) without prior data science experience. You can use QuickSight’s pre-built models, or bring your own ML models from Amazon SageMaker AI.

## Ideal usage patterns
<a name="ideal-usage-patterns-quicksight"></a>

 Amazon Quick is an ideal Business Intelligence tool, allowing end users to create visualizations that provide insight into their data to help them make better business decisions. Amazon Quick can be used to do the following:
+  Quick interactive ad hoc exploration and optimized visualization of data
+  Create and share dashboards and KPIs to provide insight into your data
+  Create *Stories*, which are guided tours through specific views of an analysis and enable you to share insights and collaborate with others. They are used to convey key points, a thought process, or the evolution of an analysis for collaboration
+  Analyze and visualize data coming from logs and stored in S3
+  Analyze and visualize data from on premise databases like SQL Server, Oracle, PostGreSQL, and MySQL
+  Analyze and visualize data in various AWS resources such as Amazon RDS databases, Amazon Redshift, Amazon Athena, and Amazon S3.
+  Analyze and visualize data in software as a service (SaaS) applications such as Salesforce.
+  Analyze and visualize data in data sources that can be connected to using [JDBC/ODBC](https://www.geeksforgeeks.org/difference-odbc-jdbc/) connection.
+ Enhance with your QuickSight dashboard with **Machine Learning Insights** and **Forecasts**
+ Ask natural language questions on your data and have [Amazon QuickSight Q](https://aws.amazon.com/quicksight/q/) automatically build your visualization

## Cost model
<a name="cost-model-quicksight"></a>

Amazon Quick has two different editions for pricing; *Standard* edition and *Enterprise* edition.
+ The **Standard Edition** is ideal for personal data analysis and exploration, it offers a full set of features for creating and sharing data visualizations, but it does not provide some of the Enterprise security and advanced options, a comparison of the features of the two editions can be found on the [Amazon QuickSight Pricing](https://aws.amazon.com/quicksight/pricing/) page. The Standard Edition is priced at $9/user/month for an annual subscription ($12/GB/month for the month-to-month option) with ten GB of SPICE capacity included. You can get additional SPICE capacity for $.25/GB/month.
+ The **Enterprise** edition delivers insights at scale and offers embedding options, advanced security (data encryption at rest, row and column level security, access on private VPC and on premises), ML insights, folders, and templates.

  It is priced at $18/author/month ($24/GB/month for the month-to-month option) with ten GB of SPICE capacity included. Readers have a per-session pricing up to $5/user/month ($.30 per session; 1 session = 30 minutes from login).

  For large-scale deployments and public embedding, there is a Session capacity pricing starting at $250 per month for 500 sessions.

## Performance
<a name="performance-quicksight"></a>

Amazon Quick is built with [SPICE](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-quicksight-spice-data-engine-supports-data-sets-250m-rows/). Built from the ground up for the cloud, SPICE uses a combination of columnar storage, in-memory technologies enabled through the latest hardware innovations, and machine code generation to run interactive queries on large datasets and get rapid responses.

## Durability and availability
<a name="durability-and-availability-quicksight"></a>

SPICE automatically replicates data for high availability and enables Amazon Quick to scale to hundreds of thousands of users who can all simultaneously perform fast interactive analysis across a wide variety of AWS data sources.

## Scalability and elasticity
<a name="scalability-and-elasticity-quicksight"></a>

Amazon Quick is a fully managed service and it internally takes care of scaling to meet the demands of your end users. With Amazon Quick you don’t need to worry about scale. You can seamlessly grow your data from a few hundred megabytes to many terabytes of data without managing any infrastructure.

## Interfaces
<a name="interfaces-quicksight"></a>

Amazon Quick can connect to a wide variety of data sources including flat files (CSV, TSV, CLF, ELF), connect to on-premises databases like SQL Server, MySQL, and PostgreSQL, and AWS data sources including Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon Athena and Amazon S3, and SaaS, applications like Salesforce. You can also export data from any type of chart or graph and the export contains only the data in the fields that are currently visible in the selected visualization.

You can [share an analysis](https://docs.aws.amazon.com/quicksight/latest/user/sharing-analyses.html), dashboard, or story by choosing **Share with users and groups in your account ** on the application bar from the Amazon Quick service interface. You can select the recipients (email address, username, or group name), permission levels, and other options, before sharing the content with others.

## Anti-patterns
<a name="anti-patterns-quicksight"></a>

While Amazon Quick can perform some transformations, it is not a full-fledged ETL tool. AWS offers AWS Glue, which is a fully managed ETL service that makes it easy for customers to prepare and load their data for analytics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
