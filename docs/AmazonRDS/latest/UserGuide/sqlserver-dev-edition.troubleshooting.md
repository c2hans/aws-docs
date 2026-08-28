---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.troubleshooting.html
---

# Troubleshooting SQL Server Developer Edition for RDS for SQL Server
<a name="sqlserver-dev-edition.troubleshooting"></a>

The following table lists some common errors and corresponding solutions when working with SQL Server Developer Edition for RDS for SQL Server

**Common Errors and Solutions**

| Error Code | Description | Solution |
| --- | --- | --- |
| InvalidParameterValue | Invalid CEV parameters or file references | Verify file names, paths, and parameter syntax |
| DBSubnetGroupNotFound | Subnet group doesn't exist | Create subnet group or verify name |
| InvalidVPCNetworkState | VPC configuration issue | Check VPC, subnets, and routing tables |
| InvalidEngineVersion | CEV not available or invalid | Verify CEV status and name |
| InvalidDBInstanceClass | Instance class not supported | Choose supported instance class |
| CustomDBEngineVersionQuotaExceededFault | You have reached the maximum number of custom engine versions | If required increase service quota, alternatively Delete unused CEVs if required |
| CreateCustomDBEngineVersionFault | Amazon RDS was unable to access the specified installer file in the Amazon S3 bucket. | Amazon RDS cannot access the SQL Server installation files in the specified Amazon S3 location. Grant the Amazon RDS service principal (rds.amazonaws.com) s3:GetObject permission in your Amazon S3 bucket policy. Validate that the Amazon S3 bucket Region is the same as the Region where you are creating the CEV. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
