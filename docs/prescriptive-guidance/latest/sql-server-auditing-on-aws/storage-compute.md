---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/storage-compute.html
---

# Storage and compute requirements for auditing
<a name="storage-compute"></a>

## For Amazon RDS
<a name="for-amazon-rds.e3872d5d-71a9-5a2f-8357-c0e4b202cb12"></a>
+ Audit logs are first stored locally to disk at the location `D:\rdsdbdata\SQLAudit`. Amazon RDS then uploads these files to an S3 bucket that's configured in the `SQLSERVER_AUDIT` option group by using the specified IAM role.
+ If you enable retention, Amazon RDS moves the file into the retention folder at `D:\rdsdbdata\SQLAudit\transmitted`. Audit records are kept on the DB instance until the audit log file is uploaded to Amazon S3.
+ Make sure to provision sufficient storage space for the instance based on the retention period.
+ CPU consumption for running audits is generally minimal. Monitor CPU usage when you run audit queries and size the Amazon RDS DB instance accordingly. You can monitor [Amazon RDS metrics with Amazon CloudWatch.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html)

## For Amazon EC2
<a name="for-amazon-ec2.1bb53b3d-9ce4-5e8f-af9d-124a32ab1545"></a>
+ Make sure that there is sufficient storage space provisioned on the drive that stores the audit log files based on the retention period.
+ CPU consumption for running audits is generally minimal. Monitor CPU usage when you run audit queries and size the EC2 instance accordingly. You can use [Amazon CloudWatch to monitor EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/using-cloudwatch.html).
