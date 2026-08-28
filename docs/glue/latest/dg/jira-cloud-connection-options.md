---
source_url: https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-connection-options.html
---

# Jira Cloud connection options
<a name="jira-cloud-connection-options"></a>

The following are connection options for Jira Cloud:
+ `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Jira Cloud.
+ `API_VERSION`(String) - (Required) Used for Read. Jira Cloud Rest API version you want to use. For example: v3.
+ `DOMAIN_URL`(String) - (Required) The Jira Cloud ID you want to use.
+ `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+ `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
+ `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
+ `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
