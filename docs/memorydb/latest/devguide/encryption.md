---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/encryption.html
---

# Data security in MemoryDB
<a name="encryption"></a>

To help keep your data secure, MemoryDB and Amazon EC2 provide mechanisms to guard against unauthorized access of your data on the server.

MemoryDB also provides encryption features for data on clusters:
+ In-transit encryption encrypts your data whenever it is moving from one place to another, such as between nodes in your cluster or between your cluster and your application.
+ At-rest encryption encrypts the transaction log and your on-disk data during snapshot operations.

You can also use [Authenticating users with Access Control Lists (ACLs)](clusters.acls.md) to control user access to your clusters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
