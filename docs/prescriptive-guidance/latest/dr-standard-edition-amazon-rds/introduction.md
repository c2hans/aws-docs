---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/introduction.html
---

# Choosing a DR capability for standard editions of Amazon RDS for Oracle and SQL Server
<a name="introduction"></a>

*Gokul Gunasekaran and Sawan Saxena, Amazon Web Services*

In data-driven industries, it's essential to have high availability and swift recovery for the data that is stored in databases. Therefore, you must understand the importance of disaster recovery (DR) strategies, and build a robust solution to recover the databases rapidly in the event of a crisis. A wide range of DR options are available for [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) on the Amazon Web Services (AWS) Cloud.

This guide focuses on the DR options for standard editions of Oracle and Microsoft SQL Server on Amazon RDS. It covers both active-active and active-passive DR scenarios, and it discusses the benefits and limitations of each option. This guide also provides examples and case studies to help you understand how DR plans can be tailored to your organization's specific needs.

## The scope of standard edition database engines
<a name="scope"></a>

Standard editions of Oracle and SQL Server database engines are widely adopted by customers for their known cost effectiveness and basic use cases. Compared with enterprise editions, standard editions offer the minimal features that are essential to run basic database workloads. If you are managing your workloads with the available limited features in standard editions, you might prefer this for its affordable license costs. If you are migrating your database workloads to the cloud, this is a good time to evaluate whether you can fit your use cases to standard edition versions and reduce costs.

These factors have significantly increased the scope of standard edition database workloads in the cloud and the need for disaster recovery solutions across AWS Regions to increase resiliency.
