---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.html
---

# Step-by-step Amazon RDS for SQL Server database to an Amazon S3 data lake migration walkthrough
<a name="chap-rdssqlserver2s3datalake.steps"></a>

The following steps provide instructions for migrating an Amazon RDS for SQL Server database to an Amazon S3 data lake. These steps assume that you have already prepared your source database as described in [Prerequisties for migrating from an Amazon RDS for SQL Server database to an Amazon S3 data lake](chap-rdssqlserver2s3datalake.prerequisites.md).

**Topics**
+ [Step 1: Create an AWS DMS Replication Instance](chap-rdssqlserver2s3datalake.steps.createreplicationinstance.md)
+ [Step 2: Configure a Source Amazon RDS for SQL Server Database](chap-rdssqlserver2s3datalake.steps.configuresource.md)
+ [Step 3: Create an AWS DMS Source Endpoint](chap-rdssqlserver2s3datalake.steps.sourceendpoint.md)
+ [Step 4: Configure a Target Amazon S3 Bucket](chap-rdssqlserver2s3datalake.steps.targets3bucket.md)
+ [Step 5: Configure an AWS DMS Target Endpoint](chap-rdssqlserver2s3datalake.steps.targetendpoint.md)
+ [Step 6: Create an AWS DMS Task](chap-rdssqlserver2s3datalake.steps.createtask.md)
+ [Step 7: Run the AWS DMS Task](chap-rdssqlserver2s3datalake.steps.runtask.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
