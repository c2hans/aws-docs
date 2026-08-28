---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/indexes.html
---

# Indexes
<a name="indexes"></a>

Indexes improve query performance by allowing Amazon DocumentDB to quickly locate documents without scanning every document in a collection. You can create indexes on fields that your application queries frequently to reduce latency and I/O costs.

For additional index-related topics, see:
+ [Managing Amazon DocumentDB indexes](managing-indexes.md) — creating and building indexes
+ [Working with indexes](best_practices.md#best_practices-indexes) — indexing best practices
+ [Troubleshooting indexes](troubleshooting.index-creation.md) — resolving index build failures and bloat
+ [How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage) — finding unused and missing indexes

**Topics**
+ [Index management](index-management.md)
+ [Index types](index-types.md)
+ [Index properties](index-properties.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
