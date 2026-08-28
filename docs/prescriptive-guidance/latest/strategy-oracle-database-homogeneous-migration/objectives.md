---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/objectives.html
---

# Migration objectives
<a name="objectives"></a>

You might want to move your Oracle workloads from your on-premises environment to AWS for various reasons. For example, you might want to reduce costs, increase agility, improve security, or refactor your workload more quickly. Whatever reasons are behind your decision, choosing the right migration strategy is important so that you can meet your goals and required timelines.

## Reducing cost
<a name="cost"></a>

Running Oracle databases in an on-premises environment might incur expensive licensing costs in the following scenarios:
+ Databases that are running on old hardware
+ Databases that no longer serve the purpose and are potential candidates for retiring
+ Databases that require modernization
+ Older databases that are retained because of compliance reasons such as personally identifiable information (PII), General Data Protection Regulation (GDPR), Fair Labor Standards Act (FLSA), or any other country-specific or industry-specific compliance

Based on the requirements of those scenarios, you might not want to allocate the same amount of resources to reduce licensing and operational costs, but you might want to automatically scale based on need, and you can achieve this more easily in the cloud. For a discussion of costs and risks, see the guide [Oracle cost traps and how to overcome them with AWS solutions](https://houseofbrick.com/wp-content/uploads/2021/01/Avoiding-the-Oracle-Traps-in-AWS.pdf) from House of Brick Technologies.

## Increasing agility
<a name="agility"></a>

Provisioning an Oracle database in an on-premises environment is typically a time-consuming activity that can take a few weeks or up to months. With Amazon Elastic Compute Cloud (Amazon EC2), you can spin up an Oracle database of the required size in a short time by using infrastructure as code (IaC).

The speed at which Oracle instances on AWS can scale up or down to meet your demand will help you complete developmental activities and make decisions quickly. Oracle databases that are rehosted on AWS can achieve increased agility for custom solutions. For example, when you host an Oracle database on Amazon EC2, you have the ability to [deploy multiple environments in seconds](https://aws.amazon.com/blogs/storage/synchronize-your-oracle-databases-quickly-and-easily-with-amazon-fsx-for-openzfs/).

## Improving security
<a name="security"></a>

Organizations that run Oracle databases on premises are responsible for security at all layers, including data at rest and in transit. This can result in an incomplete security configuration, which potentially leaves the database at risk. With the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS manages infrastructure security while you are responsible for configuring security at the EC2 instance and Oracle database layer.

You can restrict public access to the EC2 instance that hosts the Oracle database so that applications outside the virtual private cloud (VPC) won't be able to access the database. You can use an [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) key to encrypt all the storage allocated to the databases at rest all the time, which helps fulfill compliance requirements. You can configure these security policies from the AWS Management Console.

## Faster refactoring
<a name="refactoring"></a>

Databases that are already on AWS are easier to refactor compared with on-premises databases. A database that is already on AWS has the necessary infrastructure, including VPCs, security groups, and networking. When you're ready to modernize the database, you can use your existing AWS infrastructure to launch your refactored database engine. If this is your goal, you can migrate your Oracle database to AWS first, and then start the process of refactoring or modernizing it.

Additional refactoring options that can help reduce licensing costs and operational overhead include the following:
+ Offload the databases by archiving the data to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ Migrate Oracle data warehouse databases to [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
+ Migrate Oracle databases to open source databases:
  + [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
  + [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)
  + [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
  + [Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
