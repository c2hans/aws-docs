---
source_url: https://docs.aws.amazon.com/glue/latest/dg/zendesk-limitations.html
---

# Limitations
<a name="zendesk-limitations"></a>

The following are limitations of the Zendesk connector:
+ Offset-based pagination limits the number of pages that can be fetched to 100, but it not recommended as the total number of records that can be fetched is 10,000. However, the cursor-based pagination that is implemented for the Zendesk connector overcomes this limitation. Only the EQUAL\_TO filter operator is supported through the Zendesk API.

  Because of this limitation, partitioning is not supported for the Zendesk connector.
+ For the "Ticket Event" entity the Rate Limit is 10 requests per minute. While running a AWS Glue ETL job you may receive a 429 (too many requests) error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
