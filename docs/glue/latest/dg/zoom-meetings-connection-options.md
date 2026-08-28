---
source_url: https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-connection-options.html
---

# Zoom Meetings connection options
<a name="zoom-meetings-connection-options"></a>

The following are connection options for Zoom Meetings:
+ `ENTITY_NAME`(String) - (Required) Used for Read. The name of the Zoom Meetings entity. For example, `group`.
+ `API_VERSION`(String) - (Required) Used for Read. Zoom Meetings Rest API version you want to use. The value will be `v2`, as Zoom Meetings currently supports only version v2.
+ `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. A comma-separated list of columns you want to select for the selected entity.
+ `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
+ `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
