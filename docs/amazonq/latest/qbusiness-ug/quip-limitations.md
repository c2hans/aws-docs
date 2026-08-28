---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quip-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Amazon Q Business Quip connector
<a name="quip-limitations"></a>

The Quip connector has the following known limitations:
+ Only **Full sync** is supported by default. For **New, modified, or deleted content sync**, Admin API access is required and Admin API has to be enabled on the Quip website .
+ Only data in shared folders will be crawled by the Amazon Q Quip connector. Private folders, other than the private folders belonging to the Private Access Token user, will not be crawled.
+ Quip doesn't store file types and file paths. Amazon Q Quip connector can't support inclusion and exclusion filters on these.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
