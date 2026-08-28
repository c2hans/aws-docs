---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/batch-host-logs-cleanup.html
---

# Step 5: Clean up resources
<a name="batch-host-logs-cleanup"></a>

If you no longer need the host-level log collection, remove the following resources to avoid unnecessary charges:

1. Delete or drain the compute environment that uses the launch template.

1. Delete the launch template from the Amazon EC2 console or by running `aws ec2 delete-launch-template`.

1. Detach and delete the `BatchHostLogsS3Access` IAM policy from your instance role.

1. Empty and delete the Amazon S3 bucket, or remove only the `ecs-logs/` and `fluent-bit/` prefixes if the bucket is shared with other workloads.

1. If you set `minvCpus` to a non-zero value for testing, reset it to zero to avoid unnecessary costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
