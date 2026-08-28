---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-mysql.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Export MySQL Data to Amazon S3 Using AWS Data Pipeline
<a name="dp-copydata-mysql"></a>

This tutorial walks you through the process of creating a data pipeline to copy data (rows) from a table in MySQL database to a CSV (comma-separated values) file in an Amazon S3 bucket and then sending an Amazon SNS notification after the copy activity completes successfully. You will use an EC2 instance provided by AWS Data Pipeline for this copy activity.

**Pipeline Objects**
The pipeline uses the following objects:
+ [CopyActivity](dp-object-copyactivity.md)
+ [Ec2Resource](dp-object-ec2resource.md)
+ [MySqlDataNode](dp-object-mysqldatanode.md)
+ [S3DataNode](dp-object-s3datanode.md)
+ [SnsAlarm](dp-object-snsalarm.md)

**Topics**
+ [Before You Begin](dp-copydata-mysql-prereq.md)
+ [Copy MySQL Data Using the Command Line](dp-copymysql-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
