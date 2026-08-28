---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Microsoft Exchange connector
<a name="exchange-limitations"></a>

**Note**
**Legacy version notice:** We recommend using the latest connector for improved performance and retrieval quality. The following limitations apply only to the legacy connector version.

The original Microsoft Exchange connector has these known limitations:
+ When you enable Access Control Lists (ACLs), the "Sync only new or modified content" option is not available due to Microsoft Exchange API limitations. Use "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs to use this sync mode.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
