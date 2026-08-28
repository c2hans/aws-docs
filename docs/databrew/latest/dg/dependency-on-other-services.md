---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/dependency-on-other-services.html
---

# DataBrew dependency on other AWS services
<a name="dependency-on-other-services"></a>

To work with the DataBrew console, you need a minimum set of permissions to work with the DataBrew resources for your AWS account. In addition to these DataBrew permissions, the console requires permissions from the following services:
+ CloudWatch Logs permissions to display logs.
+ IAM permissions to list and pass roles.
+ Amazon EC2 permissions to list VPCs, subnets, security groups, instances, and other objects. DataBrew uses these permissions to set up Amazon EC2 items such as VPCs when running DataBrew jobs.
+ Amazon S3 permissions to list buckets and objects.
+ AWS Glue permissions to read AWS Glue schema objects, such as databases, partitions, tables, and connections.
+ AWS Lake Formation permissions to work with Lake Formation data lakes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
