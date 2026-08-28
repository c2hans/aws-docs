---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dependency-on-other-services.html
---

# AWS Glue dependency on other AWS services
<a name="dependency-on-other-services"></a>

For a user to work with the AWS Glue console, that user must have a minimum set of permissions that allows them to work with the AWS Glue resources for their AWS account. In addition to these AWS Glue permissions, the console requires permissions from the following services:
+ Amazon CloudWatch Logs permissions to display logs.
+ AWS Identity and Access Management (IAM) permissions to list and pass roles.
+ CloudFormation permissions to work with stacks.
+ Amazon Elastic Compute Cloud (Amazon EC2) permissions to list virtual private clouds (VPCs), subnets, security groups, instances, and other objects (to set up Amazon EC2 items such as VPCs when running jobs, crawlers, and creating development endpoints).
+ Amazon Simple Storage Service (Amazon S3) permissions to list buckets and objects, and to retrieve and save scripts.
+ Amazon Redshift permissions to work with clusters.
+ Amazon Relational Database Service (Amazon RDS) permissions to list instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
