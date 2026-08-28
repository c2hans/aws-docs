---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-compute-rds-connect.html
---

# Automatically connecting an AWS compute resource and a Multi-AZ DB cluster for Amazon RDS
<a name="multi-az-compute-rds-connect"></a>

You can automatically connect a Multi-AZ DB cluster and AWS compute resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances and AWS Lambda functions.

The following topics provide detailed instructions for configuring network settings, security groups, and connection parameters to establish reliable connections to Amazon RDS DB instances within a Multi-AZ DB cluster deployment. They focus on optimizing network connectivity and performance for applications interacting with Multi-AZ DB cluster, ensuring secure and efficient data operations.

**Topics**
+ [Automatically connecting an EC2 instance and a Multi-AZ DB cluster](multiaz-ec2-rds-connect.md)
+ [Automatically connecting a Lambda function and a Multi-AZ DB cluster](multiaz-lambda-rds-connect.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
