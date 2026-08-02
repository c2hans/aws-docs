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
