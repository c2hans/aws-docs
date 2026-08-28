---
source_url: https://docs.aws.amazon.com/glue/latest/dg/mixpanel-connection-options.html
---

# Mixpanel connection options
<a name="mixpanel-connection-options"></a>

The following are connection options for Mixpanel:
+  `ENTITY_NAME` (String) – (Required) Used for Read/Write. The name of your Object in Mixpanel.
+  `API_VERSION` (String) – (Required) Used for Read/Write. Mixpanel Rest API version you want to use. For example: v2.0.
+  `SELECTED_FIELDS`(List<String>) – Default: empty (SELECT \*). Used for Read. Columns you want to select for the object.
+  `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be in the Spark SQL format.
+  `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
