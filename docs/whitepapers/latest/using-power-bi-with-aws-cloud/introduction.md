---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/introduction.html
---

# Introduction
<a name="introduction"></a>

Customers with businesses of all sizes are using AWS products and services to store their data reliably, cost effectively, and securely. This is due in part to the broad ecosystem of mature data storage and analytics offerings that are available. Some of these offerings include the following services:
+ [ Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) provides a simple, scalable, secure, and cost-effective data repository. It has become an industry standard for storing application data, as well as a first choice for customer data lakes.
+ [ Amazon Athena](https://aws.amazon.com/athena/) is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
+  [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups. SQL Server, Oracle Database, MySQL, MariaDB, and PostgreSQL engines are available.
+ [ Amazon Redshift](https://aws.amazon.com/redshift/) is fully managed, massively scalable data warehouse that makes it easy to analyze both structured and unstructured datasets.
+  [Amazon Quick](https://aws.amazon.com/quicksight/) is a fast, cloud-powered business intelligence service that makes it easy to deliver insights to everyone in your organization.
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) makes it easy for you to perform interactive log analytics, near real-time application monitoring, website search, and more.
+  [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) is a service that makes it easy to set up a secure data lake in days.

To better understand how services relate to one another, we often label data services as either being *data sources* or *data consumers*. A data source allows customers and applications to store and retrieve data from the service. Frequently, data sources also have built-in compute and can provide computational analysis and filtering. But ultimately, data is loaded into these data sources and eventually data is retrieved from them by data consumers. Amazon S3, Amazon Athena, and Amazon Redshift are good examples of data sources.

Data consumers, on the other hand, access the data from data sources and, typically, process it. They might optionally display it too. Amazon Quick and the Microsoft Power BI suite are good examples of data consumers. They read from data sources, and then assist in the analysis, visualization, and publication of information.

AWS gives customers full flexibility in mixing the technologies they prefer for their data needs. While many customers choose Amazon Quick for their business intelligence (BI) needs, other customers choose vendors such as Microsoft Power BI, Tableau, and Qlik.

This document focuses on the Microsoft Power BI suite of products and services, and how to use them in combination with AWS services.
