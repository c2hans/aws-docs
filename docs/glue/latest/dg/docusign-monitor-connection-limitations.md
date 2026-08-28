---
source_url: https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-connection-limitations.html
---

# Docusign Monitor limitations
<a name="docusign-monitor-connection-limitations"></a>

The following are limitations or notes for Docusign Monitor:
+ When a filter is applied using the `cursor` field, the API retrieves records for the next seven days starting from the specified date.
+ If no filter is provided, the API retrieves records for the previous seven days from the current date of the API request.
+ Docusign Monitor does not support either field-based or record-based partitioning.
+ Docusign Monitor does not support the Order By feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
