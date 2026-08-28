---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migration-and-assessment-tools-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration and assessment tools on AWS
<a name="migration-and-assessment-tools-on-aws"></a>

 Along with the Oracle E-Business Suite specific tools mentioned previously, you can also make use of various other AWS services to migrate files and objects from on premises to AWS.
+  [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) – Can be used for application discovery, building a business case, and right-sizing environments on AWS.
+  [AWS Snowball Edge](https://aws.amazon.com/snowball/) – Can be used to move terabytes of data in about a week on AWS. You can use it to move digital assets such as databases, backups and media content. Example for a very large database would be to take an RMAN full backup a number of weeks in advance (to allow time for shipping to AWS) and then restore the standby and apply the redologs in AWS – keeping the database in sync with on premises.
+  [AWS DataSync](https://aws.amazon.com/datasync/) – Can be used to move large amounts of data online between on-premises storage and Amazon S3, [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS), [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/), [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/), [Amazon FSx for OpenZFS](https://aws.amazon.com/fsx/openzfs/), or [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/).
+  [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) – Can be used for implementing hybrid cloud storage use cases such as moving backups to the cloud, or using on-premises file shares backed by cloud storage.
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) – Can be used to establish a dedicated network connection from on premises to AWS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
