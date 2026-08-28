---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Verify.html
---

# Verifying the data migration progress
<a name="Migration-Verify"></a>

After the data migration has begun, you can do the following to track its progress:
+ Verify that Valkey or Redis OSS `master_link_status` is `up` in the `INFO` command on ElastiCache primary node(s). You can also find this information in the ElastiCache console. Select the cluster and under **CloudWatch metrics**, observe **Primary Link Health Status**. After the value reaches 1, the data is in sync.
+ You can check that the ElastiCache replica has an **online** state by running the `INFO` command on your Valkey or Redis OSS instances. Doing this also provides information about replication lag.
+ Verify low client output buffer by using the [CLIENT LIST](https://valkey.io/commands/client-list) command on your Valkey or Redis OSS instances.

After the data migration is complete, the data is in sync with any new writes coming to the primary node(s) of your Valkey or Redis OSS cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
