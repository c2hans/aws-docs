---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Slack connector
<a name="slack-limitations"></a>

The Slack connector has the following known limitations:
+ Due to API limitations, the Amazon Q Slack connector can only retrieve a maximum of 100 pages, with 100 files per page. Given this limitation, the Slack connector can only crawl a maximum of 10,000 files per channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
