---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gcal-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Google Calendar connector (Preview)
<a name="gcal-limitations"></a>

The connector employs a rolling window approach for indexing data. This rolling window mechanism spans a total of six months, with four months of historical data and two months of future data. As the connector syncs and ingests new data, the oldest data that falls beyond the four-month historical window is automatically purged from the index. Simultaneously, new data for the upcoming two months is added to the index, allowing for future data visibility and analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
