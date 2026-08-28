---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/migrate-data.html
---

# Migrating data associated with SAS
<a name="migrate-data"></a>

We recommend that you move the data associated with your SAS applications to AWS. This migration has several benefits:
+ Gaining access to cloud-based data lakes and data warehouses
+ Increased agility, performance, security, and reliability
+ Lower costs

AWS offers a wide variety of services and tools to help you migrate your data sets, including SAS files, databases, machine images, block volumes, and even tape backups. The following table provides a list of services that you can use.

|
|
| AWS service | Description | Role/skills required |
| --- |--- |--- |
| [AWS DataSync](https://aws.amazon.com/datasync/) | Copies or replicates file system data to Amazon S3 or Amazon Elastic File System (Amazon EFS). | AWS architect |
| [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) | Migrates running machine images with their data to Amazon EC2. | AWS architect |
| [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration) | Enables fast and secure transfers of data to Amazon S3 over long geographic distances. | AWS architect |
| [AWS DMS](https://aws.amazon.com/dms/) | Migrates databases to AWS quickly and securely, with minimal downtime. | AWS architect |
| [AWS Snow Family](https://aws.amazon.com/snow/) | Physically transports petabytes of data in batches to AWS. | AWS architect |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
