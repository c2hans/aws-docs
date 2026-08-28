---
source_url: https://docs.aws.amazon.com/glue/latest/dg/asana-connection-options.html
---

# Asana connection options
<a name="asana-connection-options"></a>

The following are connection options for Asana:
+  `ENTITY_NAME`(String) – (Required) Used for Read/Write. The name of your Object in Asana.
+  `API_VERSION`(String) – (Required) Used for Read/Write. Asana Rest API version you want to use. For example: 1.0.
+  `SELECTED_FIELDS`(List<String>) – Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+  `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be in the Spark SQL format.
+  `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.
+ `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
+  `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
+  `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
+  `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
