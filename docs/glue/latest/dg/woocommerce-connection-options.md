---
source_url: https://docs.aws.amazon.com/glue/latest/dg/woocommerce-connection-options.html
---

# WooCommerce connection options
<a name="woocommerce-connection-options"></a>

The following are connection options for WooCommerce:
+ `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in WooCommerce.
+ `API_VERSION`(String) - (Required) Used for Read. WooCommerce Rest API version you want to use.
+ `REALM_ID`(String) - An ID that identifies an individual WooCommerce Online company where you send requests.
+ `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+ `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
+ `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
+ `INSTANCE_URL`(String) - (Required) A valid WooCommerce instance URL with the format: https://<instance>.wpcomstaging.com
+ `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
