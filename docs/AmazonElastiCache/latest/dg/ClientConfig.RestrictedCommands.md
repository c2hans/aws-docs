---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.RestrictedCommands.html
---

# Restricted commands
<a name="ClientConfig.RestrictedCommands"></a>

To deliver a managed service experience, ElastiCache restricts access to certain cache engine-specific commands that require advanced privileges. For clusters running Redis OSS, the following commands are unavailable:
+ `bgrewriteaof`
+ `bgsave`
+ `config`
+ `debug`
+ `migrate`
+ `replicaof`
+ `save`
+ `slaveof`
+ `shutdown`
+ `sync`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
