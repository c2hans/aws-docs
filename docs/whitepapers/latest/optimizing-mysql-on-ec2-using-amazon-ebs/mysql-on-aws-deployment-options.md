---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/mysql-on-aws-deployment-options.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MySQL on AWS deployment options
<a name="mysql-on-aws-deployment-options"></a>

 AWS provides various options to deploy MySQL like a fully managed database service, [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) for MySQL. The [Amazon Aurora](https://aws.amazon.com/rds/aurora/) database engine is designed to be wire-compatible with MySQL 5.6 and 5.7 using the InnoDB storage engine. You can also host MySQL on Amazon EC2 and self-manage the database, or browse the third-party MySQL offerings on the [AWS Marketplace](https://aws.amazon.com/marketplace). This whitepaper explores the implementation and deployment considerations for MySQL on Amazon EC2 using Amazon EBS for storage.

 Although Amazon RDS and Amazon Aurora with MySQL compatibility is a good choice for most of the use cases on AWS, deployment on Amazon EC2 might be more appropriate for certain MySQL workloads. With Amazon RDS you can connect to the database itself, which gives you access to the familiar capabilities and configurations in MySQL; however, access to the operating system (OS) isn’t available. This is an issue when you need OS-level access due to specialized configurations that rely on low-level OS settings, such as when using MySQL Enterprise tools. For example, enabling MySQL Enterprise Monitor requires OS-level access to gather monitoring information. As another example, MySQL Enterprise Backup requires OS-level access to access the MySQL data directory. In such cases, running MySQL on Amazon EC2 is a better alternative.

 MySQL can be scaled vertically by adding additional hardware resources (CPU, memory, disk, network) to the same server. For both Amazon RDS and Amazon EC2, you can change the EC2 instance type to match the resources required by your MySQL database. Amazon Aurora provides a Serverless MySQL-Compatible Edition that allows compute capacity to be auto scaled on demand based on application needs. Both Amazon RDS and Amazon EC2 have an option to use EBS General Purpose SSD and EBS Provisioned IOPS volumes. The maximum provisioned storage limit for Amazon RDS database (DB) instances running MySQL is 64 TB. The EBS volume for MySQL on Amazon EC2, conversely, supports up to 16 TB per volume.

 Horizontal scaling is also an option in MySQL, where you can add MySQL secondary servers or read replicas so that you can accommodate additional read traffic into your database. With Amazon RDS, you can easily enable this option through the AWS Management Console with click of a button, Command Line Interface (CLI), or REST API. Amazon RDS for MySQL allows up to five read replicas. There are certain cases where you might need to enable specific MySQL replication features. Some of these features may require OS access to MySQL or advanced privileges to access certain system procedures and tables.

 MySQL on Amazon EC2 is an alternative to Amazon RDS and Aurora for certain use cases. It allows you to migrate new or existing workloads that have very specific requirements. Choosing the right compute, network, and—especially—storage configurations while taking advantage of its features plays a crucial role in achieving good performance at an optimal cost for your MySQL workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
