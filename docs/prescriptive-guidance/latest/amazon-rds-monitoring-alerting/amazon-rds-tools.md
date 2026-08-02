---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/amazon-rds-tools.html
---

# Tools included in Amazon RDS
<a name="amazon-rds-tools"></a>

Amazon Relational Database Service (Amazon RDS) is a managed database service in the AWS Cloud. Because Amazon RDS is a managed service, it frees you from most management tasks, such as database backups, operating system (OS) and database software installations, OS and software patching, high availability setup, hardware lifecycle, and data center operations. AWS also provides a comprehensive set of tools that enable you to build a complete [observability](https://aws.amazon.com/products/management-and-governance/use-cases/monitoring-and-observability/) solution for your Amazon RDS DB instances.

Some of the monitoring tools are included, preconfigured, and automatically enabled in the Amazon RDS service. Two automated tools are available to you as soon as you start your new Amazon RDS instance:
+ **Amazon RDS instance status** provides details about the current health of your DB instance. For example, status codes include *Available*, *Stopped*, *Creating*, *Backing-up*, and *Failed*. You can use the Amazon RDS console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API to see instance status. For more information, see [Viewing Amazon RDS DB instance status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/accessing-monitoring.html#Overview.DBInstance.Status) in the Amazon RDS documentation.
+ **Amazon RDS recommendations** provide automated recommendations for DB instances, read replicas, and DB parameter groups. These recommendations are provided by analyzing DB instance usage, performance data, and configuration, and are delivered as guidance. For example, the *Engine version outdated* recommendation suggests that your DB instances aren't running the latest version of the database software and that you should upgrade your DB instance to benefit from the latest security fixes and other improvements. For more information, see [Viewing Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html) in the Amazon RDS documentation.
