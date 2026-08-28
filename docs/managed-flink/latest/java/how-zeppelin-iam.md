---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-iam.html
---

# Review IAM permissions for Studio notebooks
<a name="how-zeppelin-iam"></a>

Managed Service for Apache Flink creates an IAM role for you when you create a Studio notebook through the AWS Management Console. It also associates with that role a policy that allows the following access:

| Service | Access  |
| --- | --- |
| CloudWatch Logs | List |
| Amazon EC2 | List |
| AWS Glue | Read, Write |
| Managed Service for Apache Flink | Read |
| Managed Service for Apache Flink V2 | Read |
| Amazon S3 | Read, Write |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
