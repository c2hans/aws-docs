---
source_url: https://docs.aws.amazon.com/efs/latest/ug/install-botocore.html
---

# Installing and upgrading `botocore`
<a name="install-botocore"></a>

The Amazon EFS client uses `botocore` to interact with other AWS services. It is required if you want to monitor mount attempt success or failure for your EFS file systems in CloudWatch Logs. For more information, see [Monitoring mount attempt successes and failures](how-to-monitor-mount-status.md).

For instructions on installing and upgrading `botocore`, see [ Installing `botocore`](https://github.com/aws/efs-utils/blob/master/README.md#install-botocore) in the `amazon-efs-utils` README on Github.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
