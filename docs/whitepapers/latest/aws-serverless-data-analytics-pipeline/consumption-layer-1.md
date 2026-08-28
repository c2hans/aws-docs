---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/consumption-layer-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Consumption layer
<a name="consumption-layer-1"></a>

 The consumption layer in the presented architecture is composed using fully managed, purpose-built, analytics services that enable interactive SQL, BI dashboarding, batch processing, and ML.

## Interactive SQL
<a name="interactive-sql"></a>

 Amazon Athena is an interactive query service that enables you to run complex ANSI SQL against terabytes of data stored in Amazon S3 without needing to first load it into a database. Athena queries can analyze structured, semi-structured, and columnar data stored in open-source formats such as CSV, JSON, XML Avro, Parquet, and ORC. Athena uses table definitions from Lake Formation to apply schema-on-read to data read from Amazon S3.

 Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the amount of data scanned by the queries you run. Athena provides faster results and lower costs by reducing the amount of data it scans by using [dataset partitioning information](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) stored in the Lake Formation catalog. You can run queries directly on the Athena console of submit them using [Athena JDBC or ODBC endpoints](https://docs.aws.amazon.com/athena/latest/ug/athena-bi-tools-jdbc-odbc.html).

 Federated queries in Amazon Athena enable users to run SQL queries across data stored in relational, non-relational, object, and custom data sources. Athena can run federated queries using [Athena Data Source Connectors](https://docs.aws.amazon.com/athena/latest/ug/writing-federated-queries.html) that run on AWS Lambda.

 Athena natively integrates with AWS services in the [security and monitoring layer](https://docs.aws.amazon.com/athena/latest/ug/security.html) to support authentication, authorization, encryption, logging, and monitoring. It supports table- and column-level access controls defined in the Lake Formation catalog.

## Data warehousing and batch analytics
<a name="data-warehousing-and-batch-analytics"></a>

 Amazon Redshift is a fully managed data warehouse service that can host and process petabytes of data and run thousands highly performant queries in parallel. Amazon Redshift uses a cluster of compute nodes to run very low-latency queries to power interactive dashboards and high-throughput batch analytics to drive business decisions. You can run Amazon Redshift queries directly on the Amazon Redshift console or submit them using the JDBC/ODBC endpoints provided by Amazon Redshift.

 Amazon Redshift provides the capability, called [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html), to perform in-place [queries on structured and semi-structured datasets in Amazon S3](https://aws.amazon.com/blogs/big-data/amazon-redshift-spectrum-extends-data-warehousing-out-to-exabytes-no-loading-required/) without needing to load it into the cluster. Amazon Redshift Spectrum can spin up thousands of query-specific temporary nodes to scan exabytes of data to deliver fast results.

 Organizations typically load most frequently accessed dimension and fact data into an Amazon Redshift cluster and keep up to exabytes of structured, semi-structured, and unstructured historical data in Amazon S3. Amazon Redshift Spectrum enables running complex queries that combine data in a cluster with data on Amazon S3 in the same query.

 Another capability to enable fast sharing between your data warehouse and data lake is [Amazon Redshift data lake export](https://aws.amazon.com/blogs/aws/new-for-amazon-redshift-data-lake-export-and-federated-queries/). You can now unload the result of an Amazon Redshift query to your Amazon S3 data lake as Apache Parquet. This enables you to save data transformation and enrichment you have done in Amazon Redshift into your Amazon S3 data lake in an open format. You can then analyze your data with Redshift Spectrum and other AWS services such as Amazon Athena, Amazon EMR, and Amazon SageMaker AI.

 Amazon Redshift provides native integration with Amazon S3 in the storage layer, Lake Formation catalog, and AWS services in the security and monitoring layer.

## Business intelligence
<a name="business-intelligence"></a>

 Quick provides a serverless BI capability to easily create and publish rich, interactive dashboards. QuickSight enriches dashboards and visuals with out-of-the- box, automatically generated ML insights such as forecasting, anomaly detection, and narrative highlights. QuickSight natively integrates with Amazon SageMaker AI to enable additional custom ML model-based insights to your BI dashboards. You can access QuickSight dashboards from any device using a QuickSight app, or you can [embed the dashboard into web applications, portals, and websites](https://docs.aws.amazon.com/quicksight/latest/user/embedding-dashboards.html).

 QuickSight allows you to directly connect to and import data from a wide variety of cloud and on-premises data sources.
+  SaaS applications, such as Salesforce, Square, ServiceNow, Twitter, GitHub, and JIRA
+  Third-party databases, such as Teradata, MySQL, Postgres, and SQL Server
+  Native AWS services, such as Amazon Redshift, Athena, Amazon S3, Amazon Relational Database Service (Amazon RDS), and [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
+  Private VPC subnets

 You can also upload a variety of file types including XLS, CSV, JSON, and Presto.

 To achieve blazing fast performance for dashboards, QuickSight provides an in-memory caching and calculation engine called SPICE. SPICE automatically replicates data for high availability and enables thousands of users to simultaneously perform fast, interactive analysis while shielding your underlying data infrastructure. QuickSight automatically scales to tens of thousands of users and provides a cost-effective, pay- per-session pricing model.

 QuickSight allows you to securely manage your users and content via a comprehensive set of security features, including role-based access control, Active Directory integration, [AWS CloudTrail](https://aws.amazon.com/cloudtrail) auditing, single sign-on (IAM or third-party), private VPC subnets, and data backup.

## Predictive analytics and ML
<a name="predictive-analytics-and-ml"></a>

 Amazon SageMaker AI is a fully managed service that provides components to build, train, and deploy ML models using an interactive development environment (IDE) called [Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/aws/amazon-sagemaker-studio-the-first-fully-integrated-development-environment-for-machine-learning/). In Amazon SageMaker AI Studio, you can upload data, create new notebooks, train and tune models, move back and forth between steps to adjust experiments, compare results, and deploy models to production, all in one place by using a unified visual interface. Amazon SageMaker AI also provides [managed Jupyter notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) that you can spin up with just a few clicks. Amazon SageMaker AI notebooks provide elastic compute resources, git integration, easy sharing, pre-configured ML algorithms, dozens of out-of-the-box ML examples, and *AWS Marketplace* integration, which enables easy deployment of hundreds of pre-trained algorithms. Amazon SageMaker AI notebooks are preconfigured with all major deep learning frameworks, including TensorFlow, PyTorch, Apache MXNet, Chainer, Keras, Gluon, Horovod, Scikit-learn, and Deep Graph Library.

 ML models are trained on Amazon SageMaker AI managed compute instances, including highly cost-effective Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances.

 You can organize multiple training jobs by using [Amazon SageMaker AI Experiments](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/). You can build training jobs using Amazon SageMaker AI built-in algorithms, your custom algorithms, or hundreds of algorithms you can deploy from AWS Marketplace. Amazon SageMaker AI Debugger provides full visibility into model training jobs. Amazon SageMaker AI also provides automatic hyperparameter tuning for ML training jobs.

 You can [deploy Amazon SageMaker AI trained models](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) into production with a few clicks and easily scale them across a fleet of fully managed EC2 instances. You can choose from multiple EC2 instance types and attach cost-effective [GPU-powered inference acceleration](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html). After the models are deployed, Amazon SageMaker AI can [monitor key model metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html) for inference accuracy and detect any concept drift.

 Amazon SageMaker AI provides native integrations with AWS services in the storage and security layers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
