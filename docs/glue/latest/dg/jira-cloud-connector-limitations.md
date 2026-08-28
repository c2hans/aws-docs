---
source_url: https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-connector-limitations.html
---

# Limitations and notes for Jira Cloud connector
<a name="jira-cloud-connector-limitations"></a>

The following are limitations or notes for the Jira Cloud connector:
+  The `Contains` operator does not work with the `resourceName` field, which is of `String` data type.
+  By default, if no explicit filter is applied, only issues from the past 30 days will be crawled. Users have the option to override this default filter by specifying a custom filter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
