---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-prerequisites.html
---

# Data tiering limitations
<a name="data-tiering-prerequisites"></a>

Data tiering has the following limitations:
+ The node type you use must be from the r6gd family, which is available in the following regions: `us-east-2`, `us-east-1`, `us-west-2`, `us-west-1`, `eu-west-1`, `eu-west-3`, `eu-central-1`, `ap-northeast-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-south-1`, `ca-central-1` and `sa-east-1`.
+ You cannot restore a snapshot of an r6gd cluster into another cluster unless it also uses r6gd.
+ You cannot export a snapshot to Amazon S3 for data-tiering clusters.
+ Forkless save is not supported.
+ Scaling is not supported from a data tiering cluster (for example, a cluster using an r6gd node type) to a cluster that does not use data tiering (for example, a cluster using an r6g node type).
+ Data tiering only supports `volatile-lru`, `allkeys-lru` and `noeviction` maxmemory policies.
+ Items larger than 128 MiB are not moved to SSD.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
