---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/restrictedcommands.html
---

# Restricted commands
<a name="restrictedcommands"></a>

To deliver a managed service experience, MemoryDB restricts access to certain commands that require advanced privileges. The following commands are unavailable:
+ `acl deluser`
+ `acl load`
+ `acl save`
+ `acl setuser`
+ `bgrewriteaof`
+ `bgsave`
+ `cluster addslot`
+ `cluster delslot`
+ `cluster setslot`
+ `config`
+ `debug`
+ `migrate`
+ `module`
+ `psync`
+ `replicaof`
+ `save`
+ `shutdown`
+ `slaveof`
+ `sync`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
