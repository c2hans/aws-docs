---
source_url: https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-limitations.html
---

# Zoom Meetings limitations
<a name="zoom-meetings-limitations"></a>

The following are limitations or notes for Zoom Meetings:
+ Zoom Meetings does not support orderby.
+ Zoom Meetings does not support filter-based partitioning because there is no field that can satisfy the required criteria.
+ Zoom Meetings does not support record-based partitioning because the pagination limit and offset-based pagination is not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
