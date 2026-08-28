---
source_url: https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-connection-options.html
---

# Instagram Ads connection options
<a name="instagram-ads-connection-options"></a>

The following are connection options for Instagram Ads:
+ `ENTITY_NAME`(String) - (Required) Used for read. The name of your object in Instagram Ads.
+ `API_VERSION`(String) - (Required) Used for read. Instagram Ads Graph API version you want to use. For example: v21.
+ `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for read. Columns you want to select for the object.
+ `FILTER_PREDICATE`(String) - Default: empty. Used for read. It should be in the Spark SQL format.
+ `QUERY`(String) - Default: empty. Used for read. Full Spark SQL query.
+ `PARTITION_FIELD`(String) - Used for read. Field to be used to partition query.
+ `LOWER_BOUND`(String)- Used for read. An inclusive lower bound value of the chosen partition field.
+ `UPPER_BOUND`(String) - Used for read. An exclusive upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`(Integer) - Default: 1. Used for read. Number of partitions for read.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
