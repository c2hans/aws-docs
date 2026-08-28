---
source_url: https://docs.aws.amazon.com/glue/latest/dg/domo-connection-limitations.html
---

# Domo limitations
<a name="domo-connection-limitations"></a>

The following are limitations or notes for Domo:
+ Due to an SDK limitation, filtration does not work as expected for the queryable fields that starts with '\_' (for example: \_BATCH\_ID ).
+ Due to an API limitation, filtration works on the date prior to the date you provide. This also affects incremental pull. To overcome this limitation, select a date according to your time zone against UTC, for getting data for the required date.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
